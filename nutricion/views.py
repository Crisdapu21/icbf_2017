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
import json, os

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
            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Nutrición','Guardar Nutrición',e.primer_nombre+" "+e.segundo_nombre+" "+e.primer_apellido+" "+e.segundo_apellido)
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
            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Nutrición','Actualizar Nutrición',e.primer_nombre+" "+e.segundo_nombre+" "+e.primer_apellido+" "+e.segundo_apellido)
        messages.success(request, 'Nutricion')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")

################## TEMPLATE AGREGAR MEDIDAS ANTROPOMETRICAS ######################

@login_required(login_url="login:login")
def medidasAntropometricas(request, id=None):
    beneficiario = Beneficiario.objects.get(id = id)
    controles = Controles.objects.filter(beneficiario=id).order_by("fecha_control")[::-1]
    return render(request,'nutricion/agregar_medidas.html',{'controles': controles, 'beneficiario': beneficiario })

################## FUNCION GUARDAR MEDIDAS ANTROPOMETRICAS ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarMedidasAntropometricas(request):
    if request.method == 'POST':
        c = Controles()
        c.beneficiario_id  = request.POST['e_ben']
        c.numero_orden = request.POST['nutricion_numero_orden']
        c.fecha_control = request.POST['nutricion_fecha_control']
        c.edad_anios =  request.POST['nutricion_edad_anios']
        c.edad_meses =  request.POST['nutricion_edad_meses']
        c.peso_kilos =  request.POST['nutricion_peso_kilos']
        c.peso_gramos =  request.POST['nutricion_peso_gramos']
        c.talla =  request.POST['nutricion_talla']
        c.interpretacion =  request.POST['nutricion_interpretacion']
        c.save()

        e = Beneficiario.objects.get(id=request.POST['e_ben'])
        registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Nutrición','Guardar Medidas Antropometricas',e.primer_nombre+" "+e.segundo_nombre+" "+e.primer_apellido+" "+e.segundo_apellido)
        peso_talla_Ideal(c.id,e.genero,e.edad_anios,c.peso_kilos,c.peso_gramos,c.talla)
        messages.success(request, 'Guardado')
        return HttpResponseRedirect('/beneficiarios/medidas_antropometricas/'+request.POST['e_ben'])
    else:
        return HttpResponseRedirect("/")

def peso_talla_Ideal(id,genero,edad,pesoK,pesoG,talla):
    edad = int(edad)
    if genero == "M":
        if edad <= 1:
            p_IdealK = "10"
            p_IdealG = "2"
            t_Ideal = "76"
        if edad >1 and edad <=2:
            p_IdealK = "12"
            p_IdealG = "9"
            t_Ideal = "88"
        if edad >2 and edad <=3:
            p_IdealK = "15"
            p_IdealG = "1"
            t_Ideal = "96"
        if edad >3 and edad <=4:
            p_IdealK = "16"
            p_IdealG = "07"
            t_Ideal = "100"
        if edad >4 and edad <=5:
            p_IdealK = "18"
            p_IdealG = "03"
            t_Ideal = "106"
    else:
        if edad <= 1:
            p_IdealK = "9"
            p_IdealG = "5"
            t_Ideal = "74"
        if edad >1 and edad <=2:
            p_IdealK = "12"
            p_IdealG = "4"
            t_Ideal = "86"
        if edad >2 and edad<=3:
            p_IdealK = "14"
            p_IdealG = "4"
            t_Ideal = "95"
        if edad >3 and edad <=4:
            p_IdealK = "15"
            p_IdealG = "5"
            t_Ideal = "99"
        if edad >4 and edad<=5:
            p_IdealK = "17"
            p_IdealG = "4"
            t_Ideal = "105"

    asignarClase(id,pesoK,p_IdealK,pesoG,p_IdealG,talla,t_Ideal,'fuera_rango')

    c = Controles.objects.get(id=id)
    c.peso_idealK = p_IdealK
    c.peso_idealG = p_IdealG
    c.talla_ideal = t_Ideal
    c.save()


############## FUNCION ASIGNAR CLASE CUANDO EL PESO ESTA FUERA DE RANGO  #######################

def asignarClase(id,pesoK,p_IdealK,pesoG,p_IdealG,talla,t_Ideal,clase):

    c_talla = ""
    c_peso = ""

    if pesoK < p_IdealK:
        c_peso = clase

    if pesoG < p_IdealG:
        c_peso = clase

    if pesoK > p_IdealK:
        c_peso = clase

    if pesoG > p_IdealG:
        c_peso = clase

    if talla < t_Ideal:
        c_talla = clase

    if talla > t_Ideal:
        c_talla = clase

    c = Controles.objects.get(id=id)
    c.clase_peso = c_peso
    c.clase_talla = c_talla
    c.save()

############## FUNCION GENERAR PDF MEDIDAS ANTROPOMETRICAS ######################

@login_required(login_url="login:login")
def MedidasAntropometricasPDF(request, id=None):
    try:
        logo = "icbf-reporte.png"
        beneficiario = Beneficiario.objects.get(id = id)
        if beneficiario.tipo_beneficiario == "1":
            tipo = 'Niño'
        else:
            tipo = 'Niña'
        controles = Controles.objects.filter(beneficiario=id).order_by("fecha_control")
        result = StringIO()
        html= render_to_string("reportes/medidas_antropometricas_pdf.html",{"url": URL, "logo": logo, "beneficiario": beneficiario , "controles": controles, "tipo": tipo, "titulo": "MEDIDAS ANTROPOMETRICAS" })
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
