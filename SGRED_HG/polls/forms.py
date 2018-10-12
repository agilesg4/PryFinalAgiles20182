from django import forms
from .models import Recurso, Artefacto


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ('titulo', 'tipo', 'descripcion', 'ubicacion', 'id_proyecto')


class ArtefactoForm(forms.ModelForm):
    class Meta:
        model = Artefacto
        ruta = forms.FileField()
        fields = ('nombre_mostrar', 'descripcion', 'archivo', 'reusable')
