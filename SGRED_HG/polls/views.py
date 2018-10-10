from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, request, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from .models import Recurso, Artefacto, Dueno, User, Usuario, Proyecto
from .serializers import RecursoSerializer
from .forms import RecursoForm, ArtefactoForm, ProyectoForm
import json

#############################
# API
#############################

# Recursos
@csrf_exempt
def apiRecursoListByTipo(request):
    tipos = dict()
    for obj in Recurso.objects.all():
        tipos.setdefault(obj.tipo, []).append(RecursoSerializer(obj).data)
    return HttpResponse(json.dumps(tipos), content_type='application/json')

#############################
# Views
#############################

@csrf_exempt
def index(request):
    return render(request, "polls/index.html")

def dueno(request):
    lista_dueno = Dueno.objects.all()
    return HttpResponse(serializers.serialize("json", lista_dueno))

def responsable(request):
    lista_responsable = User.objects.all()
    return HttpResponse(serializers.serialize("json", lista_responsable))



def agregar_Proyecto(request):
    return render(request, "polls/addProyecto.html")


@csrf_exempt
def add_proyecto(request):
    if request.method == 'POST':
        new_proyecto = Proyecto(nombre=request.POST['nombre'],
                                descripcion=request.POST['descripcion'],
                                fecha_inicio=request.POST['fecha_inicio'],
                                fecha_fin=request.POST['fecha_fin'],
                                id_dueno_prod=Dueno.objects.get(nombre= request.POST['dueno']),
                                id_responsable=User.objects.get(username=request.POST['responsable']),
                               )
        new_proyecto.save()
        return HttpResponse(serializers.serialize("json", []))
    else:
        return HttpResponse(serializers.serialize("json", []))


def addRecurso(request):
    form = RecursoForm
    return render(request, 'polls/addRecurso.html', {'form': form})


def listRecurso(request):
    return render(request, 'polls/listRecurso.html')


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
