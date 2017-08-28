#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.db import transaction
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from operarios.models import Operario
from calendario.models import *
from django.db.models import Q
from icbf.settings import URL,GRUPO2
from datetime import datetime, timedelta
from login.validators import existInGroup
from django.core import serializers
import json, time

################### FUNCION GUARDAR NOTIFICACIONESs ############################

def guardarNotificacion(evento,uds,tipo,f_inicio,f_fin,beneficiario,nombre,detalle):
    n = Notificaciones()
    n.uds_id = int(uds)
    n.tipo = tipo
    n.f_inicio = f_inicio
    n.f_fin = f_fin
    if beneficiario != "":
        n.beneficiario_id = int(beneficiario)
    n.nombre = nombre
    n.detalle = detalle
    n.limite = "A_TIEMPO"
    n.save()

    e = Eventos.objects.get(id=evento)
    e.notificacion = n.id
    e.save()

################### FUNCION OBTENER NOTIFICACIONES #######################

@csrf_exempt
@transaction.atomic
def getNotifications(request):
    operario = Operario.objects.get(id=request.user.id)
    notifications = serializers.serialize('json',Notificaciones.objects.filter(Q(uds = operario.uds) & Q(f_fin = time.strftime('%Y-%m-%d'))).exclude(limite="SUPERADO"))
    notificacion_data = json.loads(notifications)
    json_notificacion_data = json.dumps(notificacion_data)
    return HttpResponse(json_notificacion_data, content_type='json')

################### TEMPLATE CALENDARIO #######################

@login_required(login_url="login:login")
def calendario(request):
    if existInGroup(request.user.id,GRUPO2):
        operario = Operario.objects.get(id=request.user.id)
        eventos = Eventos.objects.filter(uds=operario.uds)
        beneficiarios = Beneficiario.objects.filter(uds=operario.uds)
        notificaciones = Notificaciones.objects.filter(uds=operario.uds)
        return render(request,'calendario/calendario.html',{'operario':operario,'eventos':eventos,'beneficiarios': beneficiarios,'notificaciones': notificaciones })
    else:
        return HttpResponseRedirect('/')

################### TEMPLATE EDITAR EVENTO #######################

@login_required(login_url="login:login")
def editarEvento(request,id = None):
    evento = Eventos.objects.get(id = id)
    beneficiarios = Beneficiario.objects.all()
    if evento.tipo == "PENDIENTES":
        beneficiario = Beneficiario.objects.get(id = evento.beneficiario.id)
        notas = Notas.objects.filter(Q(uds=evento.uds.id) and Q(beneficiario = beneficiario.id))
    else:
        notas = ""
    operario = Operario.objects.get(id= request.user.id)
    return render(request,'calendario/editar_evento.html',{'evento':evento,'notas': notas ,'operario': operario,'beneficiarios': beneficiarios, 'url': URL })

################### FUNCION GUARDAR EVENTO TAREAS #######################

@login_required(login_url="login:login")
def guardarTareas(request):
    if request.method == 'POST':
        o = Operario.objects.get(id=request.user.id)
        e = Eventos()
        e.uds_id = o.uds.id
        e.detalle = request.POST['tareas_detalle']
        e.f_inicio = request.POST['tareas_inicia']
        e.f_fin = request.POST['tareas_inicia']
        e.bandera = request.POST['tareas_inicia']
        e.tipo = "TAREAS"
        e.estado = "NO REALIZADA"
        e.allday = "True"
        e.save()
        messages.success(request, 'Creado')
        return HttpResponseRedirect('/calendario')
    else:
        return HttpResponseRedirect('/calendario')

################### FUNCION ACTUALIZAR EVENTO TAREAS #######################

@csrf_exempt
@login_required(login_url="login:login")
def actualizarTareas(request):
    if request.method == 'POST':
        e = Eventos.objects.get(id = request.POST['tareas_id'])
        e.detalle = request.POST['tareas_detalle']
        e.f_inicio = request.POST['tareas_inicia']
        e.f_fin = request.POST['tareas_inicia']
        e.bandera = request.POST['tareas_inicia']
        e.estado = request.POST['tareas_estado']
        e.save()
        messages.success(request, 'Actualizado')
        return HttpResponseRedirect('/calendario/editar/'+request.POST['tareas_id'])
    else:
        return HttpResponseRedirect('/calendario')


################### FUNCION GUARDAR EVENTO PENDIENTES #######################

@login_required(login_url="login:login")
def guardarPendientes(request):
    if request.method == 'POST':
        o = Operario.objects.get(id=request.user.id)
        e = Eventos()
        e.beneficiario_id = request.POST['pendientes_beneficiario']
        e.uds_id = o.uds.id
        e.detalle = request.POST['pendientes_detalle']
        e.f_inicio = request.POST['pendientes_inicia']
        e.f_fin = request.POST['pendientes_finaliza']
        e.tipo = "PENDIENTES"
        e.estado = "NO REALIZADA"
        e.allday = "True"
        e.save()
        n = Notas()
        nota = request.POST['pendientes_detalle']
        n.nota = nota.encode('ascii', 'ignore')
        n.uds = o.uds.id
        n.beneficiario_id = request.POST['pendientes_beneficiario']
        n.save()
        e.nota_id_id = n.id
        e.save()
        messages.success(request, 'Creado')
        return HttpResponseRedirect('/calendario')
    else:
        return HttpResponseRedirect('/calendario')

################### FUNCION ACTUALIZAR EVENTO PENDIENTES #######################

@csrf_exempt
@login_required(login_url="login:login")
def actualizarPendientes(request):
    if request.method == 'POST':
        o = Operario.objects.get(id=request.user.id)
        e = Eventos.objects.get(id = request.POST['pendientes_id'])
        e.detalle = request.POST['pendientes_detalle']
        e.f_inicio = request.POST['pendientes_inicia']
        e.f_fin = request.POST['pendientes_finaliza']
        e.estado = request.POST['pendientes_estado']
        e.save()
        messages.success(request, 'Actualizado')
        return HttpResponseRedirect('/calendario/editar/'+request.POST['pendientes_id'])
    else:
        return HttpResponseRedirect('/calendario')


################### FUNCION ELIMINAR  EVENTO  #######################

@csrf_exempt
def eliminarEvento(request, id=None):
  evento = Eventos.objects.get(id=id)
  try:
      n = Notificaciones.objects.get(id = evento.notificacion)
      n.delete()
  except ObjectDoesNotExist:
      print("La Notificación no Existe");
  evento.delete()
  messages.success(request, 'Borrado')
  return HttpResponseRedirect('/calendario')
