#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.db import models
from django.contrib.auth.models import User
from beneficiarios.models import Beneficiario
from parametrizacion.models import *

################ RELACIONES COMUNITARIAS  ##################

class Relaciones(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=False ,blank=False)
    #D1. El núcleo familiar se apoya de sus vecinos cuando
    d1 = models.TextField(null=False ,blank=True)
    id_d1 = models.TextField(null=False ,blank=True)
    #D2 ¿El núcleo familiar completo o alguno de sus miembros apoya a sus vecinos cuando lo requieren?
    d2 = models.CharField( max_length=1, null=False ,blank=True)
    #D3. EL núcleo familiar comparte actividades con los vecinos
    d3 = models.TextField(null=False ,blank=True)
    id_d3 = models.TextField(null=False ,blank=True)
    #D4. El núcleo familiar comparte sus dificultades con
    d4 = models.TextField(null=False ,blank=True)
    id_d4 = models.TextField(null=False ,blank=True)
    #D4.2 El núcleo familiar comparte sus acontecimientos especiales con
    d42 = models.TextField(null=False ,blank=True)
    id_d42 = models.TextField(null=False ,blank=True)
    #D5. Cuándo se presentan algunas dificultades con los vecinos el núcleo familiar los resuelve:
    d5 = models.TextField(null=False ,blank=True)
    id_d5 = models.TextField(null=False ,blank=True)
    #D6. La cabeza del núcleo familiar pertenece a algún tipo de organización dentro de su barrio o vereda
    d6 = models.TextField(null=False ,blank=True)
    id_d6 = models.TextField(null=False ,blank=True)
    #D7. Cuál es el mayor talento o capacidad de la cabeza del núcleo familiar para trabajar en grupo o comunitariamente
    d7 = models.TextField(null=False ,blank=True)
    id_d7 = models.TextField(null=False ,blank=True)
    d7_otro = models.CharField(max_length=20, null=False, blank=True)
    #d8. Alguno de los miembros del núcleo familiar desearía pertenecer a alguna organización en su barrio
    d8 = models.CharField( max_length=1, null=False ,blank=True)
    #D9. Cuándo se realizan actividades comunitarias, se comunican a través de
    d9 = models.TextField(null=False ,blank=True)
    id_d9 = models.TextField(null=False ,blank=True)

    def __str__(self):
        return str(self.d1)
    class Meta:
        verbose_name_plural = 'Crear Relaciones Comunitarias'
