#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth,  messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from .forms import LoginForm
from validators import Validator
from .validators import  FormLoginValidator
import time
from icbf.settings import URL, GRUPO1, GRUPO2
from operarios.models import Operario
import django.conf as conf
from datetime import datetime, timedelta
from parametrizacion.views import registrarLogs

################### FUNCION LOGIN  #######################

def login(request):
    if request.method == 'POST':
        validator = FormLoginValidator(request.POST)
        if validator.is_valid():
            email = request.POST['txtEmail']
            clave = request.POST['txtPassword']
            auth.login(request, validator.acceso)
            usuario = User.objects.get(email=email)
            request.session["fecha"]= time.strftime("%Y-%m-%d")
            f_max = datetime.now()
            f_min = timedelta(days=1825)
            request.session["fecha_min"] = (f_max - f_min).strftime("%Y-%m-%d")
            if User.objects.filter(pk=usuario.id, groups__name=GRUPO1).exists():
                 request.session["grupo"] = 1
                 request.session["nombregrupo"] = "ADMINISTRADOR"
            elif User.objects.filter(pk=usuario.id, groups__name=GRUPO2).exists():
                request.session["grupo"] = 2
                request.session["nombregrupo"] = "OPERARIO"

            operario = Operario.objects.get(pk= request.user.id)
            foto = str(operario.foto)
            request.session["foto"] = URL+foto
            return HttpResponseRedirect('/panel')
        else:
            return render(request, "login/login.html",{'error': validator.getMessage(), 'url': URL })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/panel')
        else:
            return render(request, "login/login.html",{'url': URL })

################### FUNCION LOGOUT  #######################

@login_required(login_url="login:login")
def logout(request):
    registrarLogs(request.user.first_name+' '+request.user.last_name,'CIERRE DE SESSIÓN','Login','Sessión Terminada Exitosamente.','')
    auth.logout(request)
    return HttpResponseRedirect("/")

################### TEMPLATE HOME ############################

@login_required(login_url="login:login")
def panel(request):
    return render(request,'panel.html')
