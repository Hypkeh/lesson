from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
from django.utils import timezone

from .models import Planet, Explorer
from .serializers import PlanetSerializer, ExplorerSerializer
# Create your views here.


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def recently_discovered_planets(self, request):
        delta = timezone.now() - timezone.timedelta(days=365*5)
        planets = Planet.objects.filter(discovered_by__expedition_date__gt=delta)
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)


class ExplorerViewSet(viewsets.ModelViewSet):
    queryset = Explorer.objects.all()
    serializer_class = ExplorerSerializer

    def get_permissions(self):
        if self.action in ['list', 'detail']:
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAuthenticated()]

    @action(detail=True, methods=['get'])
    def discovered_planets(self, request, pk):
        explorer = Explorer.objects.filter(pk=pk).prefetch_related('planet_set').first()
        planets = explorer.planet_set.all()
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)
