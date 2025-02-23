from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from planetarium.models import (
    ShowTheme,
    AstronomyShow,
    PlanetaryDome,
    ShowSession,
    Reservation,
    Ticket
)


class ShowThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTheme
        fields = ("id", "name")


class PlanetaryDomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanetaryDome
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "show_themes")


class AstronomyShowListSerializer(AstronomyShowSerializer):
    show_themes = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class AstronomyShowRetrieveSerializer(AstronomyShowSerializer):
    show_themes = ShowThemeSerializer(many=True)


class ShowSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show", "planetary_dome", "show_time")


class ShowSessionListSerializer(ShowSessionSerializer):
    astronomy_show = serializers.CharField(source="astronomy_show.title", read_only=True)
    planetary_dome = serializers.CharField(source="planetary_dome.name", read_only=True)


class ShowSessionRetrieveSerializer(ShowSessionSerializer):
    astronomy_show = AstronomyShowSerializer(read_only=True)
    planetary_dome = PlanetaryDomeSerializer(read_only=True)
    taken_seats = serializers.SerializerMethodField()

    def get_taken_seats(self, obj):
        return [{"row": ticket.row, "seat": ticket.seat} for ticket in obj.tickets.all()]

    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show", "planetary_dome", "show_time", "taken_seats")

class TicketSerializer(serializers.ModelSerializer):
    astronomy_show = serializers.CharField(source="show_session.astronomy_show.title", read_only=True)
    planetary_dome = serializers.CharField(source="show_session.planetary_dome.name", read_only=True)

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "show_session", "astronomy_show", "planetary_dome")
        validators = [
            UniqueTogetherValidator(
                queryset=Ticket.objects.all(),
                fields=["row", "seat", "show_session"]
            )
        ]

    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs=attrs)
        Ticket.validate_ticket(
            attrs["row"],
            attrs["seat"],
            attrs["show_session"].planetary_dome,
            ValidationError
        )
        return data


class ReservationSerializer(serializers.ModelSerializer):

    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Reservation
        fields = ("id", "created_at", "tickets")

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            reservation = Reservation.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(reservation=reservation, **ticket_data)
            return reservation
