from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, request, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from .serializers import RecursoSerializer, TipoSerializer
from .models import Recurso, Artefacto, Dueno, User, Usuario, Proyecto, Plan, TipoAct, Actividad, Fase, Tipo_artefacto, TPPlan, Bitacora, Tipo
import json
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Tipo, TPActividad
from .forms import RecursoForm, ArtefactoForm, PlanForm, ProyectoForm, ActividadForm,TPPlanForm
from datetime import datetime, timedelta



DEFAULT_HOME_PAGE = "polls/recursos/listRecurso.html"

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
    usuario = None
    if request.user.is_authenticated:
        usuario = Usuario.objects.filter(auth_user=request.user)
        tipos = dict()
        for obj in Recurso.objects.filter(id_usuario_id=usuario):
            tipos.setdefault(obj.tipo.nombre, []).append(RecursoSerializer(obj).data)
    else:
        tipos = dict()
        for obj in Recurso.objects.filter(id_usuario_id=None):
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
    return render(request, DEFAULT_HOME_PAGE)


@csrf_exempt
def listar_actividades(request):
    return render(request, "polls/listActividades.html")

def dueno(request):
    lista_dueno = Dueno.objects.all()
    return HttpResponse(serializers.serialize("json", lista_dueno))

def tipoact(request):
    lista_tipoact = TipoAct.objects.all()
    return HttpResponse(serializers.serialize("json", lista_tipoact))


def id_fase(request):
    lista_id_fase = Fase.objects.all()
    return HttpResponse(serializers.serialize("json", lista_id_fase))

def id_plan(request):
    lista_id_plan = Plan.objects.all()
    return HttpResponse(serializers.serialize("json", lista_id_plan))

def id_tpplan(request):
    lista_id_tpplan = TPPlan.objects.all()
    return HttpResponse(serializers.serialize("json", lista_id_tpplan))



def recurso(request):
    lista_recurso = Recurso.objects.all()
    return HttpResponse(serializers.serialize("json", lista_recurso))

def tipo_artefacto(request):
    lista_tipo_artefacto = Tipo_artefacto.objects.all()
    return HttpResponse(serializers.serialize("json", lista_tipo_artefacto))

def responsable(request):
    lista_responsable = Usuario.objects.all()
    return HttpResponse(serializers.serialize("json", lista_responsable))


def agregar_Proyecto(request):
    return render(request, "polls/addProyecto.html")


def detalle_proyecto(request, proyecto_id):
    return render(request, "polls/detalleProyecto.html")


def agregar_Plan(request):
    return render(request, "polls/addPlan.html")

def agregar_TPPlan(request):
    return render(request, "polls/templatePlan.html")


def agregar_Actividad(request):
    return render(request, "polls/addActividad.html")

def agregar_TPActividad(request):
    return render(request, "polls/templateActividad.html")



@csrf_exempt
def add_proyecto(request):
    if request.method == 'POST':
        new_proyecto = Proyecto(nombre=request.POST['nombre'],
                                descripcion=request.POST['descripcion'],
                                fecha_inicio=request.POST['fecha_inicio'],
                                fecha_fin=request.POST['fecha_fin'],
                                id_dueno_prod=Dueno.objects.get(nombre=request.POST['dueno']),
                                id_responsable=User.objects.get(username=request.POST['responsable']),
                               )
        new_proyecto.save()
        return HttpResponse(serializers.serialize("json", []))
    else:
        return HttpResponse(serializers.serialize("json", []))


@csrf_exempt
def add_plan(request):
    if request.method == 'POST':
        new_plan = Plan(nombre=request.POST['nombre'],
                        descripcion=request.POST['descripcion'],
                        id_recurso=Recurso.objects.get(titulo=request.POST.get('recurso')),
                        )
        new_plan.save()
        return HttpResponse(serializers.serialize("json", []))
    else:
        return HttpResponse(serializers.serialize("json", []))


@csrf_exempt
def add_tpplan(request):
    if request.method == 'POST':
        new_tpplan = TPPlan(nombre=request.POST['nombre'],
                            descripcion=request.POST['descripcion'],
                            )
        new_tpplan.save()
        return HttpResponse(serializers.serialize("json", []))
    else:
        return HttpResponse(serializers.serialize("json", []))





