#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
import xhtml2pdf.pisa as pisa
from StringIO import StringIO
from django.template.loader import render_to_string
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.db import transaction
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from icbf.settings import URL, SERVIDOR, GRUPO1, GRUPO2, STATIC_URL,AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID
from parametrizacion.views import registrarLogs
from parametrizacion.models import  Paises,Departamentos,Ciudades
from nutricion.models import *
from beneficiarios.models import Beneficiario
from django.db.models import Q
import json,os,math

################## FUNCION GUARDAR O ACTUALIZAR NUTRICION ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarNutricion(request):
    if request.method == 'POST':
        if request.POST['e_estado'] == "INCOMPLETO":
            e = Nutricion()
            e.beneficiario_id = request.POST['e_ben']
            e.peso_nacer = request.POST['e_peso']
            e.talla_nacer = request.POST['e_talla']
            #E3. ¿El niño o niña cuenta con el carnet actualizado de crecimiento y desarrollo
            e.e3 =  request.POST['e3']
            #E4 Si el niño o niña cuenta con el carnet de crecimiento y desarrollo verifique, cuantos controles de crecimiento y desarrollo ha recibido en los últimos 6 meses
            e.e4 =  request.POST['controles_tomados']
            e.e4_f1 = request.POST['ninos_fecha_1']
            e.e4_f2 = request.POST['ninos_fecha_2']
            e.e4_f3 = request.POST['ninos_fecha_3']
            #E5. Si el niño o niña es menor de seis meses ¿Está siendo alimentado con leche materna de forma exclusiva?
            e.e5 = request.POST['e5']
            #E6. Si la respuesta anterior es NO, ¿qué tipo de alimentación recibe el niño o niña menor de seis meses?
            e.e6 = request.POST['e6']
            e.e6_otra =  request.POST['e6_otra']
            #E7. Si el niño o niña es mayor de 6 meses y menor de 2 años, está siendo alimentado con
            e.e7 = request.POST['e7']
            e.e7_otra = request.POST['e7_otra']
            #E8. Si el niño o niña presenta diagnóstico de desnutrición u obesidad, le han realizado los siguientes exámenes
            e.t1_d8 = request.POST['t1_d8']
            e.id_t1_d8 = request.POST['id_t1_d8']
            e.e1_d8 = request.POST['e1_d8']
            e.id_e1_d8 = request.POST['id_e1_d8']
            e.a1_d8 = request.POST['a1_d8']
            e.id_a1_d8 = request.POST['id_a1_d8']
            e.t2_d8 = request.POST['t2_d8']
            e.id_t2_d8 = request.POST['id_t2_d8']
            e.e2_d8 = request.POST['e2_d8']
            e.id_e2_d8 = request.POST['id_e2_d8']
            e.a2_d8 = request.POST['a2_d8']
            e.id_a2_d8 = request.POST['id_a2_d8']
            e.t3_d8 = request.POST['t3_d8']
            e.id_t3_d8 = request.POST['id_t3_d8']
            e.e3_d8 = request.POST['e3_d8']
            e.id_e3_d8 = request.POST['id_e3_d8']
            e.a3_d8 = request.POST['a3_d8']
            e.id_a3_d8 = request.POST['id_a3_d8']
            e.t4_d8 = request.POST['t4_d8']
            e.id_t4_d8 = request.POST['id_t4_d8']
            e.e4_d8 = request.POST['e4_d8']
            e.id_e4_d8 = request.POST['id_e4_d8']
            e.a4_d8 = request.POST['a4_d8']
            e.id_a4_d8 = request.POST['id_a4_d8']
            #E9. El niño o niña mayor de dos años ¿ha recibido en el último año antiparasitarios, por parte de algún servicio de salud?
            e.e9 = request.POST['e9']
            #E10. En caso de haber recibido antiparasitarios, indique la última fecha en la que fue tomada por el niño o niña
            e.e10 = request.POST['e10']
            #E11. El niño o niña tiene alguna dieta especial o restricción alimentaria o alergia alimentaria
            e.e11 =  request.POST['e11']
            e.e11_cual = request.POST['e11_cual']
            e.save()

            e = Beneficiario.objects.get(id=request.POST['e_ben'])
            e.modulo_e = "COMPLETADO"
            e.save()
            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Nutrición','Nutrición Creada Exitosamente',e.primer_nombre+" "+e.segundo_nombre+" "+e.primer_apellido+" "+e.segundo_apellido)
        else:
            n = Nutricion.objects.get(beneficiario=request.POST['e_ben'])
            n.peso_nacer = request.POST['e_peso']
            n.talla_nacer = request.POST['e_talla']
            #E3. ¿El niño o niña cuenta con el carnet actualizado de crecimiento y desarrollo
            n.e3 =  request.POST['e3']
            #E4 Si el niño o niña cuenta con el carnet de crecimiento y desarrollo verifique, cuantos controles de crecimiento y desarrollo ha recibido en los últimos 6 meses
            n.e4 =  request.POST['controles_tomados']
            n.e4_f1 = request.POST['ninos_fecha_1']
            n.e4_f2 = request.POST['ninos_fecha_2']
            n.e4_f3 = request.POST['ninos_fecha_3']
            #E5. Si el niño o niña es menor de seis meses ¿Está siendo alimentado con leche materna de forma exclusiva?
            n.e5 = request.POST['e5']
            #E6. Si la respuesta anterior es NO, ¿qué tipo de alimentación recibe el niño o niña menor de seis meses?
            n.e6 = request.POST['e6']
            n.e6_otra =  request.POST['e6_otra']
            #E7. Si el niño o niña es mayor de 6 meses y menor de 2 años, está siendo alimentado con
            n.e7 = request.POST['e7']
            n.e7_otra = request.POST['e7_otra']
            #E8. Si el niño o niña presenta diagnóstico de desnutrición u obesidad, le han realizado los siguientes exámenes
            n.t1_d8 = request.POST['t1_d8']
            n.id_t1_d8 = request.POST['id_t1_d8']
            n.e1_d8 = request.POST['e1_d8']
            n.id_e1_d8 = request.POST['id_e1_d8']
            n.a1_d8 = request.POST['a1_d8']
            n.id_a1_d8 = request.POST['id_a1_d8']
            n.t2_d8 = request.POST['t2_d8']
            n.id_t2_d8 = request.POST['id_t2_d8']
            n.e2_d8 = request.POST['e2_d8']
            n.id_e2_d8 = request.POST['id_e2_d8']
            n.a2_d8 = request.POST['a2_d8']
            n.id_a2_d8 = request.POST['id_a2_d8']
            n.t3_d8 = request.POST['t3_d8']
            n.id_t3_d8 = request.POST['id_t3_d8']
            n.e3_d8 = request.POST['e3_d8']
            n.id_e3_d8 = request.POST['id_e3_d8']
            n.a3_d8 = request.POST['a3_d8']
            n.id_a3_d8 = request.POST['id_a3_d8']
            n.t4_d8 = request.POST['t4_d8']
            n.id_t4_d8 = request.POST['id_t4_d8']
            n.e4_d8 = request.POST['e4_d8']
            n.id_e4_d8 = request.POST['id_e4_d8']
            n.a4_d8 = request.POST['a4_d8']
            n.id_a4_d8 = request.POST['id_a4_d8']
            #E9. El niño o niña mayor de dos años ¿ha recibido en el último año antiparasitarios, por parte de algún servicio de salud?
            n.e9 = request.POST['e9']
            #E10. En caso de haber recibido antiparasitarios, indique la última fecha en la que fue tomada por el niño o niña
            n.e10 = request.POST['e10']
            #E11. El niño o niña tiene alguna dieta especial o restricción alimentaria o alergia alimentaria
            n.e11 =  request.POST['e11']
            n.e11_cual = request.POST['e11_cual']
            n.save()

            e = Beneficiario.objects.get(id=request.POST['e_ben'])
            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Nutrición','Nutrición Actualizada Exitosamente',e.primer_nombre+" "+e.segundo_nombre+" "+e.primer_apellido+" "+e.segundo_apellido)
        messages.success(request, 'Nutricion')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")

