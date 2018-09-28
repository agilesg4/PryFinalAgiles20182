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


# Create your views here.

@csrf_exempt
def index(request):
    return render(request, "polls/index.html")

@csrf_exempt
def proy(request):
    return render(request, "polls/proyecto.html")


