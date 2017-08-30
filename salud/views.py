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
from icbf.settings import URL
from salud.models import Salud
from parametrizacion.views import registrarLogs
from beneficiarios.models import Beneficiario
import json

################## FUNCION GUARDAR O ACTUALIZAR SALUD ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarSalud(request):
    if request.method == 'POST':
        if request.POST['f_estado'] == "INCOMPLETO":
            s = Salud()
            s.beneficiario_id = request.POST['f_ben']
            #F1. El niño o niña se encuentra afiliado al Sistema General de seguridad social en salud
            s.f1 =  request.POST['f1']
            #F2. El niño o niña es beneficiario del régimen
            s.f2 =  request.POST['f2']
            #F3. Nombre de la Entidad Promotora de Salud a la que se encuentra afiliado
            s.f3_id =  request.POST['f3']
            #Semana de gestación en la que ocurrio el parto (Nacimiento)
            s.semana_nacimiento =  request.POST['f3_semana']
            s.tipo_parto =  request.POST['f3_parto']
            s.servicio_parto =  request.POST['f3_servicio']
            #F4. ¿El niño o niña cuenta con el carnet de vacunación actualizado?
            s.f4 =   request.POST['f4']
            #F5. El niño o niña cuenta con el siguiente esquema de vacunación (Marque con una X aquellas que han sido aplicadas)
            s.vacunas_1 =  request.POST['vacunas_1']
            s.vacunas_2 =  request.POST['vacunas_2']
            s.vacunas_3 =  request.POST['vacunas_3']
            s.vacunas_4 =  request.POST['vacunas_4']
            s.vacunas_5 =  request.POST['vacunas_5']
            s.vacunas_6 =  request.POST['vacunas_6']
            s.vacunas_7 =  request.POST['vacunas_7']
            s.vacunas_8 =  request.POST['vacunas_8']
            #F6. En caso de no contar con el carnet de vacunación al día según la edad del niño o niña ¿Cuál ha sido el motivo?
            s.f6 = request.POST['f6']
            s.id_f6 = request.POST['id_f6']
            s.f6_otro = request.POST['f6_otro']
            #F7. Si el niño o niña es mayor de 1 año ¿ Ha asistido a Controles de Salud Oral ?
            s.f7 =  request.POST['f7']
            #F8. En caso de no contar con el Carnet de Vacunación al día según la edad del niño o niña ¿ Cuál ha sido el motivo ?
            s.f8 = request.POST['f8']
            s.id_f8 = request.POST['id_f8']
            s.f8_otro = request.POST['f8_otro']
            #F9. ¿El niño o niña menor de 4 años ¿ Ha recibido valoración Oftalmológica ?
            s.f9 =  request.POST['f9']
            #F10. ¿El niño o niña menor de 4 años ¿ Ha recibido valoración Auditiva ?
            s.f10 =  request.POST['f10']
            s.save()

            f = Beneficiario.objects.get(id=request.POST['f_ben'])
            f.modulo_f = "COMPLETADO"
            f.save()
            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Salud','Salud Creada Exitosamente.',f.primer_nombre+" "+f.segundo_nombre+" "+f.primer_apellido+" "+f.segundo_apellido)
        else:
            s = Salud.objects.get(beneficiario=request.POST['f_ben'])
            #F1. El niño o niña se encuentra afiliado al Sistema General de seguridad social en salud
            s.f1 =  request.POST['f1']
            #F2. El niño o niña es beneficiario del régimen
            s.f2 =  request.POST['f2']
            #F3. Nombre de la Entidad Promotora de Salud a la que se encuentra afiliado
            s.f3_id =  request.POST['f3']
            #Semana de gestación en la que ocurrio el parto (Nacimiento)
            s.semana_nacimiento =  request.POST['f3_semana']
            s.tipo_parto =  request.POST['f3_parto']
            s.servicio_parto =  request.POST['f3_servicio']
            #F4. ¿El niño o niña cuenta con el carnet de vacunación actualizado?
            s.f4 =   request.POST['f4']
            #F5. El niño o niña cuenta con el siguiente esquema de vacunación (Marque con una X aquellas que han sido aplicadas)
            s.vacunas_1 =  request.POST['vacunas_1']
            s.vacunas_2 =  request.POST['vacunas_2']
            s.vacunas_3 =  request.POST['vacunas_3']
            s.vacunas_4 =  request.POST['vacunas_4']
            s.vacunas_5 =  request.POST['vacunas_5']
            s.vacunas_6 =  request.POST['vacunas_6']
            s.vacunas_7 =  request.POST['vacunas_7']
            s.vacunas_8 =  request.POST['vacunas_8']
            #F6. En caso de no contar con el carnet de vacunación al día según la edad del niño o niña ¿Cuál ha sido el motivo?
            s.f6 = request.POST['f6']
            s.id_f6 = request.POST['id_f6']
            s.f6_otro = request.POST['f6_otro']
            #F7. Si el niño o niña es mayor de 1 año ¿ Ha asistido a Controles de Salud Oral ?
            s.f7 =  request.POST['f7']
            #F8. En caso de no contar con el Carnet de Vacunación al día según la edad del niño o niña ¿ Cuál ha sido el motivo ?
            s.f8 = request.POST['f8']
            s.id_f8 = request.POST['id_f8']
            s.f8_otro = request.POST['f8_otro']
            #F9. ¿El niño o niña menor de 4 años ¿ Ha recibido valoración Oftalmológica ?
            s.f9 =  request.POST['f9']
            #F10. ¿El niño o niña menor de 4 años ¿ Ha recibido valoración Auditiva ?
            s.f10 =  request.POST['f10']
            s.save()

            f = Beneficiario.objects.get(id=request.POST['f_ben'])
            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Salud','Salud Actualizada Exitosamente.',f.primer_nombre+" "+f.segundo_nombre+" "+f.primer_apellido+" "+f.segundo_apellido)
        messages.success(request, 'Salud')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")
