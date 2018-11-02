# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from rest_framework import serializers


# Create your models here.

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.nombre

class Tipo_artefacto(models.Model):
    id_tipo_artefacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.nombre

class Area_Usuaria(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True)

    def __unicode__(self):
        return self.nombre

class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    apellido = models.CharField(max_length=150, blank=True)
    cargo = models.CharField(max_length=150, blank=True)
    celular = models.CharField(max_length=10, blank=True)
    email = forms.EmailField()
    id_area = models.ForeignKey(Area_Usuaria, on_delete=models.PROTECT, null=True)

    def clean_email(self):
        """Comprueba que no exista un email igual en la Base de Datos"""
        email = self.cleaned_data['email']
        if Dueno.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registado.')
        return email

    def __unicode__(self):
        return self.nombre


class DuenoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dueno
        fields = 'nombre'


class Usuario(models.Model):
    picture = models.ImageField(upload_to="images", blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    auth_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __unicode__(self):
        return self.auth_user.username


class UserForm(ModelForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ('picture', 'country', 'city')

    def clean_username(self):
        """Comprueba que no exista un username igual en la Base de Datos"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_email(self):
        """Comprueba que no exista un email igual en la Base de Datos"""
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual registado.')
        return email

    def clean_password2(self):
        """Comprueba que password y password2 segan iguales"""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las Claves no coinciden.')
        return password2


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'foto', 'pais', 'ciudad', 'email', 'username')


class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=1000, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_dueno_prod = models.ForeignKey(Dueno, on_delete=models.PROTECT, null=True)
    id_responsable = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __unicode__(self):
        return self.nombre


# Tipo del recurso
class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=False)
    icono = models.CharField(max_length=1000, blank=False)

    def __unicode__(self):
        return self.nombre


class Recurso(models.Model):
    id_recurso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=False)
    tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT, null=True)
    descripcion=models.CharField(max_length=1000,blank=False)
    ubicacion = models.CharField(max_length=1000,blank=True)
    fecha_creacion= models.DateField()
    id_usuario=models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    reusable = models.BooleanField(default=False)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT, null=True)

    def __unicode__(self):
        return self.titulo

class Artefacto(models.Model):
    id_artefacto = models.AutoField(primary_key=True)
    nombre_mostrar = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=250, blank=False)
    tipo_artefacto = models.ForeignKey(Tipo_artefacto, on_delete=models.PROTECT, null=False)
    archivo = models.FileField(upload_to='files', null=False, blank=False)
    fecha_hora_carga = models.DateTimeField(null=False)
    cargado_por = models.ForeignKey(User, on_delete=models.PROTECT, null=False, related_name='cargado_por')
    fecha_hora_edicion = models.DateTimeField(null=False)
    editado_por = models.ForeignKey(User, on_delete=models.PROTECT, null=False, related_name='editado_por')
    reusable = models.BooleanField(default=False)
    id_recurso = models.ForeignKey(Recurso, on_delete=models.PROTECT, null=True)

    def __unicode__(self):
        return self.nombre_mostrar


class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.nombre


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = 'nombre'


class Fase(models.Model):
    id_fase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.nombre


class FaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fase
        fields = 'nombre'



class TipoAct(models.Model):
    id_tipoact = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return self.nombre


class TipoActSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoAct
        fields = 'nombre'




class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    descripcion = models.CharField(max_length=1000, blank=True)
    tipoact = models.ForeignKey(TipoAct, on_delete=models.PROTECT, null=True)
    id_fase = models.ForeignKey(Fase, on_delete=models.PROTECT, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    finalizado = models.BooleanField(default=False)
    periodicidad = models.CharField(max_length=150, blank=True)
    id_plan = models.ForeignKey(Plan, on_delete=models.PROTECT, null=True)
    id_responsable = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __unicode__(self):
        return self.nombre


class ResponsableAct(models.Model):
    id_actividad = models.ForeignKey(Actividad, on_delete=models.PROTECT, null=True)
    id_responsable = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __unicode__(self):
        return self.id_actividad


class Bitacora(models.Model):
    id_bitacora = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=1000,blank=True)
    archivo = models.FileField(upload_to='files', null=True)
    fecha = models.DateTimeField(null=True)
    id_actividad = models.ForeignKey(Actividad, on_delete=models.PROTECT, null=True)




