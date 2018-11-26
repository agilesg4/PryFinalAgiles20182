from django import forms
from .models import Recurso, Artefacto, Proyecto, Plan, Actividad, TipoAct, Fase, TPPlan, TPActividad
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('id_proyecto','nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'id_dueno_prod','id_responsable')


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('id_plan','nombre', 'descripcion')


class TPPlanForm(forms.ModelForm):
    class Meta:
        model = TPPlan
        fields = ('id_tpplan','nombre', 'descripcion')


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ('id_actividad','nombre', 'descripcion', 'tipoact','id_fase','fecha_inicio', 'fecha_fin','finalizado', 'periodicidad','id_plan')


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ('titulo', 'tipo', 'descripcion', 'ubicacion', 'id_proyecto')


class ArtefactoForm(forms.ModelForm):
    class Meta:
        model = Artefacto
        ruta = forms.FileField()
        fields = ('nombre_mostrar', 'descripcion', 'archivo', 'reusable')
