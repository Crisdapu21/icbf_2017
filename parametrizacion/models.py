#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

################ OCUPACIONES ##################

class Ocupaciones(models.Model):
    ocupacion = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.ocupacion
    class Meta:
        verbose_name_plural = 'Crear Ocupación'

################ ESTADO LABORAL ##################

class Estado_Laboral(models.Model):
    estado_laboral = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.estado_laboral
    class Meta:
        verbose_name_plural = 'Crear Estados Laborales'

################ TIPO DOCUMENTO ##################

class Tipo_Documento(models.Model):
    tipo = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name_plural = 'Crear Tipos de Documento'

################ EPS ##################

class EPS(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Crear EPS'


class No_EPS(models.Model):
    causa_no_eps = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.causa_no_eps
    class Meta:
        verbose_name_plural = 'Crear Causas que llevan a no tener EPS'


################ METAS PROYECTADAS A LAS CABEZA DE HOGAR ##################

class Metas_Cabeza(models.Model):
    metas = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.metas
    class Meta:
        verbose_name_plural = 'Crear Metas Proyectadas a Cabezas de Hogar'


################ ORGANIZACIONES CIVILES  ##################

class Organizaciones_Civiles(models.Model):
    organizacion = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.organizacion
    class Meta:
        verbose_name_plural = 'Crear Organizaciones Civiles'


############ PARENTEZCO ################

class Parentezco(models.Model):
    parentezco = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.parentezco
    class Meta:
        verbose_name_plural = 'Crear Parentezco'

######### NIVEL DE ESCOLARIDAD ##############

class Nivel_Escolaridad(models.Model):
    nivel_escolaridad = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.nivel_escolaridad
    class Meta:
        verbose_name_plural = 'Crear Nivel de Escolaridad'

################ LOCALIZACION ##################

class Paises(models.Model):
    pais = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.pais
    class Meta:
        verbose_name_plural = 'Crear Pais'

class Departamentos(models.Model):
    pais = models.ForeignKey(Paises)
    departamento = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.departamento
    class Meta:
        verbose_name_plural = 'Crear Departamento'

class Ciudades(models.Model):
    departamento = models.ForeignKey(Departamentos)
    ciudad = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.ciudad
    class Meta:
        verbose_name_plural = 'Crear Ciudades o Municipios'

################ LOGS ##################

class Logs(models.Model):
    usuario = models.TextField(null=False ,blank=False)
    accion = models.TextField(null=False ,blank=False)
    modelo = models.TextField(null=False ,blank=False)
    detalle = models.TextField(null=False ,blank=False)
    referencia = models.TextField(null=False ,blank=False)
    fecha = models.DateField(default=datetime.now, blank=True)
    hora  = models.TimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.modelo
