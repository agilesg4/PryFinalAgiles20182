from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, request, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from .models import Recurso, Artefacto, Dueno, User, Usuario, Proyecto
from .serializers import RecursoSerializer, TipoSerializer
import json
from datetime import datetime
from django.shortcuts import get_object_or_404
from .forms import RecursoForm, ArtefactoForm
from .models import Artefacto, Recurso, Proyecto, Tipo

#############################
# API
#############################

# Recursos
@csrf_exempt
def api_proyecto_recursos_por_tipo(request, proyecto_id):
    tipos = dict()
    for obj in Recurso.objects.filter(id_proyecto=proyecto_id):
        tipos.setdefault(obj.tipo.nombre, []).append(RecursoSerializer(obj).data)
    return HttpResponse(json.dumps(tipos), content_type='application/json')

@csrf_exempt
def api_recursos_por_tipo(request):
    tipos = dict()
    for obj in Recurso.objects.all():
        tipos.setdefault(obj.tipo.nombre, []).append(RecursoSerializer(obj).data)
    return HttpResponse(json.dumps(tipos), content_type='application/json')

@csrf_exempt
def api_update_recurso(request, recurso_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        titulo = data['titulo']
        tipo = get_object_or_404(Tipo, id_tipo=data['tipo'])
        descripcion = data['descripcion']
        ubicacion = data['ubicacion']
        recurso = Recurso.objects.filter(id_recurso=recurso_id)

        if recurso:
            recurso.update(titulo=titulo, tipo=tipo, descripcion=descripcion, ubicacion=ubicacion)
            return HttpResponse(status=200)
        else:
            return HttpResponse("Recursos no existe", status=404)
    else:
        return HttpResponse(serializers.serialize("json", []))

# Tipos de recursos
@csrf_exempt
def api_recursos_tipos(request):
    lista_tipos = Tipo.objects.all()
    serializer = TipoSerializer(lista_tipos, many=True)
    return HttpResponse(json.dumps(serializer.data), content_type='application/json')

#############################
# Views
#############################

@csrf_exempt
def index(request):
    return render(request, "polls/index.html")

def dueno(request):
    lista_dueno = Dueno.objects.all()
    return HttpResponse(serializers.serialize("json", lista_dueno))

def recurso(request):
    lista_recurso = Recurso.objects.all()
    return HttpResponse(serializers.serialize("json", lista_recurso))

def responsable(request):
    lista_responsable = User.objects.all()
    return HttpResponse(serializers.serialize("json", lista_responsable))

def agregar_Proyecto(request):
    return render(request, "polls/addProyecto.html")

def detalle_proyecto(request, proyecto_id):
    return render(request, "polls/detalleProyecto.html")


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
    return render(request, 'polls/recursos/addRecurso.html', {'form': form})

@csrf_exempt
def add_recurso_rest(request):
    if request.method == 'POST':
        proyecto = get_object_or_404(Proyecto, id_proyecto=request.POST['id_proyecto'])
        tipo = get_object_or_404(Tipo, id_tipo=request.POST['tipo'])
        new_recurso = Recurso(titulo=request.POST['titulo'],
                                  tipo=tipo,
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

def listResources(request):
    lista_recursos = Recurso.objects.all().values('id_recurso', 'titulo', 'tipo')
    context = {'recursos': lista_recursos}
    return render(request, 'polls/recursos/listRecurso.html', context)


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
                                  id_recurso = Recurso.objects.get(titulo=request.POST['recurso'])
                                  # cargado_por=User.objects.get(username=request.user),
                                  )

        new_artefacto.save()
        print(serializers.serialize("json", [new_artefacto]));
        return HttpResponse(serializers.serialize("json", [new_artefacto]))
    else:
        return HttpResponse(serializers.serialize("json", []))


def form_bitacora(request):
    return render(request, 'polls/addBitacora.html')

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
