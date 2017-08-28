#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.template import RequestContext
from django.db import transaction
from django.shortcuts import render, render_to_response
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from icbf.settings import URL, SERVIDOR, GRUPO1, GRUPO2, STATIC_URL,AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID
from parametrizacion.views import registrarLogs
from composicion_familiar.models import Familiar, Cabeza_Nucleo
from beneficiarios.models import Beneficiario
import os
import json

################## FUNCION GUARDAR O ACTUALIZAR COMPOSICIÓN FAMILIAR ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarComposicionFamiliar(request):
    if request.method == 'POST':
        if request.POST['cf_familiar_id'] == "":
            f = Familiar()
            f.beneficiario_id = request.POST['cf_beneficiario']
            f.parentezco_id = request.POST['cf_parentezco']
            f.nombres = request.POST['cf_nombres']
            f.tipo_documento_id = request.POST['cf_tip_doc']
            f.numero_documento = request.POST['cf_documento']
            f.edad = request.POST['cf_edad']
            f.nivel_escolaridad_id = request.POST['cf_escolaridad']
            f.ocupacion_id = request.POST['cf_ocupacion']
            f.sabe_leer = request.POST['cf_sabe_leer']
            f.sabe_escribir = request.POST['cf_sabe_escribir']
            f.estado_laboral_id = request.POST['cf_estado_laboral']
            f.n_dias_labora = request.POST['cf_dias_semana']
            f.n_horas_labora = request.POST['cf_horas']
            f.condiciones_especiales = request.POST['cf_condiciones']
            f.aporta_sustento = request.POST['cf_aporta_sustento']
            f.estado_sgsss = request.POST['cf_estado_eps']
            f.nombre_eps_id = request.POST['cf_eps']
            f.save()
            b = Beneficiario.objects.get(id=request.POST['cf_beneficiario'])
            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Familiar','Guardar Familiar',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
            messages.success(request, 'g_composicion')
        else:
            f = Familiar.objects.get(id=request.POST['cf_familiar_id'])
            f.beneficiario_id = request.POST['cf_beneficiario']
            f.parentezco_id = request.POST['cf_parentezco']
            f.nombres = request.POST['cf_nombres']
            f.tipo_documento_id = request.POST['cf_tip_doc']
            f.numero_documento = request.POST['cf_documento']
            f.edad = request.POST['cf_edad']
            f.nivel_escolaridad_id = request.POST['cf_escolaridad']
            f.ocupacion_id = request.POST['cf_ocupacion']
            f.sabe_leer = request.POST['cf_sabe_leer']
            f.sabe_escribir = request.POST['cf_sabe_escribir']
            f.estado_laboral_id = request.POST['cf_estado_laboral']
            f.n_dias_labora = request.POST['cf_dias_semana']
            f.n_horas_labora = request.POST['cf_horas']
            f.condiciones_especiales = request.POST['cf_condiciones']
            f.aporta_sustento = request.POST['cf_aporta_sustento']
            f.estado_sgsss = request.POST['cf_estado_eps']
            f.nombre_eps_id = request.POST['cf_eps']
            f.save()
            b = Beneficiario.objects.get(id=request.POST['cf_beneficiario'])
            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Familiar','Actualizar Familiar',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
            messages.success(request, 'a_composicion')
        return HttpResponseRedirect('/beneficiario/editar/'+str(request.POST['cf_beneficiario']))
    else:
        return HttpResponseRedirect("/")


################## FUNCION TRAER FAMILIAR ######################

@login_required(login_url="/login")
def traerFamiliar(request, id = None):
    try:
        if request.method == 'GET':
            data = Familiar.objects.get(id = id)
            familiar = json.dumps({"id": data.id, "parentezco": data.parentezco_id, "nombres": data.nombres,
                                 "tipo_documento": data.tipo_documento_id,"numero_documento": data.numero_documento,
                                 "edad": data.edad,"nivel_escolaridad": data.nivel_escolaridad_id, "ocupacion": data.ocupacion_id,
                                 "sabe_leer": data.sabe_leer, "sabe_escribir": data.sabe_escribir, "estado_laboral": data.estado_laboral_id,
                                 "n_dias_labora": data.n_dias_labora, "n_horas_labora": data.n_horas_labora, "condiciones_especiales": data.condiciones_especiales,
                                 "aporta_sustento": data.aporta_sustento, "estado_sgsss": data.estado_sgsss, "nombre_eps": data.nombre_eps_id })
            return HttpResponse(familiar, content_type='application/json', status=200)
        else:
            return HttpResponse(status=401)
    except Exception, error:
        print type(error)
        return HttpResponse("Ha ocurrido un error. Descripcion:%s" % (error), status=500)


