#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist
import xhtml2pdf.pisa as pisa
from StringIO import StringIO
from django.template.loader import render_to_string
from django.template import RequestContext
from django.db import transaction
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from icbf.settings import URL, SERVIDOR, GRUPO1, GRUPO2, STATIC_URL,AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID
from parametrizacion.models import  *
from beneficiarios.models import Beneficiario, Notas
from relaciones_comunitarias.models import Relaciones
from nutricion.models import Nutricion
from salud.models import Salud
from caracteristicas_vivienda.models import *
from entidad_administradora_servicio.models import *
from login.validators import existInGroup
from composicion_familiar.models import *
from operarios.models import Operario
from calendario.models import Eventos
from parametrizacion.views import registrarLogs
from django.db.models import Q
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from calendario.tasks import VacunasTask
import json, os, boto3, tinys3, time, math


################## FUNCION VERIFICAR DOCUMENTO ######################

@csrf_exempt
@login_required(login_url="login:login")
def verificarDocumento(request):
    if request.method == 'PUT':
        numdoc = request.GET['numdoc'].replace(' ','')
        if Beneficiario.objects.filter(numero_documento=numdoc).exists():
            return HttpResponse("EXISTE", status=200)
        else:
            return HttpResponse("NO EXISTE", status=200)
    else:
        return HttpResponse("SOLICITUD INCORRECTA", status=200)


################## LISTADO BENEFICIARIOS ######################

def beneficiarios(request):
    if existInGroup(request.user.id,GRUPO1) or existInGroup(request.user.id,GRUPO2):
        if existInGroup(request.user.id,GRUPO1):
            beneficiarios = Beneficiario.objects.all()
            return render(request,'beneficiarios/listado_beneficiarios.html',{'beneficiarios': beneficiarios })
        else:
            operario = Operario.objects.get(id=request.user.id)
            beneficiarios = Beneficiario.objects.filter(uds = operario.uds.id)
            return render(request,'beneficiarios/listado_beneficiarios.html',{'beneficiarios': beneficiarios })
    else:
        return HttpResponseRedirect("/")


################## TEMPLATE CREAR BENEFICIRARIO  ######################

@login_required(login_url="login:login")
def crearBeneficiario(request):
    paises = Paises.objects.all()
    unidades_servicio = UDS.objects.all()
    tipos_documentos = Tipo_Documento.objects.all().exclude(tipo = "NIT").exclude(tipo="RUT")
    lugares_expedicion = Ciudades.objects.all()
    miembros = Parentezco.objects.all()
    return render(request,'beneficiarios/nuevo_beneficiario.html',{ 'paises': paises ,'unidades_servicio': unidades_servicio,
                'tipos_documentos': tipos_documentos,'lugares_expedicion': lugares_expedicion,
                'miembros':miembros })