################## TEMPLATE AGREGAR MEDIDAS ANTROPOMETRICAS ######################

@login_required(login_url="login:login")
def medidasAntropometricas(request, id=None):
    beneficiario = Beneficiario.objects.get(id = id)
    controles = Controles.objects.filter(beneficiario=id).order_by("total_meses")

    edades = []
    lista_pesos = []
    p_sobrepeso = []
    p_obeso = []
    p_ideal = []
    p_beneficiario = []
    p_bajo = []
    p_severo = []
    labels = []

    for e in controles:
        edad = e.edad_anios*12 + e.edad_meses
        peso_sobrepeso = e.peso_SobrepesoK+"."+e.peso_SobrepesoG
        peso_obeso = e.peso_ObesoK+"."+e.peso_ObesoG
        peso_ideal = e.peso_idealK+"."+e.peso_idealG
        peso_beneficiario = e.peso_kilos+"."+e.peso_gramos
        peso_bajo = e.peso_BajoPesoK+"."+e.peso_BajoPesoG
        peso_severo = e.peso_BajoPesoSeveroK+"."+e.peso_BajoPesoSeveroG
        edades.append(int(edad))
        p_sobrepeso.append(float(peso_sobrepeso))
        p_obeso.append(float(peso_obeso))
        p_ideal.append(float(peso_ideal))
        p_beneficiario.append(float(peso_beneficiario))
        p_bajo.append(float(peso_bajo))
        p_severo.append(float(peso_severo))

    if len(p_beneficiario)>0:
        peso_sobrepeso = int(math.ceil(max(p_sobrepeso)))
        peso_obeso = int(math.ceil(max(p_obeso)))
        peso_ideal = int(math.ceil(max(p_ideal)))
        peso_beneficiario = int(math.ceil(max(p_beneficiario)))
        peso_bajo = int(math.ceil(max(p_bajo)))
        peso_severo = int(math.ceil(max(p_severo)))
        lista_pesos.append(peso_sobrepeso)
        lista_pesos.append(peso_obeso)
        lista_pesos.append(peso_ideal)
        lista_pesos.append(peso_beneficiario)
        lista_pesos.append(peso_bajo)
        lista_pesos.append(peso_severo)
        peso = max(lista_pesos)
    else:
        peso = 0

    for a in edades:
        if a == 0 or a == 1 or a == 12 or a == 24 or a == 36 or a == 48 or a == 60:
            if a == 0:
                labels.append('Recien Nacido')
            if a == 1:
                labels.append(str(a)+' Mes')
            if a == 12:
                labels.append('1 Año')
            if a == 24:
                labels.append('2 Años')
            if a == 36:
                labels.append('3 Años')
            if a == 48:
                labels.append('4 Años')
            if a == 60:
                labels.append('5 Años')
        else:
            labels.append(str(a)+' Meses')

    label = ','.join(labels)
    return render(request,'nutricion/agregar_medidas.html',{'controles':controles,'beneficiario':beneficiario,'label':label,'peso':peso })

################## FUNCION GUARDAR MEDIDAS ANTROPOMETRICAS ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarMedidasAntropometricas(request):
    if request.method == 'POST':
        a = Controles.objects.filter(beneficiario=request.POST['e_ben']).filter(edad_meses=request.POST['nutricion_edad_meses']).filter(edad_anios=request.POST['nutricion_edad_anios']).count()
        if a >=1:
            messages.success(request, 'Ya Existe')
        else:
            if int(request.POST['nutricion_edad_anios']) >=5:
                if int(request.POST['nutricion_edad_meses']) >=1:
                    messages.success(request, 'Limite de Edad')
            else:
                if int(request.POST['nutricion_edad_meses']) <=11:
                    c = Controles()
                    c.beneficiario_id = request.POST['e_ben']
                    c.numero_orden = request.POST['nutricion_numero_orden']
                    c.fecha_control = request.POST['nutricion_fecha_control']
                    c.edad_anios = request.POST['nutricion_edad_anios']
                    c.edad_meses = request.POST['nutricion_edad_meses']
                    c.total_meses = int(c.edad_anios)*12+int(c.edad_meses)
                    c.peso_kilos = int(request.POST['nutricion_peso_kilos'])
                    c.peso_gramos = request.POST['nutricion_peso_gramos']
                    c.talla = request.POST['nutricion_talla']
                    c.interpretacion = request.POST['nutricion_interpretacion']
                    c.save()
                    e = Beneficiario.objects.get(id=request.POST['e_ben'])
                    registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Nutrición','Medidas Antropometricas Creadas Exitosamente',e.primer_nombre+" "+e.segundo_nombre+" "+e.primer_apellido+" "+e.segundo_apellido)
                    peso_talla_Ideal(c.id,e.genero,c.edad_anios,c.edad_meses,c.peso_kilos,c.peso_gramos,c.talla)
                    messages.success(request, 'Guardado')
                else:
                    messages.success(request, 'Meses Incorrectos')
        return HttpResponseRedirect('/beneficiarios/medidas_antropometricas/'+request.POST['e_ben'])
    else:
        return HttpResponseRedirect("/")

