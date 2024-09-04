from rest_framework import viewsets

from .models import ShowTheme
from .serializers import ShowThemeSerializer

class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
