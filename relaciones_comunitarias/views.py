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
from relaciones_comunitarias.models import Relaciones
from beneficiarios.models import Beneficiario
import os

################## FUNCION GUARDAR RELACIONES CON LA COMUNIDAD ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarRelaciones(request):
    if request.method == 'POST':
        if request.POST['d_estado'] == "INCOMPLETO":
            r = Relaciones()
            r.beneficiario_id = request.POST['d_ben']
            #D1. El núcleo familiar se apoya de sus vecinos cuando
            r.d1 =  request.POST['d1']
            r.id_d1 =  request.POST['id_d1']
            #D2 ¿El núcleo familiar completo o alguno de sus miembros apoya a sus vecinos cuando lo requieren?
            r.d2 = request.POST['d2']
            #D3. EL núcleo familiar comparte actividades con los vecinos
            r.d3 = request.POST['d3']
            r.id_d3 = request.POST['id_d3']
            #D4. El núcleo familiar comparte sus dificultades con
            r.d4 = request.POST['d4']
            r.id_d4 = request.POST['id_d4']
            #D4.2 El núcleo familiar comparte sus acontecimientos especiales con
            r.d42 = request.POST['d42']
            r.id_d42 = request.POST['id_d42']
            #D5. Cuándo se presentan algunas dificultades con los vecinos el núcleo familiar los resuelve:
            r.d5 = request.POST['d5']
            r.id_d5 = request.POST['id_d5']
            #D6. La cabeza del núcleo familiar pertenece a algún tipo de organización dentro de su barrio o vereda
            r.d6 = request.POST['d6']
            r.id_d6 = request.POST['id_d6']
            #D7. Cuál es el mayor talento o capacidad de la cabeza del núcleo familiar para trabajar en grupo o comunitariamente
            r.d7 = request.POST['d7']
            r.id_d7 = request.POST['id_d7']
            r.d7_otro = request.POST['d7_otro']
            #d8. Alguno de los miembros del núcleo familiar desearía pertenecer a alguna organización en su barrio
            r.d8 = request.POST['d8']
            #D9. Cuándo se realizan actividades comunitarias, se comunican a través de
            r.d9 = request.POST['d9']
            r.id_d9 = request.POST['id_d9']
            r.save()

            d = Beneficiario.objects.get(id=request.POST['d_ben'])
            d.modulo_d = "COMPLETADO"
            d.save()
            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Relaciones Comunitarias','Relaciones Comunitarias Creadas Exitosamente.',d.primer_nombre+" "+d.segundo_nombre+" "+d.primer_apellido+" "+d.segundo_apellido)
        else:
            r = Relaciones.objects.get(beneficiario = request.POST['d_ben'])
            #D1. El núcleo familiar se apoya de sus vecinos cuando
            r.d1 =  request.POST['d1']
            r.id_d1 =  request.POST['id_d1']
            #D2 ¿El núcleo familiar completo o alguno de sus miembros apoya a sus vecinos cuando lo requieren?
            r.d2 = request.POST['d2']
            #D3. EL núcleo familiar comparte actividades con los vecinos
            r.d3 = request.POST['d3']
            r.id_d3 = request.POST['id_d3']
            #D4. El núcleo familiar comparte sus dificultades con
            r.d4 = request.POST['d4']
            r.id_d4 = request.POST['id_d4']
            #D4.2 El núcleo familiar comparte sus acontecimientos especiales con
            r.d42 = request.POST['d42']
            r.id_d42 = request.POST['id_d42']
            #D5. Cuándo se presentan algunas dificultades con los vecinos el núcleo familiar los resuelve:
            r.d5 = request.POST['d5']
            r.id_d5 = request.POST['id_d5']
            #D6. La cabeza del núcleo familiar pertenece a algún tipo de organización dentro de su barrio o vereda
            r.d6 = request.POST['d6']
            r.id_d6 = request.POST['id_d6']
            #D7. Cuál es el mayor talento o capacidad de la cabeza del núcleo familiar para trabajar en grupo o comunitariamente
            r.d7 = request.POST['d7']
            r.id_d7 = request.POST['id_d7']
            r.d7_otro = request.POST['d7_otro']
            #d8. Alguno de los miembros del núcleo familiar desearía pertenecer a alguna organización en su barrio
            r.d8 = request.POST['d8']
            #D9. Cuándo se realizan actividades comunitarias, se comunican a través de
            r.d9 = request.POST['d9']
            r.id_d9 = request.POST['id_d9']
            r.save()

            d = Beneficiario.objects.get(id= request.POST['d_ben'])
            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Relaciones Comunitarias','Relaciones Comunitarias Creadas Exitosamente.',d.primer_nombre+" "+d.segundo_nombre+" "+d.primer_apellido+" "+d.segundo_apellido)
        messages.success(request, 'Relaciones')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")
