from rest_framework import serializers
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
    show_themes = ShowThemeSerializer(many=True)


class ShowSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show", "planetary_dome", "show_time")


class ShowSessionListSerializer(ShowSessionSerializer):
    astronomy_show = AstronomyShowSerializer()
    planetary_dome = PlanetaryDomeSerializer()











