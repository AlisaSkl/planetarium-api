from django.db.migrations import serializer
from django.db.models import F, Count
from rest_framework import viewsets

from .models import ShowTheme, PlanetaryDome, ShowSession, AstronomyShow, Reservation
from .serializers import (
    ShowThemeSerializer,
    PlanetaryDomeSerializer,
    ShowSessionSerializer,
    AstronomyShowSerializer,
    ShowSessionListSerializer,
    AstronomyShowRetrieveSerializer,
    AstronomyShowListSerializer, ShowSessionRetrieveSerializer, ReservationSerializer
)


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetaryDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetaryDome.objects.all()
    serializer_class = PlanetaryDomeSerializer


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all().select_related()

    @staticmethod
    def _params_to_ints(query_string):
        return [int(str_id) for str_id in query_string.split(",")]


    def get_serializer_class(self):
        if self.action == "list":
            return ShowSessionListSerializer
        if self.action == "retrieve":
            return ShowSessionRetrieveSerializer

        return ShowSessionSerializer

    def get_queryset(self):
        queryset = self.queryset

        astronomy_shows = self.request.query_params.get("astronomy_shows")

        if astronomy_shows:
            astronomy_shows = self._params_to_ints(astronomy_shows)
            queryset = queryset.filter(astronomy_show__id__in=astronomy_shows)

        if self.action == "list":
            queryset = (
                queryset
                .select_related("planetary_dome")
                .annotate(seats_available=F("planetary_dome__rows") * F("planetary_dome__seats_in_row") - Count("tickets"))
            )
            return queryset
        if self.action == "retrieve":
            return queryset.select_related()

        return queryset


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()

    @staticmethod
    def _params_to_ints(query_string):
        return [int(str_id) for str_id in query_string.split(",")]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AstronomyShowRetrieveSerializer
        if self.action == "list":
            return AstronomyShowListSerializer

        return AstronomyShowSerializer

    def get_queryset(self):
        queryset = self.queryset

        show_themes = self.request.query_params.get("show_themes")

        if show_themes:
            show_themes = self._params_to_ints(show_themes)
            queryset = queryset.filter(show_themes__id__in=show_themes)

        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("show_themes")

        return queryset


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

