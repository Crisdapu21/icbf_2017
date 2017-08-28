#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User
from parametrizacion.models import *
from beneficiarios.models import Beneficiario

################ VIVIENDA ##################

class Tipo_Vivienda(models.Model):
    tipo_vivienda = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.tipo_vivienda
    class Meta:
        verbose_name_plural = 'Crear Tipos de Vivienda'

class Tipo_Tenencia_Vivienda(models.Model):
    tipo_tenencia_vivienda = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.tipo_tenencia_vivienda
    class Meta:
        verbose_name_plural = 'Crear Tipos de Tenencia de Vivienda'

class Tipo_Cama(models.Model):
    tipo_cama = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.tipo_cama
    class Meta:
        verbose_name_plural = 'Crear Tipos de Cama'

class Servicios_Domiciliarios(models.Model):
    tipo_servicio = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.tipo_servicio
    class Meta:
        verbose_name_plural = 'Crear Tipos de Servicio Domiciliario'

class Fuente_Agua_Consumible(models.Model):
    fuente_agua_consumible = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.fuente_agua_consumible
    class Meta:
        verbose_name_plural = 'Crear Fuentes de Agua Consumible'

class Periodo_Agua(models.Model):
    periodo_servicio_agua = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.periodo_servicio_agua
    class Meta:
        verbose_name_plural = 'Crear Peridiocidad del Agua'

class Uso_Agua(models.Model):
    uso_agua = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.uso_agua
    class Meta:
        verbose_name_plural = 'Crear Formas de uso del Agua'

class Tratamiento_Basuras(models.Model):
    tratamiento_basuras = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.tratamiento_basuras
    class Meta:
        verbose_name_plural = 'Crear Tipos de Tatamiento de Basuras'

class Tipo_Sanitario(models.Model):
    tipo_sanitario = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.tipo_sanitario
    class Meta:
        verbose_name_plural = 'Crear Tipos de Sanitarios'

class Servicios_Comunitarios(models.Model):
    servicio = models.CharField(max_length=80, blank=False)
    def __str__(self):
        return self.servicio
    class Meta:
        verbose_name_plural = 'Crear Servicios Comunitarios'


class CaracteristicasVivienda(models.Model):
    beneficiario = models.ForeignKey(Beneficiario,null=False ,blank=False)
    pais = models.ForeignKey(Paises,null=True ,blank=True)
    departamento = models.ForeignKey(Departamentos,null=True ,blank=True)
    ciudad = models.ForeignKey(Ciudades,null=True ,blank=True)
    zona_ubicacion =  models.CharField( max_length=2, null=False ,blank=False)
    nombre_corregimiento = models.TextField(null=False ,blank=True)
    nombre_barrio = models.TextField(null=False ,blank=True)
    direccion_vivienda = models.TextField(null=False ,blank=True)
    tipo_vivienda = models.ForeignKey(Tipo_Vivienda,null=True ,blank=True)
    tipo_tenencia = models.ForeignKey(Tipo_Tenencia_Vivienda,null=True ,blank=True)
    tiempo_anios = models.CharField(max_length=2, null=True ,blank=True)
    tiempo_meses = models.CharField(max_length=2, null=True ,blank=True)
    #b10 . Número de personas que conforman el núcleo familiar y conviven en la misma vivienda.
    b10 = models.CharField(max_length=2, null=True ,blank=True)
    #B11. Excluyendo la sala y el comedor de cuantos cuartos dispone el núcleo familiar del beneficiario para que duerman los niños y/o niñas menores de 5 años
    b11 = models.CharField( max_length=2,blank=True)
    #B12. Los niños y niñas duermen con adultos en la misma habitación SI NO
    b12 = models.CharField( max_length=2, null=False ,blank=False)
    #B13. Los niños y niñas duermen con adultos en la misma cama SI NO
    b13 = models.CharField( max_length=2, null=False ,blank=False)
    #B14. La vivienda cuenta con espacios independientes para dormitorio, cocina y baños (Verificación a través de visita domiciliaria) SI NO
    b14 = models.CharField( max_length=2, null=False ,blank=False)
    #B15. La vivienda cuenta con espacios aseados (Verificación a través de visita domiciliaria)
    b15 = models.CharField( max_length=2, null=False ,blank=False)
    #B16. En el núcleo familiar del beneficiario los niños o niñas menores de 5 años duermen en (Solo una opción) (Verificación a través de visita domiciliaria
    b16 = models.ForeignKey(Tipo_Cama,null=True ,blank=True)
    b16_otro = models.TextField(null=False ,blank=True)
    #B17. El núcleo familiar del beneficiario tiene acceso a los siguientes servicios domiciliarios (Opciones multiples
    b17_codigo = models.TextField(null=False ,blank=True)
    b17_nombre = models.TextField(null=False ,blank=True)
    #B18. El agua que consumen y utilizan para la preparación de los alimentos la obtienen de (Verificación a través de visita domiciliaria)
    b18 = models.ForeignKey(Fuente_Agua_Consumible,null=True ,blank=True)
    #B19 El núcleo familiar recibe el servicio de agua (Verificación a través de visita domiciliaria)
    b19 = models.ForeignKey(Periodo_Agua,null=True ,blank=True)
    b19_otro = models.TextField(null=False ,blank=True)
    #B20. En el hogar el agua la usan: (Verificación a través de visita domiciliaria)
    b20 =  models.ForeignKey(Uso_Agua,null=True ,blank=True)
    #B21. ¿Cuál es el tratamiento que le dan a las basuras? (Verificación a través de visita domiciliaria)
    b21 = models.ForeignKey(Tratamiento_Basuras,null=True ,blank=True)
    #¿Con qué tipo de sanitario cuenta el hogar? (Verificación a través de visita domiciliaria)
    b22 = models.ForeignKey(Tipo_Sanitario,null=True ,blank=True)
    #B23. El sanitario es de uso:
    b23 = models.CharField( max_length=2, null=False ,blank=False)
    #B24. Cerca de la vivienda se cuenta con
    b24_codigo = models.TextField(null=False,blank=True)
    b24_nombre = models.TextField(null=False,blank=True)

    def __str__(self):
        return str(self.beneficiario)
    class Meta:
        verbose_name_plural = 'Crear Caracteristicas de Vivienda'
