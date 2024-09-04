from rest_framework import viewsets

from .models import ShowTheme, PlanetaryDome, ShowSession, AstronomyShow
from .serializers import ShowThemeSerializer, PlanetaryDomeSerializer, ShowSessionSerializer, AstronomyShowSerializer


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetaryDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetaryDome.objects.all()
    serializer_class = PlanetaryDomeSerializer


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer

