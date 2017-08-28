#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from django.db import models
from django.contrib.auth.models import User
from entidad_administradora_servicio.models import UDS

def operario_directory_path(instance, id_id):
    return "media/operarios/"'{0}/{1}'.format(instance.id_id, id_id)

class Operario(models.Model):
    id = models.OneToOneField(User, primary_key=True)
    uds = models.ForeignKey(UDS, null=True,blank=True)
    foto =  models.ImageField(upload_to=operario_directory_path, blank=True)
    genero = models.CharField(max_length=1, null=True ,blank=True)
    direccion = models.CharField(max_length=40, null=True ,blank=True)
    telefono = models.CharField(max_length=15, null=False ,blank=True)
    celular = models.CharField(max_length=10, null=False ,blank=True)
    estado =  models.CharField(max_length=1, null=False ,blank=True)
    intentos =  models.CharField(max_length=1, null=False ,blank=True)

    @property
    def first_name(self):
        return self.id.first_name
    def last_name(self):
        return self.id.last_name
    def username(self):
        return self.id.username
    def email(self):
        return self.id.email
    def last_login(self):
        return self.id.last_login
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = 'Crear Operario'
