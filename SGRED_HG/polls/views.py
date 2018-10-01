from __future__ import unicode_literals
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Proyecto, Dueno, Departamento, Area_usuaria
from .models import Usuario
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request, HttpResponseBadRequest
from django.core.mail import send_mail
import json
from datetime import datetime
from django.core import serializers as jsonserializerp

from .forms import RecursoForm, ArtefactoForm, ProyectoForm
from .models import Artefacto

# Create your views here.

@csrf_exempt
def index(request):
    return render(request, "polls/index.html")


def agregar_Proyecto(request):
    return render(request, "polls/addProyecto.html")


@csrf_exempt
def add_Proyecto(request):
    if request.method == 'POST':
        new_proyecto = Proyecto(nombre=request.POST['nombre'],
                                  descripcion=request.POST['descripcion'],
                                  fecha_inicio=datetime.now(),
                                  fecha_fin=datetime.now(),
                                  dueno=request.POST['id_dueno'],
                                  responsable=request.POST['id_responsable']
                                  # ,
                                  # cargado_por=request.user
                                  )
        new_proyecto.save()
        return HttpResponse(serializers.serialize("json", [new_proyecto]))
    else:
        return HttpResponse(serializers.serialize("json", []))


def addRecurso(request):
    form = RecursoForm
    return render(request, 'polls/addRecurso.html', {'form': form})


def agregar_artefacto(request):
    return render(request, "polls/addArtefacto.html")


@csrf_exempt
def add_artefacto(request):
    if request.method == 'POST':
        if 'reusable' in request.POST:
            if request.POST.get('reusable') == 'on':
                bool_reusable = True
            else:
                bool_reusable = False
        else:
            bool_reusable = False

        new_artefacto = Artefacto(nombre_mostrar=request.POST['nombre_mostrar'],
                                  descripcion=request.POST['descripcion'],
                                  archivo=request.FILES['archivo'],
                                  reusable=bool_reusable,
                                  fecha_hora_carga=datetime.now()
                                  # ,
                                  # cargado_por=request.user
                                  )

        new_artefacto.save()
        return HttpResponse(serializers.serialize("json", [new_artefacto]))
    else:
        return HttpResponse(serializers.serialize("json", []))


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
