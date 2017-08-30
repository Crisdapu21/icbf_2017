#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.db import transaction
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from icbf.settings import URL, SERVIDOR, GRUPO1, GRUPO2, STATIC_URL,AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID
from entidad_administradora_servicio.models import UDS
from parametrizacion.models import  Paises,Departamentos,Ciudades
from parametrizacion.views import registrarLogs
from operarios.models import Operario
from calendario.models import Eventos
import json, os, boto3, tinys3, time

################## TEMPLATE PERFIL ######################3

@login_required(login_url="login:login")
def perfil(request):
    url = URL
    operario = Operario.objects.get(id=request.user.id)
    return render(request,'perfil.html',{'url': url, 'operario': operario })

################## TEMPLATE CAMBIAR CONTRASEÑA ######################

@login_required(login_url="login:login")
def cambiar_pass(request):
    operario = Operario.objects.get(id=request.user.id)
    return render(request,'cambiar_password.html',{'operario': operario })

################## FUNCION ACTUALIZAR CONTRASEÑA ######################

@login_required(login_url="login:login")
def actualizar_password(request):
    if request.method == 'POST':
        id = request.user.id
        usu = User.objects.get(id = id)
        usu.password = make_password(request.POST['password'])
        usu.save()
        messages.success(request, 'Actualizado')
        registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Operarios','Contraseña Actualizada Exitosamente.',usu.first_name + " " + usu.last_name)
        return HttpResponseRedirect('/logout')
    else:
        return HttpResponseRedirect('/')

################## LISTADO OPERARIOS ######################

@login_required(login_url="login:login")
def operarios(request):
    if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
        operarios = Operario.objects.exclude(id=request.user.id)
        return render(request,'operarios/listado_operarios.html',{'operarios': operarios })
    else:
        return HttpResponseRedirect('/')

################## TEMPLATE CREAR OPERARIO ######################

@login_required(login_url="login:login")
def crearOperario(request):
    if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
        unidades_servicio = UDS.objects.all()
        return render(request,'operarios/nuevo_operario.html',{ 'unidades_servicio': unidades_servicio })
    else:
        return HttpResponseRedirect('/')

################## FUNCION GUARDAR OPERARIO ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarOperario(request):
    if request.method == 'POST':
        if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
            usu = User()
            usu.username = request.POST['nombres'] + time.strftime("%H:%M:%S")
            usu.first_name = request.POST['nombres']
            usu.last_name = request.POST['apellidos']
            usu.email = request.POST['email']
            usu.password = make_password("icbf2017")
            usu.is_active = True
            perfil = Group.objects.get(id = 2)
            usu.save()
            usu.groups.add(perfil)

            operario = Operario()
            operario.id_id = usu.id
            operario.uds_id = request.POST['uds']
            operario.genero = request.POST['genero']
            operario.intentos = 5
            operario.estado = "A"

            if request.POST['bandera_foto'] == "CAMBIO":
                operario.foto = request.FILES['archivo']
            else:
                operario.foto = "media/operarios/no_photo.png"

            operario.direccion = request.POST['direccion']
            operario.telefono =  request.POST['telefono']
            operario.celular =  request.POST['celular']
            operario.save()

            e = Eventos()
            e.uds = operario.uds
            e.detalle = "CREACIÓN DEL OPERARIO " + usu.first_name + " " + usu.last_name
            e.f_inicio  = '1997-02-21'
            e.f_fin  = '2017-02-21'
            e.tipo = "TAREAS"
            e.allday = True
            e.estado = "REALIZADA"
            e.save()

            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Operarios','Operario Creado Exitosamente.',usu.first_name + " " + usu.last_name)
            messages.success(request, 'Creado')
            return HttpResponseRedirect('/operarios')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect("/")


################## FUNCION ACTIVAR OPERARIO ######################

