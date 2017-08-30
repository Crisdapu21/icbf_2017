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
from parametrizacion.views import registrarLogs
from parametrizacion.models import  Paises,Departamentos,Ciudades
from caracteristicas_vivienda.models import CaracteristicasVivienda
from beneficiarios.models import Beneficiario
import json, os

################## FUNCION GUARDAR O ACTUALIZAR CARACTERISTICAS DE VIVIENDA ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarCaracteristicas(request):
    if request.method == 'POST':
        if request.POST['b_estado'] == "INCOMPLETO":
            c = CaracteristicasVivienda()
            c.beneficiario_id = request.POST['b_ben']
            c.pais_id = request.POST['pais_re']
            c.departamento_id = request.POST['departamento_re']
            c.ciudad_id = request.POST['ciudad_re']
            c.zona_ubicacion = request.POST['z_ubicacion']
            c.nombre_corregimiento = request.POST['nom_corregimiento']
            c.nombre_barrio = request.POST['nom_barrio']
            c.direccion_vivienda = request.POST['dir_vivienda']
            c.tipo_vivienda_id = request.POST['tip_vivienda']
            c.tipo_tenencia_id = request.POST['tip_tenencia']
            c.tiempo_anios = request.POST['tiempo_anios']
            c.tiempo_meses = request.POST['tiempo_meses']
            #b10 . Número de personas que conforman el núcleo familiar y conviven en la misma vivienda.
            c.b10 = request.POST['b10']
            #B11. Excluyendo la sala y el comedor de cuantos cuartos dispone el núcleo familiar del beneficiario para que duerman los niños y/o niñas menores de 5 años
            c.b11 = request.POST['b11']
            #B12. Los niños y niñas duermen con adultos en la misma habitación SI NO
            c.b12 = request.POST['b12']
            #B13. Los niños y niñas duermen con adultos en la misma cama SI NO
            c.b13 = request.POST['b13']
            #B14. La vivienda cuenta con espacios independientes para dormitorio, cocina y baños (Verificación a través de visita domiciliaria) SI NO
            c.b14 = request.POST['b14']
            #B15. La vivienda cuenta con espacios aseados (Verificación a través de visita domiciliaria)
            c.b15 = request.POST['b15']
            #B16. En el núcleo familiar del beneficiario los niños o niñas menores de 5 años duermen en (Solo una opción) (Verificación a través de visita domiciliaria
            c.b16_id = request.POST['b16']
            c.b16_otro = request.POST['b16_otro']
            #B17. El núcleo familiar del beneficiario tiene acceso a los siguientes servicios domiciliarios (Opciones multiples
            c.b17_codigo = request.POST['id_servicios_domiciliarios']
            c.b17_nombre = request.POST['servicios_domiciliarios']
            #B18. El agua que consumen y utilizan para la preparación de los alimentos la obtienen de (Verificación a través de visita domiciliaria)
            c.b18_id = request.POST['b18']
            #B19 El núcleo familiar recibe el servicio de agua (Verificación a través de visita domiciliaria)
            c.b19_id = request.POST['b19']
            c.b19_otro = request.POST['b19_otra']
            #B20. En el hogar el agua la usan: (Verificación a través de visita domiciliaria)
            c.b20_id = request.POST['b20']
            #B21. ¿Cuál es el tratamiento que le dan a las basuras? (Verificación a través de visita domiciliaria)
            c.b21_id = request.POST['b21']
            #¿Con qué tipo de sanitario cuenta el hogar? (Verificación a través de visita domiciliaria)
            c.b22_id = request.POST['b22']
            #B23. El sanitario es de uso:
            c.b23 = request.POST['b23']
            #B24. Cerca de la vivienda se cuenta con
            c.b24_codigo = request.POST['id_servicios_comunitarios']
            c.b24_nombre = request.POST['servicios_comunitarios']
            c.save()

            b = Beneficiario.objects.get(id=request.POST['b_ben'])
            b.modulo_b = "COMPLETADO"
            b.save()

            registrarLogs(request.user.first_name+" "+request.user.last_name,'GUARDAR','Caracteristicas de Vivienda','Caracteristicas de Vivienda Creadas Exitosamente.',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
        else:
            b = Beneficiario.objects.get(id = request.POST['b_ben'])
            c = CaracteristicasVivienda.objects.get(beneficiario=request.POST['b_ben'])
            c.pais_id = request.POST['pais_re']
            c.departamento_id = request.POST['departamento_re']
            c.ciudad_id = request.POST['ciudad_re']
            c.zona_ubicacion = request.POST['z_ubicacion']
            c.nombre_corregimiento = request.POST['nom_corregimiento']
            c.nombre_barrio = request.POST['nom_barrio']
            c.direccion_vivienda = request.POST['dir_vivienda']
            c.tipo_vivienda_id = request.POST['tip_vivienda']
            c.tipo_tenencia_id = request.POST['tip_tenencia']
            c.tiempo_anios = request.POST['tiempo_anios']
            c.tiempo_meses = request.POST['tiempo_meses']
            #b10 . Número de personas que conforman el núcleo familiar y conviven en la misma vivienda.
            c.b10 = request.POST['b10']
            #B11. Excluyendo la sala y el comedor de cuantos cuartos dispone el núcleo familiar del beneficiario para que duerman los niños y/o niñas menores de 5 años
            c.b11 = request.POST['b11']
            #B12. Los niños y niñas duermen con adultos en la misma habitación SI NO
            c.b12 = request.POST['b12']
            #B13. Los niños y niñas duermen con adultos en la misma cama SI NO
            c.b13 = request.POST['b13']
            #B14. La vivienda cuenta con espacios independientes para dormitorio, cocina y baños (Verificación a través de visita domiciliaria) SI NO
            c.b14 = request.POST['b14']
            #B15. La vivienda cuenta con espacios aseados (Verificación a través de visita domiciliaria)
            c.b15 = request.POST['b15']
            #B16. En el núcleo familiar del beneficiario los niños o niñas menores de 5 años duermen en (Solo una opción) (Verificación a través de visita domiciliaria
            c.b16_id = request.POST['b16']
            c.b16_otro = request.POST['b16_otro']
            #B17. El núcleo familiar del beneficiario tiene acceso a los siguientes servicios domiciliarios (Opciones multiples
            c.b17_codigo = request.POST['id_servicios_domiciliarios']
            c.b17_nombre = request.POST['servicios_domiciliarios']
            #B18. El agua que consumen y utilizan para la preparación de los alimentos la obtienen de (Verificación a través de visita domiciliaria)
            c.b18_id = request.POST['b18']
            #B19 El núcleo familiar recibe el servicio de agua (Verificación a través de visita domiciliaria)
            c.b19_id = request.POST['b19']
            c.b19_otro = request.POST['b19_otra']
            #B20. En el hogar el agua la usan: (Verificación a través de visita domiciliaria)
            c.b20_id = request.POST['b20']
            #B21. ¿Cuál es el tratamiento que le dan a las basuras? (Verificación a través de visita domiciliaria)
            c.b21_id = request.POST['b21']
            #¿Con qué tipo de sanitario cuenta el hogar? (Verificación a través de visita domiciliaria)
            c.b22_id = request.POST['b22']
            #B23. El sanitario es de uso:
            c.b23 = request.POST['b23']
            #B24. Cerca de la vivienda se cuenta con
            c.b24_codigo = request.POST['id_servicios_comunitarios']
            c.b24_nombre = request.POST['servicios_comunitarios']
            c.save()

            registrarLogs(request.user.first_name+" "+request.user.last_name,'ACTUALIZAR','Caracteristicas de Vivienda','Caracteristicas de Vivienda Actualizadas Exitosamente.',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
        messages.success(request, 'Caracteristicas')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")
