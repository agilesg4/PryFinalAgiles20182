from django.db import models
from rest_framework import serializers
from .models import Recurso, Tipo, Artefacto

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = "__all__"
        depth = 1

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = "__all__"

class ArtefactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artefacto
        fields = "__all__"
        depth = 1