@csrf_exempt
def add_actividad(request):
    if request.method == 'POST':
        if 'finalizado' in request.POST:
            if request.POST.get('finalizado') == 'on':
                bool_finalizado = True
            else:
                bool_finalizado = False
        else:
            bool_finalizado = False
        #usuario = Usuario.objects.filter(auth_user=request.user).first()
        new_actividad = Actividad(nombre=request.POST['nombre'],
                                  descripcion=request.POST['descripcion'],
                                  tipoact=TipoAct.objects.get(nombre=request.POST['tipoact']),
                                  id_fase=Fase.objects.get(nombre=request.POST['id_fase']),
                                  fecha_inicio=request.POST['fecha_inicio'],
                                  fecha_fin=request.POST['fecha_fin'],
                                  finalizado=bool_finalizado,
                                  periodicidad=request.POST['periodicidad'],
                                  id_plan=Plan.objects.get(nombre=request.POST['id_plan']),
                                  id_responsable=Usuario.objects.get(name=request.POST['responsable']),
                                  #id_responsable=Usuario.objects.get(auth_user=request.user),
                                  )
        new_actividad.save()
        return HttpResponse(serializers.serialize("json", []))
    else:
        return HttpResponse(serializers.serialize("json", []))


@csrf_exempt
def add_tpactividad(request):
    if request.method == 'POST':
        if 'finalizado' in request.POST:
            if request.POST.get('finalizado') == 'on':
                bool_finalizado = True
            else:
                bool_finalizado = False
        else:
            bool_finalizado = False

        new_tpactividad = TPActividad(nombre=request.POST['nombre'],
                                  descripcion=request.POST['descripcion'],
                                  tipoact=TipoAct.objects.get(nombre=request.POST['tipoact']),
                                  id_fase=Fase.objects.get(nombre=request.POST['id_fase']),
                                  num_dias=request.POST['num_dias'],
                                  finalizado=bool_finalizado,
                                  id_tpplan=TPPlan.objects.get(nombre=request.POST['id_tpplan']),
                                  )
        new_tpactividad.save()
        return HttpResponse(serializers.serialize("json", []))
    else:
        return HttpResponse(serializers.serialize("json", []))





def addRecurso(request):
    form = RecursoForm
    return render(request, 'polls/recursos/addRecurso.html', {'form': form})


@csrf_exempt
def add_recurso_rest(request):
    usuario = None
    if request.user.is_authenticated:
        usuario = Usuario.objects.filter(auth_user=request.user).first()
    if request.method == 'POST':
        proyecto = get_object_or_404(Proyecto, id_proyecto=request.POST['id_proyecto'])
        tipo = get_object_or_404(Tipo, id_tipo=request.POST['tipo'])
        new_recurso = Recurso(titulo=request.POST['titulo'],
                                  tipo=tipo,
                                  descripcion=request.POST['descripcion'],
                                  ubicacion=request.POST['ubicacion'],
                                  id_proyecto=proyecto,
                                  fecha_creacion=datetime.now(),
                                  id_usuario=usuario,
                            )

        new_recurso.save()

        if request.POST['id_tpplan'] == 'Seleccionar Template Plan':
            {

            }
        else:
            new_plan = Plan(nombre="Plan de Trabajo de Recurso " + request.POST['titulo'],
                        descripcion="Plan de Trabajo de Recurso " + request.POST['titulo'],
                        id_recurso=new_recurso,
                        )
            new_plan.save()

            id_tpplan=TPPlan.objects.filter(nombre=request.POST['id_tpplan']).first()
            actividades=TPActividad.objects.filter(id_tpplan=id_tpplan)


            for actividad in actividades:

                new_actividad = Actividad(nombre=actividad.nombre + " Actividad de Recurso " + request.POST['titulo'],
                                  descripcion=actividad.descripcion + " Actividad de Recurso " + request.POST['titulo'],
                                  tipoact=actividad.tipoact,
                                  id_fase=actividad.id_fase,
                                  fecha_inicio=datetime.now(),
                                  fecha_fin=datetime.now()+timedelta(days=int(actividad.num_dias)),
                                  finalizado=actividad.finalizado,
                                  periodicidad='Dia',
                                  id_plan=new_plan,
                                  id_responsable=usuario,
                                  )
                new_actividad.save()

