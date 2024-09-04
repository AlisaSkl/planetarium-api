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


# class AstronomyShowListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AstronomyShow
#         fields = ("id", "title", "description", "show_theme") many-to-many







