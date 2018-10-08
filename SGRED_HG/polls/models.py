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


class Area_usuaria(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT,null=True)


class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True)
    apellido = models.CharField(max_length=150, blank=True)
    cargo = models.CharField(max_length=150, blank=True)
    celular = models.CharField(max_length=10, blank=True)
    email = forms.EmailField()
    id_area = models.ForeignKey(Area_usuaria, on_delete=models.PROTECT,null=True)

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
        fields = ('nombre')


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
        password=self.cleaned_data['password']
        password2=self.cleaned_data['password2']
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
    id_dueno_prod = models.ForeignKey(Dueno, on_delete=models.PROTECT,null=True)
    id_responsable = models.ForeignKey(User,on_delete=models.PROTECT,null=True)

    def __unicode__(self):
        return self.nombre


class Recurso(models.Model):
    id_recurso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, blank=False)
    tipo=models.CharField(max_length=150,blank=False)
    descripccion=models.CharField(max_length=1000,blank=False)
    ubicacion = models.CharField(max_length=1000,blank=True)
    #solicitante =
    fecha_creacion= models.DateField()
    id_usuario=models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    reusable = models.BooleanField(default=False)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT, null=True)


class Artefacto(models.Model):
    id_artefacto = models.AutoField(primary_key=True)
    nombre_mostrar = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=250, blank=False)
    archivo = models.FileField(upload_to='files', null=True)
    fecha_hora_carga = models.DateTimeField()
    cargado_por = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    fecha_hora_edicion = models.DateTimeField(null=True)
    reusable = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nombre_mostrar
