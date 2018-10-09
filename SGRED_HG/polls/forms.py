from django import forms
from .models import Recurso, Artefacto


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ('titulo', 'tipo', 'descripccion', 'ubicacion', 'id_proyecto', 'artefacto')


class ArtefactoForm(forms.ModelForm):
    class Meta:
        model = Artefacto
        ruta = forms.FileField()
        fields = ('nombre_mostrar', 'descripcion', 'archivo', 'reusable')
