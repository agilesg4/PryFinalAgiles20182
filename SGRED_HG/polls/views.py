from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .forms import RecursoForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, request, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from .models import Recurso
from .serializers import RecursoSerializer
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

def index(request):
    return render(request, "polls/index.html")

# Recursos
def addRecurso(request):
    form = RecursoForm
    return render(request, 'polls/addRecurso.html', {'form': form})

def listRecurso(request):
    return render(request, 'polls/listRecurso.html')
