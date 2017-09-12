#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User
from parametrizacion.models import *
from beneficiarios.models import Beneficiario


class Salud(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=False ,blank=False)
    f1 = models.CharField( max_length=2, null=False ,blank=False)
    #F2. El niño o niña es beneficiario del régimen
    f2 =models.CharField( max_length=2,  null=False ,blank=True)
    #F3. Nombre de la Entidad Promotora de Salud a la que se encuentra afiliado
    f3 = models.ForeignKey(EPS, null=True ,blank=True)
    #Semana de gestación en la que ocurrio el parto (Nacimiento)
    semana_nacimiento = models.CharField( max_length=4,  null=False ,blank=True)
    tipo_parto = models.CharField( max_length=2,  null=False ,blank=True)
    servicio_parto =  models.CharField( max_length=2,  null=False ,blank=True)
    #F4. ¿El niño o niña cuenta con el carnet de vacunación actualizado?
    f4 =  models.CharField( max_length=2, null=False ,blank=True)
    #F5. El niño o niña cuenta con el siguiente esquema de vacunación (Marque con una X aquellas que han sido aplicadas)
    vacunas_1 = models.TextField(null=False ,blank=True)
    vacunas_2 = models.TextField(null=False ,blank=True)
    vacunas_3 = models.TextField(null=False ,blank=True)
    vacunas_4 = models.TextField(null=False ,blank=True)
    vacunas_5 = models.TextField(null=False ,blank=True)
    vacunas_6 = models.TextField(null=False ,blank=True)
    vacunas_7 = models.TextField(null=False ,blank=True)
    vacunas_8 = models.TextField(null=False ,blank=True)
    #F6. En caso de no contar con el Carnet de Vacunación al día según la edad del niño o niña ¿ Cuál ha sido el motivo ?
    f6 = models.TextField(null=False ,blank=True)
    id_f6 = models.TextField(null=False ,blank=True)
    f6_otro = models.CharField(max_length=20, null=False, blank=True)
    #F7. Si el niño o niña es mayor de 1 año ¿ Ha asistido a Controles de Salud Oral ?
    f7 =  models.CharField( max_length=2, null=False ,blank=True)
    #F8. En caso de no contar con el Carnet de Vacunación al día según la edad del niño o niña ¿ Cuál ha sido el motivo ?
    f8 = models.TextField(null=False ,blank=True)
    id_f8 = models.TextField(null=False ,blank=True)
    f8_otro = models.CharField(max_length=20, null=False, blank=True)
    #F9. ¿El niño o niña menor de 4 años ¿ Ha recibido valoración Oftalmológica ?
    f9 =  models.CharField( max_length=2, null=False ,blank=True)
    #F10. ¿El niño o niña menor de 4 años ¿ Ha recibido valoración Auditiva ?
    f10 =  models.CharField( max_length=2, null=False ,blank=True)

    def __str__(self):
        return str(self.beneficiario)
