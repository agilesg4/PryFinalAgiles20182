from django import forms
from .models import Recurso, Artefacto, Proyecto
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'id_proyecto','id_dueno_prod','id_responsable')


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ('titulo', 'tipo', 'descripccion', 'ubicacion', 'id_proyecto')


class ArtefactoForm(forms.ModelForm):
    class Meta:
        model = Artefacto
        ruta = forms.FileField()
        fields = ('nombre_mostrar', 'descripcion', 'ruta', 'reusable')
