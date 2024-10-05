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

    def get_serializer_class(self):
        if self.action == "list":
            return ShowSessionListSerializer
        if self.action == "retrieve":
            return ShowSessionRetrieveSerializer

        return ShowSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.select_related()

        return queryset


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AstronomyShowRetrieveSerializer
        if self.action == "list":
            return AstronomyShowListSerializer

        return AstronomyShowSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            return queryset.prefetch_related("show_themes")

        return queryset


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
