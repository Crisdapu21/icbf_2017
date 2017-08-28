#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from django.db import models
from django.contrib.auth.models import User
from parametrizacion.models import *

############ ENTIDAD ADMINISTRADORA DEL SERVICIO ############

class Entidad_Administradora(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    tipo_documento = models.ForeignKey(Tipo_Documento, null=False ,blank=False)
    numero_documento = models.CharField( max_length=15,  null=False ,blank=False)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Crear Entidad Administradora'

############ MODALIDADES DE SERVICIO ############

class Modalidades_servicio(models.Model):
    modalidad = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.modalidad
    class Meta:
        verbose_name_plural = 'Crear Modaliades del Servicio'

############## UNIDAD DE SERVICIO ################

class UDS(models.Model):
    entidad = models.ForeignKey(Entidad_Administradora, null=False ,blank=False)
    nombre = models.TextField(null=False, blank=True)
    modalidad = models.ForeignKey(Modalidades_servicio, null=False ,blank=False)
    pais = models.ForeignKey(Paises, null=False ,blank=False)
    departamento = models.ForeignKey(Departamentos, null=False ,blank=False)
    ciudad = models.ForeignKey(Ciudades, null=False ,blank=False)
    direccion = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Crear UDS'
