#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from entidad_administradora_servicio.models import UDS
from beneficiarios.models import Beneficiario,Notas

class Eventos(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=True,blank=True)
    uds = models.ForeignKey(UDS, null=True,blank=True)
    detalle = models.TextField(null=False, blank=True)
    f_inicio  = models.CharField(max_length=10, null=True ,blank=True)
    f_fin  = models.CharField(max_length=10, null=True ,blank=True)
    allday = models.CharField(max_length=5, null=True ,blank=True)
    tipo = models.CharField(max_length=20, null=True ,blank=True)
    estado = models.CharField(max_length=20, null=True ,blank=True)
    nota_id = models.ForeignKey(Notas, null=True ,blank=True )
    notificacion = models.TextField(null=False, blank=True)
    bandera = models.CharField(max_length=10, null=True ,blank=True)

    def __str__(self):
        return  self.detalle
    class Meta:
        verbose_name_plural = 'Crear Eventos'

class Notificaciones(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=True,blank=True)
    nombre = models.TextField(null=False, blank=True)
    detalle = models.TextField(null=False, blank=True)
    uds = models.ForeignKey(UDS, null=True,blank=True)
    tipo = models.CharField(max_length=20, null=True ,blank=True)
    f_inicio = models.CharField(max_length=10, null=True ,blank=True)
    f_fin = models.CharField(max_length=10, null=True ,blank=True)
    limite = models.TextField(null=False, blank=True)