################## FUNCION GUARDAR BENEFICIARIO ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarBeneficiario(request):
    if request.method == 'POST':
        b = Beneficiario()
        b.uds_id = request.POST['uds']
        b.tipo_beneficiario = request.POST['tip_ben']
        b.primer_nombre = request.POST['1nombre']
        b.segundo_nombre = request.POST['2nombre']
        b.primer_apellido = request.POST['1apellido']
        b.segundo_apellido = request.POST['2apellido']
        b.fecha_nacimiento = request.POST['fec_nac']

        if request.POST['bandera_foto'] == "CAMBIO":
            b.foto = request.FILES['archivo']
        else:
            b.foto = "media/beneficiarios/no_photo.png"

        d_fechas = datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.strptime(b.fecha_nacimiento, '%Y-%m-%d')
        b.edad_anios = int(d_fechas.days / 365.2425)
        meses = int(d_fechas.days / 30.4375)

        if meses < 12:
            b.edad_meses = meses
        if meses >=12 and meses <=23.9:
            b.edad_meses = meses - 12
        if meses >=24 and meses <=35.9:
            b.edad_meses = meses - 24
        if meses >=36 and meses <=47.9:
            b.edad_meses = meses - 36
        if meses >=48 and meses <=59.9:
            b.edad_meses = meses - 48
        if meses >=60 and meses <=71.9:
            b.edad_meses = meses - 60

        b.tipo_documento_id = request.POST['tip_doc']
        b.numero_documento = request.POST['numdoc']
        b.fecha_expedicion = request.POST['fec_exp']
        b.lugar_expedicion = request.POST['lug_exp']

        b.genero = request.POST['genero']
        b.pais_id = request.POST['pais_nac']
        b.departamento_id = request.POST['departamento_nac']
        b.ciudad_id = request.POST['ciudad_nac']
        b.grupo_etnico = request.POST['grupo_etnico']
        #A14. Si el núcleo familiar del beneficiario se reconoce como Afrocolombiano o Indígena indique a qué comunidad, resguardo o territorio colectivo pertenece
        b.grupo_perteneciente = request.POST['a14']
        #A15. ¿En la familia se habla la lengua nativa del grupo étnico al que pertenece?
        b.a15 = request.POST['a15']
        #A16. ¿El beneficiario habla la lengua nativa del grupo étnico al que pertenece?
        b.a16 = request.POST['a16']
        #A.17. Datos de contacto del Adulto responsable o acudiente
        b.direccion_acudiente = request.POST['direccion_acu']
        b.telefono_acudiente = request.POST['tel_acu']
        #A.18. Ha sido víctima del desplazamiento forzado u otro hecho victimizante?
        b.a18 = request.POST['a18']
        #¿Algún miembro del grupo familiar con el que convive el beneficiario ha sido víctima del Desplazamiento forzado u otro hecho victimizante?
        b.a19 = request.POST['a19']
        # Señale el tipo de relación del miembro del grupo familiar con el que convive, que ha sido víctima del Desplazamiento u otro hecho victimizante
        b.a20_id = request.POST['a20']
        b.modulo_b = "INCOMPLETO"
        b.modulo_c = "INCOMPLETO"
        b.modulo_d = "INCOMPLETO"
        b.modulo_e = "INCOMPLETO"
        b.modulo_f = "INCOMPLETO"
        b.modulo_g = "INCOMPLETO"
        b.save()

        VacunasTask.delay(b.id,b.uds.id,b.fecha_nacimiento)
        registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Beneficiarios','Beneficiario Creado Exitosamente',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
        messages.success(request, 'Creado')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")


################## TEMPLATE EDITAR BENEFICIARIO ######################

@login_required(login_url="login:login")
def editarBeneficiario(request,id = None):
    url = URL
    paises = Paises.objects.all()
    unidades_servicio = UDS.objects.all()
    tipos_documentos = Tipo_Documento.objects.all().exclude(tipo = "NIT").exclude(tipo="RUT")
    lugares_expedicion = Ciudades.objects.all()
    miembros = Parentezco.objects.all()
    try:
        caracteristicas = CaracteristicasVivienda.objects.get(beneficiario = id)
    except:
        caracteristicas = ""
    try:
        cabeza_nucleo = Cabeza_Nucleo.objects.get(beneficiario = id)
    except:
        cabeza_nucleo = ""
    try:
        relaciones = Relaciones.objects.get(beneficiario = id)
    except:
        relaciones = ""
    try:
        nutricion = Nutricion.objects.get(beneficiario = id)
    except:
        nutricion = ""
    try:
        salud = Salud.objects.get(beneficiario = id)
    except:
        salud = ""
    try:
        factores_riesgo = Factores_Riesgo.objects.get(beneficiario = id)
    except:
        factores_riesgo= ""

    tipos_viviendas = Tipo_Vivienda.objects.all()
    tipos_tenencias = Tipo_Tenencia_Vivienda.objects.all()
    tipos_camas = Tipo_Cama.objects.all()
    servicios_domiciliarios = Servicios_Domiciliarios.objects.all()
    fuentes_agua = Fuente_Agua_Consumible.objects.all()
    periodo_agua  = Periodo_Agua.objects.all()
    usos_aguas = Uso_Agua.objects.all()
    tratamiento_basuras = Tratamiento_Basuras.objects.all()
    tipos_sanitarios = Tipo_Sanitario.objects.all()
    servicios_comunitarios = Servicios_Comunitarios.objects.all()
    nivel_escolaridad = Nivel_Escolaridad.objects.all()
    ocupaciones = Ocupaciones.objects.all()
    estados_laborales = Estado_Laboral.objects.all()
    listado_eps = EPS.objects.all()
    miembros_familia = Familiar.objects.filter(beneficiario = id)
    causas_no_eps = No_EPS.objects.all()
    metas_cabeza = Metas_Cabeza.objects.all()
    organizaciones_civiles = Organizaciones_Civiles.objects.all()
    beneficiario = Beneficiario.objects.get(id = id)
    return render(request,'beneficiarios/editar_beneficiario.html',{'beneficiario': beneficiario,
                'url': url ,'paises': paises,'unidades_servicio': unidades_servicio,
                'tipos_documentos': tipos_documentos,'lugares_expedicion': lugares_expedicion,
                'miembros':miembros,'caracteristicas': caracteristicas,'cabeza_nucleo': cabeza_nucleo,
                'relaciones':relaciones, 'nutricion': nutricion, 'salud': salud, 'factores_riesgo': factores_riesgo,
                'tipos_viviendas':tipos_viviendas,'tipos_tenencias': tipos_tenencias,
                'tipos_camas': tipos_camas , 'servicios_domiciliarios': servicios_domiciliarios,
                'fuentes_agua': fuentes_agua,'periodo_agua': periodo_agua, 'usos_aguas': usos_aguas,
                'tratamiento_basuras': tratamiento_basuras, 'tipos_sanitarios':tipos_sanitarios,
                'servicios_comunitarios': servicios_comunitarios, 'nivel_escolaridad': nivel_escolaridad,
                'ocupaciones': ocupaciones, 'estados_laborales': estados_laborales, 'listado_eps': listado_eps,
                'miembros_familia': miembros_familia, 'causas_no_eps': causas_no_eps, 'metas_cabeza': metas_cabeza,
                'organizaciones_civiles' : organizaciones_civiles })

