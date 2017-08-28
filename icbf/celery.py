#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import Celery,group
import os
import datetime
from celery.schedules import crontab
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icbf.settings')
CELERY_ACCEPT_CONTENT = ['json']
app = Celery('CeleryApp')
app.conf.update(
    BROKER_URL = 'django://',
    CELERYBEAT_SCHEDULE={
        'alertarFechaEventos': {
            'task': 'alertarFecha',
            'schedule': timedelta(seconds=20),
        },
        'actualizarFechaEventos': {
            'task': 'actualizarFecha',
            'schedule': timedelta(minutes=1, seconds = 30),
        },
    },
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