@csrf_exempt
@login_required(login_url="login:login")
def activarOperario(request):
    if request.method == 'PUT':
        if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
            operario = Operario.objects.get(id = request.GET['id'])
            operario.estado = "A"
            operario.intentos = 5
            operario.save()
            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Operarios','Intentos Reiniciados Exitosamente.', operario.id.first_name + " " + operario.id.last_name)
            return HttpResponse("Operario Activado", status=200)
        else:
            return HttpResponse("Permisos Incorrectos", status=200)
    else:
        return HttpResponse("Solicitud Incorrecta", status=200)


################## TEMPLATE EDITAR OPERARIO ######################

@login_required(login_url="login:login")
def editarOperario(request,id = None):
    if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
        operario = Operario.objects.get(id = id)
        unidades_servicio = UDS.objects.all()
        return render(request,'operarios/editar_operario.html',{'operario': operario ,'url': URL, 'unidades_servicio': unidades_servicio })
    else:
        return HttpResponseRedirect('/')


################## FUNCION VERIFICAR EMAIL ######################

@csrf_exempt
@login_required(login_url="login:login")
def verificarEmail(request):
    if request.method == 'PUT':
        email = request.GET['email'].replace(' ','').encode('ascii', 'ignore')
        if User.objects.filter(email=email).exists():
            return HttpResponse("El E-MAIL ya Existe", status=200)
        else:
            return HttpResponse("Campos Correctos", status=200)
    else:
        return HttpResponse("Solicitud Incorrecta", status=200)

################## FUNCION ACTUALIZAR OPERARIO ##############

@login_required(login_url="login:login")
def actualizarOperario(request):
    if request.method == 'POST':
        if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
            usu = User.objects.get(id = request.POST['operario_id'])
            usu.first_name = request.POST['nombres'].encode('ascii', 'ignore')
            usu.last_name = request.POST['apellidos'].encode('ascii', 'ignore')
            usu.email = request.POST['email']
            usu.save()

            operario = Operario.objects.get(id = request.POST['operario_id'])
            f_anterior = str(operario.foto)

            if request.POST['bandera_foto'] == "CAMBIO":
                operario.foto  = request.FILES['archivo']
                if  f_anterior != ("media/operarios/no_photo.png"):
                    try:
                        conn = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,tls=True)
                        conn.delete(f_anterior,AWS_STORAGE_BUCKET_NAME)
                    except OSError as e:
                        print(e)
                if int(request.POST['operario_id']) == request.user.id:
                    request.session["foto"] = URL +"media/operarios/" + str(request.POST['operario_id']) +"/"+str(operario.foto)
            else:
                operario.foto = f_anterior

            operario.genero = request.POST['genero']
            operario.direccion =  request.POST['direccion']
            operario.telefono =  request.POST['telefono']
            operario.celular =  request.POST['celular']

            if operario.id_id == request.user.id:
                messages.success(request, 'PerfilActualizado')
                redireccion = "/perfil"
            else:
                operario.uds_id = request.POST['uds']
                messages.success(request, 'Actualizado')
                redireccion = "/operarios"

            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Operarios','Operario Actualizado Exitosamente.',usu.first_name + " " + usu.last_name)
            operario.save()
            return HttpResponseRedirect(redireccion)
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


################## FUNCION ELIMINAR OPERARIO ######################

@csrf_exempt
@transaction.atomic
@login_required(login_url="login:login")
def eliminarOperario(request, id=None):
  if request.method == 'DELETE':
      if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
           usu = User.objects.get(id=id)
           operario = Operario.objects.get(id = id)
           try:
             conn = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_STORAGE_BUCKET_NAME,tls=True)
             lista = conn.list('media/operarios/'+str(id), AWS_STORAGE_BUCKET_NAME)
             for fichero in lista:
               conn.delete(fichero['key'])
             conn.delete('media/operarios/'+str(id))
           except OSError as e:
             print(e)
           operario.delete()
           registrarLogs(request.user.first_name+" "+request.user.last_name,'ELIMINAR','Operarios','Operario Eliminado Exitosamente.',usu.first_name + " " + usu.last_name)
           usu.delete()
           messages.success(request, 'Borrado')
           return HttpResponse(status=200)
      else:
          return HttpResponseRedirect("/")
  else:
      return HttpResponseRedirect("/")