################## FUNCION ACTUALIZAR BENEFICIARIO ##############

@login_required(login_url="login:login")
def actualizarBeneficiario(request):
    if request.method == 'POST':
        b = Beneficiario.objects.get(id=request.POST['beneficiario_id'])
        d_fechas = datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.strptime(b.fecha_nacimiento, '%Y-%m-%d')
        b.edad_anios = int(d_fechas.days / 365.2425)
        meses = int(d_fechas.days / 30.4375)

        if meses < 12:
            b.edad_meses = meses
        if meses >=12 and meses <=23.9:
            b.edad_meses = meses - 12
        if meses >=24 and meses <=35.9:
            b.edad_meses = meses - 24
        if meses >=36 and meses <=47.9:
            b.edad_meses = meses - 36
        if meses >=48 and meses <=59.9:
            b.edad_meses = meses - 48
        if meses >=60 and meses <=71.9:
            b.edad_meses = meses - 60

        b.grupo_etnico = request.POST['grupo_etnico']
        #A14. Si el núcleo familiar del beneficiario se reconoce como Afrocolombiano o Indígena indique a qué comunidad, resguardo o territorio colectivo pertenece
        b.grupo_perteneciente = request.POST['a14']
        #A15. ¿En la familia se habla la lengua nativa del grupo étnico al que pertenece?
        b.a15 = request.POST['a15']
        #A16. ¿El beneficiario habla la lengua nativa del grupo étnico al que pertenece?
        b.a16 = request.POST['a16']
        #A.17. Datos de contacto del Adulto responsable o acudiente
        b.direccion_acudiente = request.POST['direccion_acu']
        b.telefono_acudiente = request.POST['tel_acu']
        #A.18. Ha sido víctima del desplazamiento forzado u otro hecho victimizante?
        b.a18 = request.POST['a18']
        #¿Algún miembro del grupo familiar con el que convive el beneficiario ha sido víctima del Desplazamiento forzado u otro hecho victimizante?
        b.a19 = request.POST['a19']
        # Señale el tipo de relación del miembro del grupo familiar con el que convive, que ha sido víctima del Desplazamiento u otro hecho victimizante
        b.a20_id = request.POST['a20']

        f_anterior = str(b.foto)
        if request.POST['bandera_foto'] == "CAMBIO":
            b.foto  = request.FILES['archivo']
            if  f_anterior != ("media/beneficiarios/no_photo.png"):
                try:
                    conn = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,tls=True)
                    conn.delete(f_anterior,AWS_STORAGE_BUCKET_NAME)
                except OSError as e:
                    print(e)
        else:
            b.foto = f_anterior

        b.save()
        registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Beneficiarios','Beneficiario Actualizado Exitosamente',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
        messages.success(request, 'Actualizado')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect('/')


################## FUNCION ELIMINAR BENEFICIARIO ######################

