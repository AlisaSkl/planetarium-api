from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    ShowThemeViewSet,
    PlanetaryDomeViewSet,
    ShowSessionViewSet,
    AstronomyShowViewSet,
    ReservationViewSet
)

router = routers.DefaultRouter()
router.register("show_themes", ShowThemeViewSet)
router.register("planetary_domes", PlanetaryDomeViewSet)
router.register("show_sessions", ShowSessionViewSet)
router.register("astronomy_shows", AstronomyShowViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "planetarium"
