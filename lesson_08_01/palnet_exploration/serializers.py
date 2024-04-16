from rest_framework import serializers

from .models import Planet, Explorer


class PlanetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planet
        fields = '__all__'


class ExplorerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Explorer
        fields = '__all__'
