from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url('^calendario$', views.calendario, name = 'calendario'),
    url('^calendario/editar/(?P<id>\d+)$', views.editarEvento, name='editarEvento'),
    url('^eliminarEvento/(?P<id>\d+)$', views.eliminarEvento, name='eliminarEvento'),
    url('^guardarTareas$', views.guardarTareas, name = 'guardarTareas'),
    url('^guardarPendientes$', views.guardarPendientes, name = 'guardarPendientes'),
    url('^actualizarTarea$', views.actualizarTareas, name='actualizarTareas'),
    url('^actualizarPendiente$', views.actualizarPendientes, name='actualizarPendientes'),
    url('^getNotifications$', views.getNotifications, name='getNotifications')
]
