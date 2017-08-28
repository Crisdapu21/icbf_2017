#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from celery import shared_task,Celery,group
from celery.task import periodic_task
from celery.schedules import crontab
from icbf.celery import app
from calendario.models import Eventos, Notificaciones
from beneficiarios.models import Notas
from calendario.views import guardarNotificacion
from dateutil.relativedelta import relativedelta
from django.db.models import Q
import os,time
import datetime
from datetime import datetime, timedelta

################### FUNCION ACTUALIZAR FECHA EVENTOS #####################

@app.task(name='actualizarFecha')
def actualizarFecha():
    eventos = Eventos.objects.filter(Q(tipo = "TAREAS") & Q(estado = "NO REALIZADA"))
    for e in eventos:
        if  e.f_inicio == time.strftime('%Y-%m-%d') and time.strftime('%H:%M') >= '23:55' and e.bandera == time.strftime('%Y-%m-%d'):
            newFecha = datetime.strptime(e.f_inicio, '%Y-%m-%d')
            newFecha = newFecha + timedelta(days=1)
            newFecha = newFecha.strftime('%Y-%m-%d')
            ev = Eventos.objects.get(id=e.id)
            ev.f_inicio = newFecha
            ev.f_fin = newFecha
            ev.bandera = newFecha
            ev.save()

################### FUNCION ALERTAR FECHA EVENTOS #####################

@app.task(name='alertarFecha')
def alertarFecha():
    eventos = Eventos.objects.all()
    for e in eventos:
        if e.beneficiario != None:
            beneficiario = e.beneficiario.id
            nombre = e.beneficiario.primer_nombre+" "+e.beneficiario.primer_apellido
        else:
            beneficiario = ""
            nombre = ""
        if e.f_fin <= time.strftime('%Y-%m-%d'):
            if e.notificacion != "":
                if e.estado == "REALIZADA":
                    n = Notificaciones.objects.get(id = int(e.notificacion))
                    n.nombre = nombre
                    n.detalle = e.detalle
                    n.f_inicio = e.f_inicio
                    n.f_fin = e.f_fin
                    n.uds_id = e.uds.id
                    n.limite = "SUPERADO"
                    n.save()
                else:
                    n = Notificaciones.objects.get(id = int(e.notificacion))
                    n.nombre = nombre
                    n.detalle = e.detalle
                    n.f_inicio = e.f_inicio
                    n.f_fin = e.f_fin
                    n.uds_id = e.uds.id
                    n.limite = "A TIEMPO"
                    n.save()
            else:
                guardarNotificacion(e.id,e.uds.id,e.tipo,e.f_inicio,e.f_fin,beneficiario,nombre,e.detalle)
        else:
            if e.notificacion != "":
                if e.estado == "REALIZADA":
                    n = Notificaciones.objects.get(id = int(e.notificacion))
                    n.nombre = nombre
                    n.detalle = e.detalle
                    n.f_inicio = e.f_inicio
                    n.f_fin = e.f_fin
                    n.uds_id = e.uds.id
                    n.limite = "SUPERADO"
                    n.save()
                else:
                    n = Notificaciones.objects.get(id = int(e.notificacion))
                    n.nombre = nombre
                    n.detalle = e.detalle
                    n.f_inicio = e.f_inicio
                    n.f_fin = e.f_fin
                    n.uds_id = e.uds.id
                    n.limite = "A TIEMPO"
                    n.save()
            else:
                guardarNotificacion(e.id,e.uds.id,e.tipo,e.f_inicio,e.f_fin,beneficiario,nombre,e.detalle)


