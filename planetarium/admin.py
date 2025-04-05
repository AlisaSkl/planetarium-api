from django.contrib import admin

from .models import (
    PlanetaryDome,
    ShowSession,
    Reservation,
    Ticket,
    ShowTheme,
    AstronomyShow
)

admin.site.register(PlanetaryDome)
admin.site.register(ShowSession)
admin.site.register(Reservation)
admin.site.register(Ticket)
admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