def peso_talla_Ideal(id,genero,edad_anios,edad_meses,pesoK,pesoG,talla):
    edad_anios = int(edad_anios)
    edad_meses = int(edad_meses)

    if genero == "M":
        if edad_anios < 1:
            if edad_meses == 0:
                p_SobrepesoK = "4"
                p_SobrepesoG = "800"
                p_ObesoK = "3"
                p_ObesoG = "800"
                p_IdealK = "3"
                p_IdealG = "400"
                p_BajoPesoK = "2"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "2"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 1:
                p_SobrepesoK = "5"
                p_SobrepesoG = "800"
                p_ObesoK = "5"
                p_ObesoG = "100"
                p_IdealK = "4"
                p_IdealG = "500"
                p_BajoPesoK = "4"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "3"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 2:
                p_SobrepesoK = "7"
                p_SobrepesoG = "0"
                p_ObesoK = "6"
                p_ObesoG = "300"
                p_IdealK = "5"
                p_IdealG = "500"
                p_BajoPesoK = "5"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "4"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 3:
                p_SobrepesoK = "8"
                p_SobrepesoG = "0"
                p_ObesoK = "7"
                p_ObesoG = "100"
                p_IdealK = "6"
                p_IdealG = "400"
                p_BajoPesoK = "5"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "5"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 4:
                p_SobrepesoK = "8"
                p_SobrepesoG = "600"
                p_ObesoK = "7"
                p_ObesoG = "900"
                p_IdealK = "7"
                p_IdealG = "0"
                p_BajoPesoK = "6"
                p_BajoPesoG = "300"
                p_BajoPesoSeveroK = "5"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 5:
                p_SobrepesoK = "9"
                p_SobrepesoG = "400"
                p_ObesoK = "8"
                p_ObesoG = "400"
                p_IdealK = "7"
                p_IdealG = "500"
                p_BajoPesoK = "6"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 6:
                p_SobrepesoK = "9"
                p_SobrepesoG = "800"
                p_ObesoK = "8"
                p_ObesoG = "800"
                p_IdealK = "8"
                p_IdealG = "0"
                p_BajoPesoK = "7"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 7:
                p_SobrepesoK = "10"
                p_SobrepesoG = "300"
                p_ObesoK = "9"
                p_ObesoG = "200"
                p_IdealK = "8"
                p_IdealG = "400"
                p_BajoPesoK = "7"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 8:
                p_SobrepesoK = "10"
                p_SobrepesoG = "700"
                p_ObesoK = "9"
                p_ObesoG = "600"
                p_IdealK = "8"
                p_IdealG = "600"
                p_BajoPesoK = "7"
                p_BajoPesoG = "700"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 9:
                p_SobrepesoK = "11"
                p_SobrepesoG = "0"
                p_ObesoK = "10"
                p_ObesoG = "0"
                p_IdealK = "8"
                p_IdealG = "900"
                p_BajoPesoK = "8"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 10:
                p_SobrepesoK = "11"
                p_SobrepesoG = "400"
                p_ObesoK = "10"
                p_ObesoG = "300"
                p_IdealK = "9"
                p_IdealG = "100"
                p_BajoPesoK = "8"
                p_BajoPesoG = "200"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 11:
                p_SobrepesoK = "11"
                p_SobrepesoG = "700"
                p_ObesoK = "10"
                p_ObesoG = "500"
                p_IdealK = "9"
                p_IdealG = "500"
                p_BajoPesoK = "8"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "500"
        if edad_anios == 1:
            if edad_meses == 0:
                p_SobrepesoK = "12"
                p_SobrepesoG = "0"
                p_ObesoK = "10"
                p_ObesoG = "800"
                p_IdealK = "9"
                p_IdealG = "600"
                p_BajoPesoK = "8"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 1:
                p_SobrepesoK = "12"
                p_SobrepesoG = "300"
                p_ObesoK = "11"
                p_ObesoG = "0"
                p_IdealK = "9"
                p_IdealG = "900"
                p_BajoPesoK = "8"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 2:
                p_SobrepesoK = "12"
                p_SobrepesoG = "600"
                p_ObesoK = "11"
                p_ObesoG = "300"
                p_IdealK = "10"
                p_IdealG = "100"
                p_BajoPesoK = "9"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 3:
                p_SobrepesoK = "12"
                p_SobrepesoG = "900"
                p_ObesoK = "11"
                p_ObesoG = "500"
                p_IdealK = "10"
                p_IdealG = "400"
                p_BajoPesoK = "9"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 4:
                p_SobrepesoK = "13"
                p_SobrepesoG = "100"
                p_ObesoK = "11"
                p_ObesoG = "800"
                p_IdealK = "10"
                p_IdealG = "500"
                p_BajoPesoK = "9"
                p_BajoPesoG = "300"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 5:
                p_SobrepesoK = "13"
                p_SobrepesoG = "400"
                p_ObesoK = "12"
                p_ObesoG = "0"
                p_IdealK = "10"
                p_IdealG = "800"
                p_BajoPesoK = "9"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 6:
                p_SobrepesoK = "13"
                p_SobrepesoG = "600"
                p_ObesoK = "12"
                p_ObesoG = "200"
                p_IdealK = "11"
                p_IdealG = "0"
                p_BajoPesoK = "9"
                p_BajoPesoG = "700"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "700"
            if edad_meses == 7:
                p_SobrepesoK = "13"
                p_SobrepesoG = "900"
                p_ObesoK = "12"
                p_ObesoG = "500"
                p_IdealK = "11"
                p_IdealG = "100"
                p_BajoPesoK = "10"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 8:
                p_SobrepesoK = "14"
                p_SobrepesoG = "200"
                p_ObesoK = "12"
                p_ObesoG = "700"
                p_IdealK = "11"
                p_IdealG = "400"
                p_BajoPesoK = "10"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 9:
                p_SobrepesoK = "14"
                p_SobrepesoG = "500"
                p_ObesoK = "12"
                p_ObesoG = "900"
                p_IdealK = "11"
                p_IdealG = "500"
                p_BajoPesoK = "10"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 10:
                p_SobrepesoK = "14"
                p_SobrepesoG = "700"
                p_ObesoK = "13"
                p_ObesoG = "100"
                p_IdealK = "11"
                p_IdealG = "800"
                p_BajoPesoK = "10"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 11:
                p_SobrepesoK = "15"
                p_SobrepesoG = "0"
                p_ObesoK = "13"
                p_ObesoG = "400"
                p_IdealK = "12"
                p_IdealG = "0"
                p_BajoPesoK = "10"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "500"
        if edad_anios == 2:
            if edad_meses == 0:
        		p_SobrepesoK = "15"
        		p_SobrepesoG = "300"
        		p_ObesoK = "13"
        		p_ObesoG = "600"
        		p_IdealK = "12"
        		p_IdealG = "100"
        		p_BajoPesoK = "10"
        		p_BajoPesoG = "800"
        		p_BajoPesoSeveroK = "9"
        		p_BajoPesoSeveroG = "600"
            if edad_meses == 1:
                p_SobrepesoK = "15"
                p_SobrepesoG = "500"
                p_ObesoK = "13"
                p_ObesoG = "900"
                p_IdealK = "12"
                p_IdealG = "400"
                p_BajoPesoK = "11"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 2:
                p_SobrepesoK = "15"
                p_SobrepesoG = "800"
                p_ObesoK = "14"
                p_ObesoG = "100"
                p_IdealK = "12"
                p_IdealG = "500"
                p_BajoPesoK = "11"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 3:
                p_SobrepesoK = "16"
                p_SobrepesoG = "100"
                p_ObesoK = "14"
                p_ObesoG = "400"
                p_IdealK = "12"
                p_IdealG = "700"
                p_BajoPesoK = "11"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 4:
                p_SobrepesoK = "16"
                p_SobrepesoG = "400"
                p_ObesoK = "14"
                p_ObesoG = "500"
                p_IdealK = "13"
                p_IdealG = "0"
                p_BajoPesoK = "11"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 5:
                p_SobrepesoK = "16"
                p_SobrepesoG = "600"
                p_ObesoK = "14"
                p_ObesoG = "700"
                p_IdealK = "13"
                p_IdealG = "100"
                p_BajoPesoK = "11"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 6:
                p_SobrepesoK = "16"
                p_SobrepesoG = "800"
                p_ObesoK = "15"
                p_ObesoG = "0"
                p_IdealK = "13"
                p_IdealG = "300"
                p_BajoPesoK = "11"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 7:
                p_SobrepesoK = "17"
                p_SobrepesoG = "100"
                p_ObesoK = "15"
                p_ObesoG = "200"
                p_IdealK = "13"
                p_IdealG = "500"
                p_BajoPesoK = "12"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "700"
            if edad_meses == 8:
                p_SobrepesoK = "17"
                p_SobrepesoG = "400"
                p_ObesoK = "15"
                p_ObesoG = "400"
                p_IdealK = "13"
                p_IdealG = "600"
                p_BajoPesoK = "12"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 9:
                p_SobrepesoK = "17"
                p_SobrepesoG = "600"
                p_ObesoK = "15"
                p_ObesoG = "600"
                p_IdealK = "13"
                p_IdealG = "900"
                p_BajoPesoK = "12"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 10:
                p_SobrepesoK = "17"
                p_SobrepesoG = "800"
                p_ObesoK = "15"
                p_ObesoG = "800"
                p_IdealK = "14"
                p_IdealG = "0"
                p_BajoPesoK = "12"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 11:
                p_SobrepesoK = "18"
                p_SobrepesoG = "0"
                p_ObesoK = "16"
                p_ObesoG = "0"
                p_IdealK = "14"
                p_IdealG = "100"
                p_BajoPesoK = "12"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "100"
        if edad_anios == 3:
            if edad_meses == 0:
                p_SobrepesoK = "18"
                p_SobrepesoG = "400"
                p_ObesoK = "16"
                p_ObesoG = "100"
                p_IdealK = "14"
                p_IdealG = "400"
                p_BajoPesoK = "12"
                p_BajoPesoG = "700"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 1:
                p_SobrepesoK = "18"
                p_SobrepesoG = "600"
                p_ObesoK = "16"
                p_ObesoG = "400"
                p_IdealK = "14"
                p_IdealG = "500"
                p_BajoPesoK = "12"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 2:
                p_SobrepesoK = "18"
                p_SobrepesoG = "800"
                p_ObesoK = "16"
                p_ObesoG = "600"
                p_IdealK = "14"
                p_IdealG = "600"
                p_BajoPesoK = "13"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 3:
                p_SobrepesoK = "19"
                p_SobrepesoG = "0"
                p_ObesoK = "16"
                p_ObesoG = "800"
                p_IdealK = "14"
                p_IdealG = "900"
                p_BajoPesoK = "13"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 4:
                p_SobrepesoK = "19"
                p_SobrepesoG = "300"
                p_ObesoK = "17"
                p_ObesoG = "0"
                p_IdealK = "15"
                p_IdealG = "0"
                p_BajoPesoK = "13"
                p_BajoPesoG = "300"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "700"
            if edad_meses == 5:
                p_SobrepesoK = "19"
                p_SobrepesoG = "500"
                p_ObesoK = "17"
                p_ObesoG = "200"
                p_IdealK = "15"
                p_IdealG = "200"
                p_BajoPesoK = "13"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 6:
                p_SobrepesoK = "19"
                p_SobrepesoG = "800"
                p_ObesoK = "17"
                p_ObesoG = "400"
                p_IdealK = "15"
                p_IdealG = "400"
                p_BajoPesoK = "13"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 7:
                p_SobrepesoK = "20"
                p_SobrepesoG = "0"
                p_ObesoK = "17"
                p_ObesoG = "600"
                p_IdealK = "15"
                p_IdealG = "500"
                p_BajoPesoK = "13"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 8:
                p_SobrepesoK = "20"
                p_SobrepesoG = "200"
                p_ObesoK = "17"
                p_ObesoG = "800"
                p_IdealK = "15"
                p_IdealG = "600"
                p_BajoPesoK = "13"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "300"
            if edad_meses == 9:
                p_SobrepesoK = "20"
                p_SobrepesoG = "500"
                p_ObesoK = "18"
                p_ObesoG = "0"
                p_IdealK = "15"
                p_IdealG = "900"
                p_BajoPesoK = "14"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 10:
                p_SobrepesoK = "20"
                p_SobrepesoG = "800"
                p_ObesoK = "18"
                p_ObesoG = "100"
                p_IdealK = "16"
                p_IdealG = "0"
                p_BajoPesoK = "14"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 11:
                p_SobrepesoK = "21"
                p_SobrepesoG = "0"
                p_ObesoK = "18"
                p_ObesoG = "400"
                p_IdealK = "16"
                p_IdealG = "100"
                p_BajoPesoK = "14"
                p_BajoPesoG = "300"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "600"
        if edad_anios == 4:
            if edad_meses == 0:
                p_SobrepesoK = "21"
                p_SobrepesoG = "100"
                p_ObesoK = "18"
                p_ObesoG = "600"
                p_IdealK = "16"
                p_IdealG = "400"
                p_BajoPesoK = "14"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 1:
                p_SobrepesoK = "21"
                p_SobrepesoG = "400"
                p_ObesoK = "18"
                p_ObesoG = "800"
                p_IdealK = "16"
                p_IdealG = "500"
                p_BajoPesoK = "14"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 2:
                p_SobrepesoK = "21"
                p_SobrepesoG = "600"
                p_ObesoK = "19"
                p_ObesoG = "0"
                p_IdealK = "16"
                p_IdealG = "600"
                p_BajoPesoK = "14"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 3:
                p_SobrepesoK = "22"
                p_SobrepesoG = "0"
                p_ObesoK = "19"
                p_ObesoG = "200"
                p_IdealK = "16"
                p_IdealG = "900"
                p_BajoPesoK = "14"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 4:
                p_SobrepesoK = "22"
                p_SobrepesoG = "100"
                p_ObesoK = "19"
                p_ObesoG = "400"
                p_IdealK = "17"
                p_IdealG = "0"
                p_BajoPesoK = "15"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 5:
                p_SobrepesoK = "22"
                p_SobrepesoG = "400"
                p_ObesoK = "19"
                p_ObesoG = "600"
                p_IdealK = "17"
                p_IdealG = "100"
                p_BajoPesoK = "15"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "300"
            if edad_meses == 6:
                p_SobrepesoK = "22"
                p_SobrepesoG = "600"
                p_ObesoK = "19"
                p_ObesoG = "800"
                p_IdealK = "17"
                p_IdealG = "400"
                p_BajoPesoK = "15"
                p_BajoPesoG = "200"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 7:
                p_SobrepesoK = "23"
                p_SobrepesoG = "0"
                p_ObesoK = "20"
                p_ObesoG = "0"
                p_IdealK = "17"
                p_IdealG = "500"
                p_BajoPesoK = "15"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 8:
                p_SobrepesoK = "23"
                p_SobrepesoG = "100"
                p_ObesoK = "20"
                p_ObesoG = "100"
                p_IdealK = "17"
                p_IdealG = "600"
                p_BajoPesoK = "15"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 9:
                p_SobrepesoK = "23"
                p_SobrepesoG = "400"
                p_ObesoK = "20"
                p_ObesoG = "500"
                p_IdealK = "17"
                p_IdealG = "900"
                p_BajoPesoK = "15"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 10:
                p_SobrepesoK = "23"
                p_SobrepesoG = "600"
                p_ObesoK = "20"
                p_ObesoG = "600"
                p_IdealK = "18"
                p_IdealG = "0"
                p_BajoPesoK = "15"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 11:
                p_SobrepesoK = "23"
                p_SobrepesoG = "900"
                p_ObesoK = "20"
                p_ObesoG = "900"
                p_IdealK = "18"
                p_IdealG = "100"
                p_BajoPesoK = "15"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "14"
                p_BajoPesoSeveroG = "0"
        if edad_anios == 5:
            if edad_meses == 0:
                p_SobrepesoK = "24"
                p_SobrepesoG = "100"
                p_ObesoK = "21"
                p_ObesoG = "0"
                p_IdealK = "18"
                p_IdealG = "300"
                p_BajoPesoK = "16"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "14"
                p_BajoPesoSeveroG = "100"
    else:
        if edad_anios < 1:
            if edad_meses == 0:
                p_SobrepesoK = "4"
                p_SobrepesoG = "250"
                p_ObesoK = "3"
                p_ObesoG = "700"
                p_IdealK = "3"
                p_IdealG = "200"
                p_BajoPesoK = "2"
                p_BajoPesoG = "700"
                p_BajoPesoSeveroK = "2"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 1:
                p_SobrepesoK = "5"
                p_SobrepesoG = "500"
                p_ObesoK = "4"
                p_ObesoG = "800"
                p_IdealK = "4"
                p_IdealG = "200"
                p_BajoPesoK = "3"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "2"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 2:
                p_SobrepesoK = "6"
                p_SobrepesoG = "600"
                p_ObesoK = "5"
                p_ObesoG = "900"
                p_IdealK = "5"
                p_IdealG = "100"
                p_BajoPesoK = "4"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "4"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 3:
                p_SobrepesoK = "7"
                p_SobrepesoG = "500"
                p_ObesoK = "6"
                p_ObesoG = "600"
                p_IdealK = "5"
                p_IdealG = "900"
                p_BajoPesoK = "5"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "4"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 4:
                p_SobrepesoK = "8"
                p_SobrepesoG = "200"
                p_ObesoK = "7"
                p_ObesoG = "200"
                p_IdealK = "6"
                p_IdealG = "500"
                p_BajoPesoK = "5"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "5"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 5:
                p_SobrepesoK = "8"
                p_SobrepesoG = "900"
                p_ObesoK = "7"
                p_ObesoG = "900"
                p_IdealK = "7"
                p_IdealG = "0"
                p_BajoPesoK = "6"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "4"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 6:
                p_SobrepesoK = "9"
                p_SobrepesoG = "400"
                p_ObesoK = "8"
                p_ObesoG = "250"
                p_IdealK = "7"
                p_IdealG = "400"
                p_BajoPesoK = "6"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "5"
                p_BajoPesoSeveroG = "700"
            if edad_meses == 7:
                p_SobrepesoK = "9"
                p_SobrepesoG = "900"
                p_ObesoK = "8"
                p_ObesoG = "600"
                p_IdealK = "7"
                p_IdealG = "700"
                p_BajoPesoK = "6"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 8:
                p_SobrepesoK = "10"
                p_SobrepesoG = "100"
                p_ObesoK = "9"
                p_ObesoG = "0"
                p_IdealK = "8"
                p_IdealG = "0"
                p_BajoPesoK = "7"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 9:
                p_SobrepesoK = "10"
                p_SobrepesoG = "500"
                p_ObesoK = "9"
                p_ObesoG = "400"
                p_IdealK = "8"
                p_IdealG = "300"
                p_BajoPesoK = "7"
                p_BajoPesoG = "300"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 10:
                p_SobrepesoK = "10"
                p_SobrepesoG = "900"
                p_ObesoK = "9"
                p_ObesoG = "600"
                p_IdealK = "8"
                p_IdealG = "500"
                p_BajoPesoK = "7"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 11:
                p_SobrepesoK = "11"
                p_SobrepesoG = "200"
                p_ObesoK = "9"
                p_ObesoG = "900"
                p_IdealK = "8"
                p_IdealG = "800"
                p_BajoPesoK = "7"
                p_BajoPesoG = "700"
                p_BajoPesoSeveroK = "6"
                p_BajoPesoSeveroG = "900"
        if edad_anios == 1:
            if edad_meses == 0:
                p_SobrepesoK = "11"
                p_SobrepesoG = "500"
                p_ObesoK = "10"
                p_ObesoG = "100"
                p_IdealK = "9"
                p_IdealG = "0"
                p_BajoPesoK = "7"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 1:
                p_SobrepesoK = "11"
                p_SobrepesoG = "800"
                p_ObesoK = "10"
                p_ObesoG = "900"
                p_IdealK = "9"
                p_IdealG = "200"
                p_BajoPesoK = "8"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 2:
                p_SobrepesoK = "12"
                p_SobrepesoG = "100"
                p_ObesoK = "10"
                p_ObesoG = "600"
                p_IdealK = "9"
                p_IdealG = "400"
                p_BajoPesoK = "8"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 3:
                p_SobrepesoK = "12"
                p_SobrepesoG = "400"
                p_ObesoK = "10"
                p_ObesoG = "900"
                p_IdealK = "9"
                p_IdealG = "600"
                p_BajoPesoK = "8"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 4:
                p_SobrepesoK = "12"
                p_SobrepesoG = "600"
                p_ObesoK = "11"
                p_ObesoG = "100"
                p_IdealK = "9"
                p_IdealG = "900"
                p_BajoPesoK = "8"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "700"
            if edad_meses == 5:
                p_SobrepesoK = "12"
                p_SobrepesoG = "900"
                p_ObesoK = "11"
                p_ObesoG = "400"
                p_IdealK = "10"
                p_IdealG = "0"
                p_BajoPesoK = "8"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "7"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 6:
                p_SobrepesoK = "13"
                p_SobrepesoG = "200"
                p_ObesoK = "11"
                p_ObesoG = "600"
                p_IdealK = "10"
                p_IdealG = "200"
                p_BajoPesoK = "9"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 7:
                p_SobrepesoK = "13"
                p_SobrepesoG = "500"
                p_ObesoK = "11"
                p_ObesoG = "800"
                p_IdealK = "10"
                p_IdealG = "500"
                p_BajoPesoK = "9"
                p_BajoPesoG = "300"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 8:
                p_SobrepesoK = "13"
                p_SobrepesoG = "700"
                p_ObesoK = "12"
                p_ObesoG = "100"
                p_IdealK = "10"
                p_IdealG = "600"
                p_BajoPesoK = "9"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 9:
                p_SobrepesoK = "14"
                p_SobrepesoG = "0"
                p_ObesoK = "12"
                p_ObesoG = "300"
                p_IdealK = "10"
                p_IdealG = "800"
                p_BajoPesoK = "9"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 10:
                p_SobrepesoK = "14"
                p_SobrepesoG = "400"
                p_ObesoK = "12"
                p_ObesoG = "500"
                p_IdealK = "11"
                p_IdealG = "0"
                p_BajoPesoK = "9"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "700"
            if edad_meses == 11:
                p_SobrepesoK = "14"
                p_SobrepesoG = "600"
                p_ObesoK = "12"
                p_ObesoG = "700"
                p_IdealK = "11"
                p_IdealG = "200"
                p_BajoPesoK = "10"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "8"
                p_BajoPesoSeveroG = "900"
        if edad_anios == 2:
            if edad_meses == 0:
        		p_SobrepesoK = "14"
        		p_SobrepesoG = "800"
        		p_ObesoK = "13"
        		p_ObesoG = "0"
        		p_IdealK = "11"
        		p_IdealG = "500"
        		p_BajoPesoK = "10"
        		p_BajoPesoG = "100"
        		p_BajoPesoSeveroK = "9"
        		p_BajoPesoSeveroG = "0"
            if edad_meses == 1:
                p_SobrepesoK = "15"
                p_SobrepesoG = "100"
                p_ObesoK = "13"
                p_ObesoG = "300"
                p_IdealK = "11"
                p_IdealG = "700"
                p_BajoPesoK = "10"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 2:
                p_SobrepesoK = "15"
                p_SobrepesoG = "400"
                p_ObesoK = "13"
                p_ObesoG = "500"
                p_IdealK = "12"
                p_IdealG = "0"
                p_BajoPesoK = "10"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 3:
                p_SobrepesoK = "15"
                p_SobrepesoG = "600"
                p_ObesoK = "13"
                p_ObesoG = "600"
                p_IdealK = "12"
                p_IdealG = "200"
                p_BajoPesoK = "10"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 4:
                p_SobrepesoK = "16"
                p_SobrepesoG = "0"
                p_ObesoK = "14"
                p_ObesoG = "0"
                p_IdealK = "12"
                p_IdealG = "400"
                p_BajoPesoK = "10"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 5:
                p_SobrepesoK = "16"
                p_SobrepesoG = "200"
                p_ObesoK = "14"
                p_ObesoG = "200"
                p_IdealK = "12"
                p_IdealG = "500"
                p_BajoPesoK = "11"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "9"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 6:
                p_SobrepesoK = "16"
                p_SobrepesoG = "500"
                p_ObesoK = "14"
                p_ObesoG = "500"
                p_IdealK = "12"
                p_IdealG = "800"
                p_BajoPesoK = "11"
                p_BajoPesoG = "200"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 7:
                p_SobrepesoK = "16"
                p_SobrepesoG = "800"
                p_ObesoK = "14"
                p_ObesoG = "600"
                p_IdealK = "12"
                p_IdealG = "900"
                p_BajoPesoK = "11"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 8:
                p_SobrepesoK = "17"
                p_SobrepesoG = "0"
                p_ObesoK = "15"
                p_ObesoG = "0"
                p_IdealK = "13"
                p_IdealG = "0"
                p_BajoPesoK = "11"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 9:
                p_SobrepesoK = "17"
                p_SobrepesoG = "400"
                p_ObesoK = "15"
                p_ObesoG = "100"
                p_IdealK = "13"
                p_IdealG = "300"
                p_BajoPesoK = "11"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 10:
                p_SobrepesoK = "17"
                p_SobrepesoG = "600"
                p_ObesoK = "15"
                p_ObesoG = "400"
                p_IdealK = "13"
                p_IdealG = "500"
                p_BajoPesoK = "11"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 11:
                p_SobrepesoK = "17"
                p_SobrepesoG = "900"
                p_ObesoK = "15"
                p_ObesoG = "500"
                p_IdealK = "13"
                p_IdealG = "600"
                p_BajoPesoK = "12"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "600"
        if edad_anios == 3:
            if edad_meses == 0:
        		p_SobrepesoK = "18"
        		p_SobrepesoG = "100"
        		p_ObesoK = "15"
        		p_ObesoG = "800"
        		p_IdealK = "13"
        		p_IdealG = "900"
        		p_BajoPesoK = "12"
        		p_BajoPesoG = "200"
        		p_BajoPesoSeveroK = "10"
        		p_BajoPesoSeveroG = "700"
            if edad_meses == 1:
                p_SobrepesoK = "18"
                p_SobrepesoG = "500"
                p_ObesoK = "16"
                p_ObesoG = "0"
                p_IdealK = "14"
                p_IdealG = "0"
                p_BajoPesoK = "12"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "10"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 2:
                p_SobrepesoK = "18"
                p_SobrepesoG = "600"
                p_ObesoK = "16"
                p_ObesoG = "200"
                p_IdealK = "14"
                p_IdealG = "100"
                p_BajoPesoK = "12"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "0"
            if edad_meses == 3:
                p_SobrepesoK = "19"
                p_SobrepesoG = "0"
                p_ObesoK = "16"
                p_ObesoG = "500"
                p_IdealK = "14"
                p_IdealG = "400"
                p_BajoPesoK = "12"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 4:
                p_SobrepesoK = "19"
                p_SobrepesoG = "200"
                p_ObesoK = "16"
                p_ObesoG = "600"
                p_IdealK = "14"
                p_IdealG = "500"
                p_BajoPesoK = "12"
                p_BajoPesoG = "700"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 5:
                p_SobrepesoK = "19"
                p_SobrepesoG = "500"
                p_ObesoK = "17"
                p_ObesoG = "0"
                p_IdealK = "14"
                p_IdealG = "800"
                p_BajoPesoK = "13"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 6:
                p_SobrepesoK = "19"
                p_SobrepesoG = "800"
                p_ObesoK = "17"
                p_ObesoG = "200"
                p_IdealK = "15"
                p_IdealG = "0"
                p_BajoPesoK = "13"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 7:
                p_SobrepesoK = "20"
                p_SobrepesoG = "100"
                p_ObesoK = "17"
                p_ObesoG = "400"
                p_IdealK = "15"
                p_IdealG = "100"
                p_BajoPesoK = "13"
                p_BajoPesoG = "200"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 8:
                p_SobrepesoK = "20"
                p_SobrepesoG = "400"
                p_ObesoK = "17"
                p_ObesoG = "600"
                p_IdealK = "15"
                p_IdealG = "400"
                p_BajoPesoK = "13"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "11"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 9:
                p_SobrepesoK = "20"
                p_SobrepesoG = "600"
                p_ObesoK = "17"
                p_ObesoG = "900"
                p_IdealK = "15"
                p_IdealG = "500"
                p_BajoPesoK = "13"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 10:
                p_SobrepesoK = "21"
                p_SobrepesoG = "0"
                p_ObesoK = "18"
                p_ObesoG = "0"
                p_IdealK = "15"
                p_IdealG = "700"
                p_BajoPesoK = "13"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 11:
                p_SobrepesoK = "21"
                p_SobrepesoG = "200"
                p_ObesoK = "18"
                p_ObesoG = "400"
                p_IdealK = "15"
                p_IdealG = "900"
                p_BajoPesoK = "13"
                p_BajoPesoG = "900"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "300"
        if edad_anios == 4:
            if edad_meses == 0:
                p_SobrepesoK = "21"
                p_SobrepesoG = "500"
                p_ObesoK = "18"
                p_ObesoG = "500"
                p_IdealK = "16"
                p_IdealG = "0"
                p_BajoPesoK = "14"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 1:
                p_SobrepesoK = "21"
                p_SobrepesoG = "800"
                p_ObesoK = "18"
                p_ObesoG = "800"
                p_IdealK = "16"
                p_IdealG = "200"
                p_BajoPesoK = "14"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 2:
                p_SobrepesoK = "22"
                p_SobrepesoG = "100"
                p_ObesoK = "19"
                p_ObesoG = "0"
                p_IdealK = "16"
                p_IdealG = "500"
                p_BajoPesoK = "14"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "600"
            if edad_meses == 3:
                p_SobrepesoK = "22"
                p_SobrepesoG = "400"
                p_ObesoK = "19"
                p_ObesoG = "200"
                p_IdealK = "16"
                p_IdealG = "600"
                p_BajoPesoK = "14"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "700"
            if edad_meses == 4:
                p_SobrepesoK = "22"
                p_SobrepesoG = "600"
                p_ObesoK = "19"
                p_ObesoG = "500"
                p_IdealK = "16"
                p_IdealG = "800"
                p_BajoPesoK = "14"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "800"
            if edad_meses == 5:
                p_SobrepesoK = "23"
                p_SobrepesoG = "0"
                p_ObesoK = "19"
                p_ObesoG = "600"
                p_IdealK = "17"
                p_IdealG = "0"
                p_BajoPesoK = "14"
                p_BajoPesoG = "700"
                p_BajoPesoSeveroK = "12"
                p_BajoPesoSeveroG = "900"
            if edad_meses == 6:
                p_SobrepesoK = "23"
                p_SobrepesoG = "100"
                p_ObesoK = "19"
                p_ObesoG = "900"
                p_IdealK = "17"
                p_IdealG = "100"
                p_BajoPesoK = "15"
                p_BajoPesoG = "0"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "100"
            if edad_meses == 7:
                p_SobrepesoK = "23"
                p_SobrepesoG = "500"
                p_ObesoK = "20"
                p_ObesoG = "100"
                p_IdealK = "17"
                p_IdealG = "400"
                p_BajoPesoK = "15"
                p_BajoPesoG = "100"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "200"
            if edad_meses == 8:
                p_SobrepesoK = "23"
                p_SobrepesoG = "800"
                p_ObesoK = "20"
                p_ObesoG = "400"
                p_IdealK = "17"
                p_IdealG = "500"
                p_BajoPesoK = "15"
                p_BajoPesoG = "200"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "300"
            if edad_meses == 9:
                p_SobrepesoK = "24"
                p_SobrepesoG = "0"
                p_ObesoK = "20"
                p_ObesoG = "600"
                p_IdealK = "17"
                p_IdealG = "600"
                p_BajoPesoK = "15"
                p_BajoPesoG = "400"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "400"
            if edad_meses == 10:
                p_SobrepesoK = "24"
                p_SobrepesoG = "400"
                p_ObesoK = "20"
                p_ObesoG = "800"
                p_IdealK = "17"
                p_IdealG = "900"
                p_BajoPesoK = "15"
                p_BajoPesoG = "500"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "500"
            if edad_meses == 11:
                p_SobrepesoK = "24"
                p_SobrepesoG = "600"
                p_ObesoK = "21"
                p_ObesoG = "0"
                p_IdealK = "18"
                p_IdealG = "0"
                p_BajoPesoK = "15"
                p_BajoPesoG = "600"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "600"
        if edad_anios == 5:
            if edad_meses == 0:
                p_SobrepesoK = "24"
                p_SobrepesoG = "900"
                p_ObesoK = "21"
                p_ObesoG = "100"
                p_IdealK = "18"
                p_IdealG = "100"
                p_BajoPesoK = "15"
                p_BajoPesoG = "800"
                p_BajoPesoSeveroK = "13"
                p_BajoPesoSeveroG = "800"

    c = Controles.objects.get(id=id)
    c.peso_SobrepesoK = p_SobrepesoK
    c.peso_SobrepesoG = p_SobrepesoG
    c.peso_ObesoK = p_ObesoK
    c.peso_ObesoG = p_ObesoG
    c.peso_idealK = p_IdealK
    c.peso_idealG = p_IdealG
    c.peso_BajoPesoK = p_BajoPesoK
    c.peso_BajoPesoG = p_BajoPesoG
    c.peso_BajoPesoSeveroK = p_BajoPesoSeveroK
    c.peso_BajoPesoSeveroG = p_BajoPesoSeveroG
    #c.talla_ideal = t_Ideal
    c.save()
    asignarClase(id,p_SobrepesoK,p_SobrepesoG,p_ObesoK,p_ObesoG,p_IdealK,p_IdealG,p_BajoPesoK,p_BajoPesoG,p_BajoPesoSeveroK,p_BajoPesoSeveroG,pesoK,pesoG)