################## FUNCION GUARDAR O ACTUALIZAR CABEZA DE NUCLEO ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarCabeza_Nucleo(request):
    if request.method == 'POST':
        if request.POST['c_estado'] == "INCOMPLETO":
            c = Cabeza_Nucleo()
            c.beneficiario_id = request.POST['c_ben']
            #C2. Condición especial del padre o madre cabeza de hogar
            c.c2 = request.POST['c2_condicion']
            c.id_c2 = request.POST['id_c2_condicion']
            #C3. ¿Presenta declaración de los hechos de victimización en el marco del conflicto armado ante la personería,
            # Defensoría o Procuraduría?
            c.c3 = request.POST['c3']
            #C4. Pertenece a población prioritaria de:
            c.c4 = request.POST['c4_poblacion']
            c.id_c4 = request.POST['id_c4_poblacion']
            #NUMERO DE FOLIO O PUNTAJE DEL SISBEN
            c.c4_puntaje = request.POST['c4_puntaje']
            c.c4_folio = request.POST['c4_folio']
            #C5. ¿Recibe subsidio de familias en acción?
            c.c5 = request.POST['c5']
            c.c5_beneficio = request.POST['c5_beneficio']
            c.id_c5_beneficio = request.POST['id_c5_beneficio']
            #C6. ¿Se encuentra recibiendo beneficios de otro programa?
            c.c6 = request.POST['c6']
            c.c6_beneficio = request.POST['c6_cual']
            #C7. La mujer cuidadora del niño o niña menor de cinco años se encuentra
            c.c7 = request.POST['c7']
            #C8. En caso de no encontrarse afiliado al Sistema de seguridad social en salud, ¿Cuál es la razón?
            c.c8 = request.POST['c8_razon']
            c.id_c8 = request.POST['id_c8_razon']
            #C9. Dentro de sus metas en un plazo de un año, se proyecta: (Diligenciar solo si la cabeza del núcleo
            #familiar es mayor de 18 años)
            c.c9 = request.POST['c9_metas']
            c.id_c9 = request.POST['id_c9_metas']
            #C10. La cabeza de hogar hace parte de
            c.c10 = request.POST['c10_organizacion']
            c.id_c10 = request.POST['id_c10_organizacion']
            #C11. El padre y la madre de los niños y niñas menores de 5 años, planearon con antelación el embarazo
            c.c11 = request.POST['c11']
            c.save()

            c = Beneficiario.objects.get(id=request.POST['c_ben'])
            c.modulo_c = "COMPLETADO"
            c.save()

            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Cabeza de Nucleo','Guardar Cabeza de Nucleo',c.primer_nombre+" "+c.segundo_nombre+" "+c.primer_apellido+" "+c.segundo_apellido)
        else:
            c = Cabeza_Nucleo.objects.get(beneficiario=request.POST['c_ben'])
            c.beneficiario_id = request.POST['c_ben']
            #C2. Condición especial del padre o madre cabeza de hogar
            c.c2 = request.POST['c2_condicion']
            c.id_c2 = request.POST['id_c2_condicion']
            #C3. ¿Presenta declaración de los hechos de victimización en el marco del conflicto armado ante la personería,
            # Defensoría o Procuraduría?
            c.c3 = request.POST['c3']
            #C4. Pertenece a población prioritaria de:
            c.c4 = request.POST['c4_poblacion']
            c.id_c4 = request.POST['id_c4_poblacion']
            #NUMERO DE FOLIO O PUNTAJE DEL SISBEN
            c.c4_puntaje = request.POST['c4_puntaje']
            c.c4_folio = request.POST['c4_folio']
            #C5. ¿Recibe subsidio de familias en acción?
            c.c5 = request.POST['c5']
            c.c5_beneficio = request.POST['c5_beneficio']
            c.id_c5_beneficio = request.POST['id_c5_beneficio']
            #C6. ¿Se encuentra recibiendo beneficios de otro programa?
            c.c6 = request.POST['c6']
            c.c6_beneficio = request.POST['c6_cual']
            #C7. La mujer cuidadora del niño o niña menor de cinco años se encuentra
            c.c7 = request.POST['c7']
            #C8. En caso de no encontrarse afiliado al Sistema de seguridad social en salud, ¿Cuál es la razón?
            c.c8 = request.POST['c8_razon']
            c.id_c8 = request.POST['id_c8_razon']
            #C9. Dentro de sus metas en un plazo de un año, se proyecta: (Diligenciar solo si la cabeza del núcleo
            #familiar es mayor de 18 años)
            c.c9 = request.POST['c9_metas']
            c.id_c9 = request.POST['id_c9_metas']
            #C10. La cabeza de hogar hace parte de
            c.c10 = request.POST['c10_organizacion']
            c.id_c10 = request.POST['id_c10_organizacion']
            #C11. El padre y la madre de los niños y niñas menores de 5 años, planearon con antelación el embarazo
            c.c11 = request.POST['c11']
            c.save()

            b = Beneficiario.objects.get(id=request.POST['c_ben'])
            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Cabeza de Nucleo','Actualizar Cabeza de Nucleo',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
        messages.success(request, 'Cabeza')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")