@app.task()
def VacunasTask(beneficiario,uds,fecha_nacimiento):
    recien_nacido_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=1) - relativedelta(days=2)
    recien_nacido_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=1)
    meses_2_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=2) - relativedelta(days=2)
    meses_2_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=2)
    meses_4_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=4) - relativedelta(days=2)
    meses_4_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=4)
    meses_6_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=6) - relativedelta(days=2)
    meses_6_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=6)
    meses_7_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=7) - relativedelta(days=2)
    meses_7_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(months=7)
    meses_12_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(years=1) - relativedelta(days=2)
    meses_12_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(years=1)
    meses_18_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(years=1) + relativedelta(months=6) - relativedelta(days=2)
    meses_18_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(years=1) + relativedelta(months=6)
    meses_60_inicia = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(years=5) - relativedelta(days=2)
    meses_60_finaliza = datetime.strptime(fecha_nacimiento, '%Y-%m-%d') + relativedelta(years=5)
    alertaVacuna(beneficiario,uds,"Vacuna Tuberculosis B.C.G",recien_nacido_inicia.strftime('%Y-%m-%d'),recien_nacido_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Hepatitis B",recien_nacido_inicia.strftime('%Y-%m-%d'),recien_nacido_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Polio 1ra Dosis",meses_2_inicia.strftime('%Y-%m-%d'),meses_2_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Pentavalente 1ra Dosis",meses_2_inicia.strftime('%Y-%m-%d'),meses_2_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Rotavirus 1ra Dosis",meses_2_inicia.strftime('%Y-%m-%d'),meses_2_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Neumococo 1ra Dosis",meses_2_inicia.strftime('%Y-%m-%d'),meses_2_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Polio 2da Dosis",meses_4_inicia.strftime('%Y-%m-%d'),meses_4_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Pentalvente 2da Dosis",meses_4_inicia.strftime('%Y-%m-%d'),meses_4_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Rotavirus 2da Dosis",meses_4_inicia.strftime('%Y-%m-%d'),meses_4_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Neumococo 2da Dosis",meses_4_inicia.strftime('%Y-%m-%d'),meses_4_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Polio 3ra Dosis",meses_6_inicia.strftime('%Y-%m-%d'),meses_6_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Pentalvente 3ra Dosis",meses_6_inicia.strftime('%Y-%m-%d'),meses_6_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Influenza 1ra Dosis",meses_6_inicia.strftime('%Y-%m-%d'),meses_6_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Influenza 2da Dosis",meses_7_inicia.strftime('%Y-%m-%d'),meses_7_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Sarampión, Rubeola, Paperas 1ra Dosis",meses_12_inicia.strftime('%Y-%m-%d'),meses_12_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Fibre Amarilla 1ra Dosis",meses_12_inicia.strftime('%Y-%m-%d'),meses_12_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Neumococo Refuerzo",meses_12_inicia.strftime('%Y-%m-%d'),meses_12_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Influenza Anual",meses_12_inicia.strftime('%Y-%m-%d'),meses_12_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Hepatitis A Unica",meses_12_inicia.strftime('%Y-%m-%d'),meses_12_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Difteria, Tosferina, Tetano 1er Refuerzo",meses_18_inicia.strftime('%Y-%m-%d'),meses_18_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Polio 1er Refuerzo",meses_18_inicia.strftime('%Y-%m-%d'),meses_18_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Polio 2do Refuerzo",meses_60_inicia.strftime('%Y-%m-%d'),meses_60_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Difteria, Tosferina, Tetano 2do Refuerzo",meses_60_inicia.strftime('%Y-%m-%d'),meses_60_finaliza.strftime('%Y-%m-%d'))
    alertaVacuna(beneficiario,uds,"Vacuna Sarampeón, Rubeola, Paperas Refuerzo",meses_60_inicia.strftime('%Y-%m-%d'),meses_60_finaliza.strftime('%Y-%m-%d'))

def alertaVacuna(beneficiario,uds,detalle,inicia,finaliza):
    e = Eventos()
    e.beneficiario_id = beneficiario
    e.uds_id = uds
    e.detalle = detalle
    e.f_inicio = inicia
    e.f_fin = finaliza
    e.tipo = "PENDIENTES"
    e.estado = "NO REALIZADA"
    e.allday = "True"
    e.save()
    n = Notas()
    n.nota = "Añadir Evento "+detalle+" a Calendario."
    n.uds = uds
    n.beneficiario_id = beneficiario
    n.save()
    e.nota_id_id = n.id
    e.save()
