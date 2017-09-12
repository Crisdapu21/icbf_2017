#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
register = template.Library()

@register.filter
def beneficiarios(value,bandera):
    if bandera == "M":
        if  value == 1:
            return (str(value)+" Niño")
        else:
            return (str(value)+" Niños")
    else:
        if  value == 1:
            return (str(value)+" Niña")
        else:
            return (str(value)+" Niñas")

@register.filter
def respuestas(value):
    if value == "S":
        return ("SI")
    else:
        return ("NO")

@register.filter
def tipo_beneficiarios(value):
    if value == "1":
        return ("Niño")
    else:
        return ("Niña")

@register.filter
def generos(value):
    if value == "M":
        return ("Masculino")
    else:
        return ("Femenino")

@register.filter
def edades(value,bandera):
    if bandera == "A":
        if value == 1:
            return (str(value)+" Año")
        else:
            return (str(value)+" Años")
    else:
        if value == 1:
            return (str(value)+" Mes")
        else:
            return (str(value)+" Meses")

@register.filter
def cantidades(value):
    if value != "":
        return ('{:,}'.format(int(value)))
    else:
        return ("")