#        print(request.POST['id_tpplan'])
        return render(request, 'polls/recursos/listRecurso.html')
        #return HttpResponse(serializers.serialize("json", [new_recurso]))
    else:
        return render(request, 'polls/recursos/listRecurso.html')
        #return HttpResponse(serializers.serialize("json", []))


def agregar_artefacto(request):
    return render(request, "polls/addArtefacto.html")


def listResources(request):
    usuario = None
    if request.user is None:
        usuario = Usuario.objects.filter(auth_user=request.user)
    lista_recursos = Recurso.objects.filter(id_usuario_id=usuario)
    context = {'recursos': lista_recursos}
    return render(request, 'polls/recursos/listRecurso.html', context)


def listActividadesFuturas(request):
    usuario = None

    if request.user.is_authenticated:
        usuario = Usuario.objects.filter(auth_user=request.user)
    lista_Actividades_Futuras = Actividad.objects.filter(id_responsable=usuario)
    # lista_Actividades_Futuras = Actividad.objects.all()
    return HttpResponse(serializers.serialize("json", lista_Actividades_Futuras))


@csrf_exempt
def add_artefacto(request):
    usuario = None
    if request.user is None:
        usuario = Usuario.objects.filter(auth_user=request.user).first()

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
                                  tipo_artefacto=Tipo_artefacto.objects.get(nombre=request.POST.get('tipo_artefacto')),
                                  archivo=request.FILES['archivo'],
                                  reusable=bool_reusable,
                                  fecha_hora_carga=datetime.now(),
                                  fecha_hora_edicion=datetime.now(),
                                  id_recurso=Recurso.objects.get(titulo=request.POST.get('recurso')),
                                  cargado_por=User.objects.get(username=request.user),
                                  editado_por=User.objects.get(username=request.user),
                                  )

        new_artefacto.save()
        print(serializers.serialize("json", [new_artefacto]))
        return HttpResponse(serializers.serialize("json", [new_artefacto]))
    else:
        return HttpResponse(serializers.serialize("json", []))


def form_bitacora(request,actividad_id):
    return render(request, 'polls/addBitacora.html')

@csrf_exempt
def add_bitacora_rest(request):
    if request.method == 'POST':
        print (request)
        actividad = get_object_or_404(Actividad, pk=request.POST['actividad_id'])
        print(actividad)
        new_bitacora = Bitacora(
            fecha_bitacora=datetime.now(),
            descripcion=request.POST['descripcion'],
            archivo_bitacora=(request.FILES['archivo']),
            id_actividad_bitacora=actividad
                            )
        new_bitacora.save()
        print(serializers.serialize("json", [new_bitacora]))
        return render(request, 'polls/listActividades.html')
        #return HttpResponse(serializers.serialize("json", [new_bitacora]))
    else:
        return render(request, 'polls/listActividades.html')
        #return HttpResponse(serializers.serialize("json", []))

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def detalle_actividad(request, actividad_id):
    return render(request, "polls/detalle_actividad.html")

def rest_actividades_id(request,actividad_id):
    lista_Actividades_Futuras = Actividad.objects.filter(id_actividad=actividad_id);
    return HttpResponse(serializers.serialize("json", lista_Actividades_Futuras))



def login_view(request):

    if request.user.is_authenticated():
        # return redirect(reverse('media1:index'))
        return render(request, DEFAULT_HOME_PAGE)

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect(reverse('media1:index'))
            return render(request, DEFAULT_HOME_PAGE)
        else:
            mensaje = 'Credenciales de acceso incorrectas'

    return render(request, 'polls/login.html', {'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return render(request, DEFAULT_HOME_PAGE)


def create_TPPlan(nombre_plan):
    new_plan = Plan(nombre="Plan de Trabajo de Recurso " + nombre_plan ,
                    descripcion="Plan de Trabajo de Recurso " + nombre_plan ,
                    id_recurso=Recurso.objects.filter(nombre=nombre_plan).order_by('-id_recurso')[0],
                    )
    new_plan.save()
    return render(request, 'polls/recursos/listRecurso.html')
