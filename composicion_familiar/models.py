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

class Familiar(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=False ,blank=False)
    parentezco = models.ForeignKey(Parentezco, null=False ,blank=False)
    nombres = models.TextField(null=False, blank=True)
    tipo_documento = models.ForeignKey(Tipo_Documento, null=True ,blank=True)
    numero_documento = models.CharField( max_length=15,  null=False ,blank=True)
    edad = models.CharField( max_length=2,  null=False ,blank=True)
    nivel_escolaridad = models.ForeignKey(Nivel_Escolaridad, null=True ,blank=True)
    ocupacion = models.ForeignKey(Ocupaciones, null=True ,blank=True)
    sabe_leer = models.CharField( max_length=1, null=False ,blank=False)
    sabe_escribir = models.CharField( max_length=1, null=False ,blank=False)
    estado_laboral = models.ForeignKey(Estado_Laboral, null=True ,blank=True)
    n_dias_labora = models.CharField( max_length=1,null=False ,blank=False)
    n_horas_labora = models.CharField( max_length=1, null=False ,blank=False)
    condiciones_especiales =  models.CharField( max_length=2, null=False ,blank=False)
    aporta_sustento = models.CharField( max_length=1, null=False ,blank=False)
    estado_sgsss = models.CharField(max_length=1, null=False ,blank=False)
    nombre_eps = models.ForeignKey(EPS, null=True ,blank=True)

    def __str__(self):
        return  self.nombres
    class Meta:
        verbose_name_plural = 'Crear Familiar'


################ CABEZA DE NUCLEO ##################

class Cabeza_Nucleo(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=False ,blank=False)
    #C2. Condición especial del padre o madre cabeza de hogar
    c2 = models.TextField(null=False ,blank=True)
    id_c2 = models.TextField(null=False ,blank=True)
    #C3. ¿Presenta declaración de los hechos de victimización en el marco del conflicto armado ante la personería,
    # Defensoría o Procuraduría?
    c3 = models.CharField( max_length=1, null=False ,blank=False)
    #C4. Pertenece a población prioritaria de:
    c4 = models.TextField(null=False ,blank=True)
    id_c4 = models.TextField(null=False ,blank=True)
    #NUMERO DE FOLIO O PUNTAJE DEL SISBEN
    c4_puntaje = models.CharField(max_length=15, null=False, blank=True)
    c4_folio = models.CharField(max_length=15, null=False, blank=True)
    #C5. ¿Recibe subsidio de familias en acción?
    c5 = models.CharField( max_length=1, null=False ,blank=False)
    c5_beneficio =  models.TextField(null=False ,blank=True)
    id_c5_beneficio =  models.TextField(null=False ,blank=True)
    #C6. ¿Se encuentra recibiendo beneficios de otro programa?
    c6 = models.CharField( max_length=1, null=False ,blank=False)
    c6_beneficio = models.CharField( max_length=1, null=False ,blank=False)
    #C7. La mujer cuidadora del niño o niña menor de cinco años se encuentra
    c7 = models.CharField( max_length=1, null=False ,blank=False)
    #C8. En caso de no encontrarse afiliado al Sistema de seguridad social en salud, ¿Cuál es la razón?
    c8 = models.TextField(null=False ,blank=True)
    id_c8 = models.TextField(null=False ,blank=True)
    #C9. Dentro de sus metas en un plazo de un año, se proyecta: (Diligenciar solo si la cabeza del núcleo
    #familiar es mayor de 18 años)
    c9 = models.TextField(null=False ,blank=True)
    id_c9 = models.TextField(null=False ,blank=True)
    #C10. La cabeza de hogar hace parte de
    c10 = models.TextField(null=False ,blank=True)
    id_c10 = models.TextField(null=False ,blank=True)
    #C11. El padre y la madre de los niños y niñas menores de 5 años, planearon con antelación el embarazo
    c11 = models.CharField( max_length=1, null=False ,blank=False)

    def __str__(self):
        return str(self.beneficiario)
    class Meta:
        verbose_name_plural = 'Crear Cabeza de Nucleo'