############## FUNCION ASIGNAR CLASE CUANDO EL PESO O TALLA ESTA FUERA DE RANGO  #######################

def asignarClase(id,p_SobrepesoK,p_SobrepesoG,p_ObesoK,p_ObesoG,p_IdealK,p_IdealG,p_BajoPesoK,p_BajoPesoG,p_BajoPesoSeveroK,p_BajoPesoSeveroG,pesoK,pesoG):
    peso = float(str(pesoK)+"."+str(pesoG))
    Sobrepeso = float(str(p_SobrepesoK)+"."+str(p_SobrepesoG))
    Obeso = float(str(p_ObesoK)+"."+str(p_ObesoG))
    Ideal = float(str(p_IdealK)+"."+str(p_IdealG))
    BajoPeso = float(str(p_BajoPesoK)+"."+str(p_BajoPesoG))
    BajoPesoSevero = float(str(p_BajoPesoSeveroK)+"."+str(p_BajoPesoSeveroG))

    if peso > Obeso and peso <= Sobrepeso or peso > Obeso and peso >= Sobrepeso :
        c_peso = "Sobrepeso"
        interpretacion = "SOBREPESO"
    else:
        if peso > Ideal and peso <= Obeso:
            c_peso = "Obeso"
            interpretacion = "OBESO"
        else:
            if peso > BajoPeso and peso <= Ideal:
                c_peso = "Promedio"
                interpretacion = "PESO IDEAL"
            else:
                if peso > BajoPesoSevero and peso <= BajoPeso:
                    c_peso = "Bajo"
                    interpretacion = "BAJO PESO"
                else:
                    c_peso = "Severo"
                    interpretacion = "BAJO PESO SEVERO"

    c = Controles.objects.get(id=id)
    c.clase_peso = c_peso
    #c.clase_talla = c_talla
    c.interpretacion = interpretacion
    c.save()

