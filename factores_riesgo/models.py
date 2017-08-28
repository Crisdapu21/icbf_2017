#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from beneficiarios.models import Beneficiario
from parametrizacion.models import *


################ FAMILIAR ##################

class Factores_Riesgo(models.Model):
    #G1. Condición especial del niño o niña
    g1 = models.TextField(null=False ,blank=True)
    g1_otro = nombres = models.CharField(max_length=60, null=False, blank=True)



    beneficiario = models.ForeignKey(Beneficiario, null=False ,blank=True)
    parentezco = models.ForeignKey(Parentezco, null=False ,blank=True)
    nombres = models.TextField(null=False, blank=True)
    tipo_documento = models.ForeignKey(Tipo_Documento, null=False ,blank=False)
    numero_documento = models.CharField( max_length=15,  null=False ,blank=False)
    edad = models.CharField( max_length=2,  null=False ,blank=False)
    nivel_escolaridad = models.ForeignKey(Nivel_Escolaridad, null=False ,blank=True)
    ocupacion = models.ForeignKey(Ocupaciones, null=False ,blank=True)
    sabe_leer = models.CharField( max_length=1, choices = respuesta,blank=True)
    sabe_escribir = models.CharField( max_length=1, choices = respuesta,blank=True)
    estado_laboral = models.ForeignKey(Estado_Laboral, null=False ,blank=True)
    n_dias_labora = models.CharField( max_length=1, choices = dias, blank=True)
    n_horas_labora = models.CharField( max_length=1, choices = horas, blank=True)
    condiciones_especiales =  models.CharField( max_length=2, choices = condicion_especial, blank=True)
    aporta_sustento = models.CharField( max_length=1, choices = respuesta, blank=True)
    estado_sgsss = models.CharField(max_length=1, choices = estado_eps, blank=True )
    nombre_eps = models.ForeignKey(EPS, null=False ,blank=True)

    def __str__(self):
        return  self.nombres
    class Meta:
        verbose_name_plural = 'Crear Familiar'


################ CABEZA DE NUCLEO ##################

class Cabeza_Nucleo(models.Model):
    familiar = models.ForeignKey(Familiar, null=False ,blank=False)
    #C2. Condición especial del padre o madre cabeza de hogar
    c2 = models.CharField( max_length=1, choices = condicion_especial)
    #C3. ¿Presenta declaración de los hechos de victimización en el marco del conflicto armado ante la personería,
    # Defensoría o Procuraduría?
    c3 = models.CharField( max_length=1, choices = respuesta)
    #C4. Pertenece a población prioritaria de:
    c4 = models.CharField( max_length=1, choices = poblacion_prioritaria)
    #NUMERO DE FOLIO O PUNTAJE DEL SISBEN
    referencia = models.CharField(max_length=20, null=False, blank=False)
    #C5. ¿Recibe subsidio de familias en acción?
    c5 = models.CharField( max_length=1, choices = respuesta)
    c5_beneficio = models.CharField( max_length=1, choices = beneficio_familias_accion)
    #C6. ¿Se encuentra recibiendo beneficios de otro programa?
    c6 = models.CharField( max_length=1, choices = respuesta)
    c6_beneficio = models.CharField( max_length=1, choices = beneficio_programa)
    #C7. La mujer cuidadora del niño o niña menor de cinco años se encuentra
    c7 = models.CharField( max_length=1, choices = estado_madre)
    #C8. En caso de no encontrarse afiliado al Sistema de seguridad social en salud, ¿Cuál es la razón?
    c8 = models.ForeignKey(No_EPS, null=False ,blank=False)
    #C9. Dentro de sus metas en un plazo de un año, se proyecta: (Diligenciar solo si la cabeza del núcleo
    #familiar es mayor de 18 años)
    c9 = models.ForeignKey(Metas_Cabeza, null=False ,blank=False)
    #C10. La cabeza de hogar hace parte de
    c10 = models.ForeignKey(Organizaciones_Civiles, null=False ,blank=False)
    #C11. El padre y la madre de los niños y niñas menores de 5 años, planearon con antelación el embarazo
    c11 = models.CharField( max_length=1, choices = respuesta)
    #D1. El núcleo familiar se apoya de sus vecinos cuando
    d1 = models.CharField( max_length=1, choices = apoyo_vecinos)
    #D2 ¿El núcleo familiar completo o alguno de sus miembros apoya a sus vecinos cuando lo requieren?
    d2 = models.CharField( max_length=1, choices = respuesta)
    #D3. EL núcleo familiar comparte actividades con los vecinos
    d3 = models.CharField( max_length=1, choices = comparte_vecinos)
    #D4. El núcleo familiar comparte sus dificultades con
    d4 = models.CharField( max_length=1, choices = comparte_situaciones)
    #D4.2 El núcleo familiar comparte sus acontecimientos especiales con
    d4n2 = models.CharField( max_length=1, choices = comparte_situaciones)
    #D5. Cuándo se presentan algunas dificultades con los vecinos el núcleo familiar los resuelve:
    d5 = models.CharField( max_length=2, choices = solucion_conflictos)
    d5_otro = models.CharField(max_length=20, null=True, blank=True)
    #D6. La cabeza del núcleo familiar pertenece a algún tipo de organización dentro de su barrio o vereda
    d6 = models.CharField( max_length=2, choices = organizacion_barrio)
    #D7. Cuál es el mayor talento o capacidad de la cabeza del núcleo familiar para trabajar en grupo o comunitariamente
    d7 = models.CharField( max_length=2, choices = talentos)
    d7_otro = models.CharField(max_length=20, null=True, blank=True)
    #d8. Alguno de los miembros del núcleo familiar desearía pertenecer a alguna organización en su barrio
    d8 = models.CharField( max_length=1, choices = respuesta)
    #D9. Cuándo se realizan actividades comunitarias, se comunican a través de
    d9 = models.CharField( max_length=1, choices = difusion_comunitaria)
    d9_otro = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.familiar)
    class Meta:
        verbose_name_plural = 'Crear Cabeza de Nucleo'
