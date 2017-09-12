#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth,  messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from forms import LoginForm
from validators import Validator, FormLoginValidator
from django.db.models import Q
from icbf.settings import URL, GRUPO1, GRUPO2
from operarios.models import Operario
from beneficiarios.models import Beneficiario
import django.conf as conf
from datetime import datetime, timedelta
from parametrizacion.views import registrarLogs
from login.validators import existInGroup
import time

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
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, "login/login.html",{'error': validator.getMessage(), 'url': URL })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request, "login/login.html",{'url': URL })

################### FUNCION LOGOUT  #######################

@login_required(login_url="login:login")
def logout(request):
    registrarLogs(request.user.first_name+' '+request.user.last_name,'CIERRE DE SESSIÓN','Login','Sessión Terminada Exitosamente','')
    auth.logout(request)
    return HttpResponseRedirect("/")

################### TEMPLATE HOME ############################

@login_required(login_url="login:login")
def dashboard(request):
    if existInGroup(request.user.id,GRUPO2):
        o = Operario.objects.get(id=request.user.id)
        afro = Beneficiario.objects.filter(Q(grupo_etnico = 1) & Q(uds = o.uds)).count()
        indigena = Beneficiario.objects.filter(Q(grupo_etnico = 2) & Q(uds = o.uds)).count()
        gitano = Beneficiario.objects.filter(Q(grupo_etnico = 3) & Q(uds = o.uds)).count()
        raizal = Beneficiario.objects.filter(Q(grupo_etnico = 4) & Q(uds = o.uds)).count()
        palenquero = Beneficiario.objects.filter(Q(grupo_etnico = 5) & Q(uds = o.uds)).count()
        ninguno = Beneficiario.objects.filter(Q(grupo_etnico = 6) & Q(uds = o.uds)).count()
        beneficiarios = Beneficiario.objects.all().count()
        return render(request,'dashboard.html', {'afro':afro,'indigena':indigena,'gitano':gitano,'raizal':raizal,'palenquero':palenquero,'ninguno':ninguno,'beneficiarios':beneficiarios})
    else:
        return HttpResponseRedirect("/")