@csrf_exempt
@transaction.atomic
@login_required(login_url="login:login")
def eliminarBeneficiario(request, id=None):
  if request.method == 'DELETE':
       s = Salud.objects.filter(beneficiario = id)
       n = Nutricion.objects.filter(beneficiario = id)
       c = Cabeza_Nucleo.objects.filter(beneficiario = id)
       f = Familiar.objects.filter(beneficiario = id)
       v = CaracteristicasVivienda.objects.filter(beneficiario = id)
       b = Beneficiario.objects.filter(id = id)
       try:
         conn = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_STORAGE_BUCKET_NAME,tls=True)
         lista = conn.list('media/beneficiarios/'+str(id), AWS_STORAGE_BUCKET_NAME)
         for fichero in lista:
           conn.delete(fichero['key'])
         conn.delete('media/beneficiarios/'+str(id))
       except OSError as e:
         print(e)
       registrarLogs(request.user.first_name+" "+request.user.last_name,'ELIMINAR','Beneficiarios','Beneficiario Eliminado Exitosamente',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
       s.delete()
       n.delete()
       c.delete()
       f.delete()
       b.delete()
       messages.success(request, 'Borrado')
       return HttpResponse(status=200)
  else:
      return HttpResponseRedirect("/")


############## FUNCION GENERAR PDF DATOS ETNICOS ######################

@login_required(login_url="login:login")
def DatosEtnicosPDF(request, id=None):
    try:
        logo = "icbf-reporte.png"
        beneficiario = Beneficiario.objects.get(id = id)
        if beneficiario.grupo_etnico == '1':
            grupoI = "media/grupos_etnicos/afrocolombiano.jpg"
            grupoN = "Afrocolombiano"
        if beneficiario.grupo_etnico == '2':
            grupoI = "media/grupos_etnicos/indigena.jpg"
            grupoN = "Indigena"
        if beneficiario.grupo_etnico == '3':
            grupoI = "media/grupos_etnicos/gitano.jpg"
            grupoN = "Rrom / Gitano"
        if beneficiario.grupo_etnico == '4':
            grupoI = "media/grupos_etnicos/raizal.jpg"
            grupoN = "Raizal del Archipielago SA"
        if beneficiario.grupo_etnico == '5':
            grupoI = "media/grupos_etnicos/palenquero.jpg"
            grupoN = "Palenquero"
        if beneficiario.grupo_etnico == '6':
            grupoI = "media/grupos_etnicos/no_reconoce.jpg"
            grupoN = "No se Autoreconze"

        result = StringIO()
        html= render_to_string("reportes/datos_etnicos_pdf.html",{"url": URL, "logo": logo, "beneficiario": beneficiario , "grupoI": grupoI, "grupoN": grupoN, "titulo": "DATOS ETNICOS" })
        pdf = pisa.pisaDocument(html,result)
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/")

############## FUNCION GENERAR PDF HECHOS VICTIMIZANTES ######################

@login_required(login_url="login:login")
def HechosVictimizantesPDF(request, id=None):
    try:
        logo = "icbf-reporte.png"
        beneficiario = Beneficiario.objects.get(id = id)
        if beneficiario.a20 != None:
            parentezco = beneficiario.a20
        else:
            parentezco = "Ninguno"
        result = StringIO()
        html= render_to_string("reportes/hechos_victimizantes_pdf.html",{"url": URL, "logo": logo, "beneficiario": beneficiario , "titulo": "HECHOS VICTIMIZANTES", "parentezco": parentezco })
        pdf = pisa.pisaDocument(html,result)
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/")


############## FUNCION GENERAR PDF GENERAL ######################

@login_required(login_url="login:login")
def reporteGeneralPDF(request):
    o = Operario.objects.get(id=request.user.id)
    uds = UDS.objects.get(id=o.uds_id)
    logo = "icbf-reporte.png"

    cantidad_ben = Beneficiario.objects.filter(uds = o.uds).count()
    ninos = Beneficiario.objects.filter(Q(uds = o.uds) & Q(genero = "M")).count()
    ninas = Beneficiario.objects.filter(Q(uds = o.uds) & Q(genero = "F")).count()
    afro = Beneficiario.objects.filter(Q(grupo_etnico = 1) & Q(uds = o.uds)).count()
    indigena = Beneficiario.objects.filter(Q(grupo_etnico = 2) & Q(uds = o.uds)).count()
    gitano = Beneficiario.objects.filter(Q(grupo_etnico = 3) & Q(uds = o.uds)).count()
    raizal = Beneficiario.objects.filter(Q(grupo_etnico = 4) & Q(uds = o.uds)).count()
    palenquero = Beneficiario.objects.filter(Q(grupo_etnico = 5) & Q(uds = o.uds)).count()
    ninguno = Beneficiario.objects.filter(Q(grupo_etnico = 6) & Q(uds = o.uds)).count()
    menor = Beneficiario.objects.filter(Q(uds = o.uds) & Q(edad_anios = 0)).count()
    uno = Beneficiario.objects.filter(Q(uds = o.uds) & Q(edad_anios = 1)).count()
    dos = Beneficiario.objects.filter(Q(uds = o.uds) & Q(edad_anios = 2)).count()
    tres = Beneficiario.objects.filter(Q(uds = o.uds) & Q(edad_anios = 3)).count()
    cuatro = Beneficiario.objects.filter(Q(uds = o.uds) & Q(edad_anios = 4)).count()
    cinco = Beneficiario.objects.filter(Q(uds = o.uds) & Q(edad_anios = 5)).count()
    victimas = Beneficiario.objects.filter(Q(uds = o.uds) & Q(a18 = "S")).count()
    victimas_ninos = Beneficiario.objects.filter(Q(uds = o.uds) & Q(a18 = "S") & Q(genero="M")).count()
    victimas_ninas = Beneficiario.objects.filter(Q(uds = o.uds) & Q(a18 = "S") & Q(genero="F")).count()

    beneficiarios = Beneficiario.objects.filter(uds = o.uds)
    B = []
    BM = []
    BF = []
    for i in beneficiarios:
        B.append(i.id)
        if i.genero == "M":
            BM.append(i.id)
        else:
            BF.append(i.id)

    beneficio = Cabeza_Nucleo.objects.filter(Q(beneficiario__in = B) & Q(c5 = "S")).count()
    beneficio_ninos = Cabeza_Nucleo.objects.filter(Q(beneficiario__in = BM) & Q(c5 = "S")).count()
    beneficio_ninas = Cabeza_Nucleo.objects.filter(Q(beneficiario__in = BF) & Q(c5 = "S")).count()

    servicios = CaracteristicasVivienda.objects.filter(Q(beneficiario__in = B) & Q(b17_nombre__icontains="Energía") & Q(b17_nombre__icontains="Acueducto")).count()
    servicios_ninos = CaracteristicasVivienda.objects.filter(Q(beneficiario__in = BM) & Q(b17_nombre__icontains="Energía") & Q(b17_nombre__icontains="Acueducto")).count()
    servicios_ninas = CaracteristicasVivienda.objects.filter(Q(beneficiario__in = BF) & Q(b17_nombre__icontains="Energía") & Q(b17_nombre__icontains="Acueducto")).count()

    result = StringIO()
    html= render_to_string("reportes/general_pdf.html",{"url": URL, "logo": logo, "titulo": "REPORTE GENERAL UDS", 'uds':uds,
    'cantidad_ben':cantidad_ben, 'ninos':ninos,'ninas':ninas, 'afro':afro,'indigena':indigena,'gitano':gitano,'raizal':raizal,
    'palenquero':palenquero,'ninguno':ninguno,'menor':menor,'uno':uno,'dos':dos,'tres':tres,'cuatro':cuatro,'cinco':cinco,
    'victimas':victimas, 'victimas_ninos': victimas_ninos, 'victimas_ninas':victimas_ninas, 'beneficio':beneficio,
    'beneficio_ninos':beneficio_ninos, 'beneficio_ninas':beneficio_ninas, 'servicios':servicios, 'servicios_ninos': servicios_ninos, 'servicios_ninas':servicios_ninas })
    pdf = pisa.pisaDocument(html,result)
    return HttpResponse(result.getvalue(),content_type='application/pdf')

################### FUNCIÓN GUARDAR NOTA  #######################

@login_required(login_url="login:login")
def guardarNota(request):
    if request.method == 'POST':
        o = Operario.objects.get(id=request.user.id)
        n = Notas()
        n.uds = o.uds.id
        n.beneficiario_id = request.POST['beneficiario_id']
        n.nota = request.POST['notas_detalle']
        n.save()
        messages.success(request, 'Creada')
        return HttpResponseRedirect('/calendario/editar/'+request.POST['pendientes_id'])
    else:
        return HttpResponseRedirect('/')
