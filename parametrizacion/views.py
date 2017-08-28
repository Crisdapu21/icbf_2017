#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from parametrizacion.models import *
from icbf.settings import URL, SERVIDOR, GRUPO1, GRUPO2, STATIC_URL,AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID
from django.core import serializers
import json

################### LOCALIZACION #######################

@login_required(login_url="/login")
def ajaxDepartamentos(request):
    departamento =  Departamentos.objects.filter(pais_id = request.GET['pais'])
    data = serializers.serialize('json', departamento, fields=('id','departamento'))
    return HttpResponse( data , content_type ='application/json' )

@login_required(login_url="/login")
def ajaxCiudades(request):
    ciudad =  Ciudades.objects.filter(departamento_id = request.GET['departamento'])
    data = serializers.serialize('json', ciudad, fields=('id','ciudad'))
    return HttpResponse( data , content_type ='application/json' )


################### FUNCION GUARDAR LOGS #######################

def registrarLogs(operario,accion,modelo,detalle,referencia):
    l = Logs()
    l.usuario = operario
    l.accion = accion
    l.modelo = modelo
    l.detalle = detalle
    l.referencia = referencia
    l.save()

################## TEMPLATE LISTADO DE LOGS ######################3

@login_required(login_url="login:login")
def listadoLogs(request):
    if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
        logs = Logs.objects.all().order_by('fecha')[::-1]
        return render(request,'listado_logs.html',{'logs': logs })
    else:
        return HttpResponseRedirect('/')