############## FUNCION GUARDAR GRAFICAS DEL BENEFICIARIO ######################

def guardarGraficas(request):
    if request.method == 'POST':
        b = Beneficiario.objects.get(id=request.POST['beneficiario'])
        b.grafica_peso = request.POST['grafica_peso']
        #b.grafica_talla = request.POST['grafica_talla']
        b.save()
        return HttpResponse('Guardadas Correctamente',status=200)
    else:
        return HttpResponse('Solicitud Incorrecta',status=501)

############## FUNCION GENERAR PDF MEDIDAS ANTROPOMETRICAS ######################

@login_required(login_url="login:login")
def MedidasAntropometricasPDF(request, id=None):
    try:
        logo = "icbf-reporte.png"
        beneficiario = Beneficiario.objects.get(id = id)
        controles = Controles.objects.filter(beneficiario=id).order_by("total_meses")
        result = StringIO()
        html = render_to_string("reportes/medidas_antropometricas_pdf.html",{'url':URL,'logo':logo,'beneficiario':beneficiario,'controles':controles,'titulo':'MEDIDAS ANTROPOMETRICAS'})
        pdf = pisa.pisaDocument(html,result)
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/")

############## FUNCION GENERAR PDF ENFERMEDADES ######################

@login_required(login_url="login:login")
def EnfermedadesPDF(request, id=None):
    try:
        logo = "icbf-reporte.png"
        beneficiario = Beneficiario.objects.get(id = id)
        if beneficiario.tipo_beneficiario == "1":
            tipo = 'Niño'
        else:
            tipo = 'Niña'
        result = StringIO()
        html= render_to_string("reportes/enfermedades_pdf.html",{"url": URL, "logo": logo, "beneficiario": beneficiario , "tipo": tipo, "titulo": "ENFERMEDADES" })
        pdf = pisa.pisaDocument(html,result)
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/")
