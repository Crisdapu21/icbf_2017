#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.template import RequestContext
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from parametrizacion.models import *
import json


################### LOCALIZACION #######################

from django.core import serializers
@login_required(login_url="/login")
def ajaxDepartamentos(request):
    departamento =  Departamentos.objects.filter(pais_id = request.GET['pais'])
    data = serializers.serialize('json', departamento, fields=('id','departamento'))
    return HttpResponse( data , content_type ='application/json' )

@login_required(login_url="/login")
def ajaxProvincias(request):
    provincia =  Provincias.objects.filter(departamento_id = request.GET['departamento'])
    data = serializers.serialize('json', provincia, fields=('id','provincia'))
    return HttpResponse( data , content_type ='application/json' )

@login_required(login_url="/login")
def ajaxDistritos(request):
    distrito = Distritos.objects.filter(provincia_id = request.GET['provincia'])
    data = serializers.serialize('json', distrito, fields=('id','distrito'))
    return HttpResponse( data , content_type ='application/json' )

@login_required(login_url="/login")
def ajaxCiudades(request):
    ciudad =  Ciudades.objects.filter(distrito_id = request.GET['distrito'])
    data = serializers.serialize('json', ciudad, fields=('id','ciudad'))
    return HttpResponse( data , content_type ='application/json' )
