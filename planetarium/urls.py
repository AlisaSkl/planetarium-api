from django.urls import path, include
from rest_framework import routers

from planetarium.views import ShowThemeViewSet, PlanetaryDomeViewSet

router = routers.DefaultRouter()
router.register("show_themes", ShowThemeViewSet)
router.register("planetary_domes", PlanetaryDomeViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "planetarium"
