#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.db import transaction
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from icbf.settings import URL, SERVIDOR, GRUPO1, GRUPO2, STATIC_URL,AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID
from entidad_administradora_servicio.models import Entidad_Administradora, UDS, Modalidades_servicio
from parametrizacion.models import  *
from login.validators import existInGroup
from parametrizacion.views import registrarLogs
from django.db.models import Q
import json, os, boto3, tinys3, time, math

########## TEMPLATE LISTADO ENTIDADES ADMINISTRADORAS DEL SERVICIO ###########

@login_required(login_url="login:login")
def entidades(request):
    if existInGroup(request.user.id,GRUPO1):
        entidades = Entidad_Administradora.objects.all()
        return render(request,'entidades/listado_entidades.html',{ 'entidades':entidades })
    else:
        return HttpResponseRedirect('/')

########## TEMPLATE ENTIDADES ADMINISTRADORAS DEL SERVICIO  ###########

@login_required(login_url="login:login")
def crearEntidad(request):
    tipos_documentos = Tipo_Documento.objects.filter(pk__in = [1,2])
    return render(request,'entidades/nueva_entidad.html',{ 'tipos_documentos':tipos_documentos })

############## FUNCION GUARDAR ENTIDADES ADMINISTRADORAS DEL SERVICIO #######################

@login_required(login_url="login:login")
def guardarEntidad(request):
    if request.method == 'POST':
        e = Entidad_Administradora()
        e.nombre = request.POST['nombre_entidad']
        e.tipo_documento_id = request.POST['tip_doc']
        e.numero_documento = request.POST['numero_documento']
        e.save()
        registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Entidad Administradora','Entidad Administradora Creada Exitosamente',e.nombre)
        messages.success(request, 'Creada')
        return HttpResponseRedirect('/entidades')
    else:
        return HttpResponseRedirect('/')

########## TEMPLATE EDITAR ENTIDADES ADMINISTRADORAS DEL SERVICIO ###########

@login_required(login_url="login:login")
def editarEntidad(request,id = None):
    entidad = Entidad_Administradora.objects.get(id=id)
    tipos_documentos = Tipo_Documento.objects.filter(pk__in = [1,2])
    return render(request,'entidades/editar_entidad.html',{ 'tipos_documentos':tipos_documentos, 'entidad':entidad })

############## FUNCION ACTUALIZAR ENTIDADES ADMINISTRADORAS DEL SERVICIO #######################

@login_required(login_url="login:login")
def actualizarEntidad(request):
    if request.method == 'POST':
        e = Entidad_Administradora.objects.get(id=request.POST['entidad_id'])
        e.nombre = request.POST['nombre_entidad']
        e.tipo_documento_id = request.POST['tip_doc']
        e.numero_documento = request.POST['numero_documento']
        e.save()
        registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Entidad Administradora','Entidad Administradora Actulizada Exitosamente',e.nombre)
        messages.success(request, 'Actualizada')
        return HttpResponseRedirect('/entidades')
    else:
        return HttpResponseRedirect('/')

############## FUNCION ELIMINAR ENTIDADES ADMINISTRADORAS DEL SERVICIO  #######################

@csrf_exempt
@transaction.atomic
@login_required(login_url="login:login")
def eliminarEntidad(request, id=None):
  if request.method == 'DELETE':
      e = Entidad_Administradora.objects.get(id=id)
      e.delete()
      messages.success(request, 'Borrada')
      return HttpResponse(status=200)
  else:
      return HttpResponseRedirect("/")

########## TEMPLATE LISTADO UDS ###########

@login_required(login_url="login:login")
def uds(request):
    if existInGroup(request.user.id,GRUPO1):
        uds = UDS.objects.all()
        return render(request,'entidades/listado_uds.html',{ 'uds':uds })
    else:
        return HttpResponseRedirect('/')

########## TEMPLATE UDS ###########

@login_required(login_url="login:login")
def crearUDS(request):
    entidades = Entidad_Administradora.objects.all()
    modalidades = Modalidades_servicio.objects.all()
    paises = Paises.objects.all()
    return render(request,'entidades/nueva_uds.html', {'entidades': entidades, 'modalidades':modalidades, 'paises':paises })

############## FUNCION GUARDAR UDS #######################

@login_required(login_url="login:login")
def guardarUDS(request):
    if request.method == 'POST':
        u = UDS()
        u.entidad_id = request.POST['entidad']
        u.nombre = request.POST['nombre_uds']
        u.modalidad_id = request.POST['modalidad']
        u.pais_id = request.POST['pais']
        u.departamento_id = request.POST['departamento']
        u.ciudad_id = request.POST['ciudad']
        u.direccion = request.POST['direccion']
        u.save()
        registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','UDS','Unidad del Servicio Creada Exitosamente',u.nombre)
        messages.success(request, 'Creada')
        return HttpResponseRedirect('/uds')
    else:
        return HttpResponseRedirect('/')

########## TEMPLATE EDITAR UDS ###########

@login_required(login_url="login:login")
def editarUDS(request,id = None):
    uds = UDS.objects.get(id=id)
    entidades = Entidad_Administradora.objects.all()
    modalidades = Modalidades_servicio.objects.all()
    paises = Paises.objects.all()
    return render(request,'entidades/editar_uds.html',{'entidades': entidades,'modalidades':modalidades,'paises':paises,'uds':uds })

############## FUNCION ACTUALIZAR UDS #######################

@login_required(login_url="login:login")
def actualizarUDS(request):
    if request.method == 'POST':
        u = UDS.objects.get(id=request.POST['id_uds'])
        u.entidad_id = request.POST['entidad']
        u.nombre = request.POST['nombre_uds']
        u.modalidad_id = request.POST['modalidad']
        u.pais_id = request.POST['pais']
        u.departamento_id = request.POST['departamento']
        u.ciudad_id = request.POST['ciudad']
        u.direccion = request.POST['direccion']
        u.save()
        registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','UDS','Unidad del Servicio Actualizada Exitosamente',u.nombre)
        messages.success(request, 'Actualizada')
        return HttpResponseRedirect('/uds')
    else:
        return HttpResponseRedirect('/')

############## FUNCION ELIMINAR UDS #######################

@csrf_exempt
@transaction.atomic
@login_required(login_url="login:login")
def eliminarUDS(request, id=None):
  if request.method == 'DELETE':
      u = UDS.objects.get(id=id)
      u.delete()
      messages.success(request, 'Borrada')
      return HttpResponse(status=200)
  else:
      return HttpResponseRedirect("/")
