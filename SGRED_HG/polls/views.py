from __future__ import unicode_literals
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Proyecto, Dueno, Departamento, Area_usuaria
from .models import Usuario
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request, HttpResponseBadRequest
from django.core.mail import send_mail
import json
from datetime import datetime
from django.core import serializers as jsonserializerp
from django.shortcuts import get_object_or_404

from .forms import RecursoForm, ArtefactoForm
from .models import Artefacto, Recurso, Proyecto

# Create your views here.

#Views
def index(request):
    return render(request, "polls/index.html")


def addRecurso(request):
    form = RecursoForm
    return render(request, 'polls/addRecurso.html', {'form': form})

@csrf_exempt
def add_recurso_rest(request):
    if request.method == 'POST':
        proyecto = get_object_or_404(Proyecto, id_proyecto=request.POST['id_proyecto'])
        new_recurso = Recurso(titulo=request.POST['titulo'],
                                  tipo=request.POST['tipo'],
                                  descripcion=request.POST['descripcion'],
                                  ubicacion=request.POST['ubicacion'],
                                  id_proyecto=proyecto,
                                  fecha_creacion=datetime.now()

                            )

        new_recurso.save()
        print(serializers.serialize("json", [new_recurso]));
        return HttpResponse(serializers.serialize("json", [new_recurso]))
    else:
        return HttpResponse(serializers.serialize("json", []))


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
                                  fecha_hora_carga=datetime.now(),
                                  # cargado_por=User.objects.get(username=request.user),
                                  )

        new_artefacto.save()
        print(serializers.serialize("json", [new_artefacto]));
        return HttpResponse(serializers.serialize("json", [new_artefacto]))
    else:
        return HttpResponse(serializers.serialize("json", []))


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
