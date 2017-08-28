from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from icbf.celery import app
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, EmailMultiAlternatives
from remax.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
import django.conf as conf
from django.db.models import Q
import smtplib
from calendario.models import Eventos, Notificaciones
from calendario.views import guardarNotificacion
from parametrizacion.models import Palabras_clave
from datetime import datetime, timedelta
from django.template import RequestContext
import time

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
        if e.f_fin == time.strftime('%Y-%m-%d'):
            if e.notificacion != "":
                n = Notificaciones.objects.get(id = int(e.notificacion))
                n.f_inicio = e.f_inicio
                n.f_fin = e.f_fin
                n.uds_id = uds
                n.save()
            else:
                guardarNotificacion(e.id,e.uds,e.tipo,e.f_inicio,e.f_fin,e.beneficiario)
        else:
            if e.notificacion != "":
                n = Notificaciones.objects.get(id = int(e.notificacion))
                n.f_inicio = e.f_inicio
                n.f_fin = e.f_fin
                n.uds_id = uds
                n.save()
            else:
                guardarNotificacion(e.id,e.uds,e.tipo,e.f_inicio,e.f_fin,e.beneficiario)
