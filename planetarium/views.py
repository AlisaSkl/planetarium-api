from rest_framework import viewsets

from .models import ShowTheme, PlanetaryDome, ShowSession, AstronomyShow
from .serializers import ShowThemeSerializer, PlanetaryDomeSerializer, ShowSessionSerializer, AstronomyShowSerializer, \
    ShowSessionListSerializer


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

        return ShowSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.select_related()

        return queryset


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer

