from django.db import models
from rest_framework import serializers
from .models import Recurso

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = "__all__"