from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url('^entidades$', views.entidades, name = 'entidades' ),
    url('^entidades/nueva$', views.crearEntidad, name = 'crearEntidad' ),
    url('^entidades/editar/(?P<id>\d+)$', views.editarEntidad, name = 'editarEntidad' ),
    url('^entidades/eliminar/(?P<id>\d+)$', views.eliminarEntidad, name = 'eliminarEntidad' ),
    url('^guardarEntidad', views.guardarEntidad, name = 'guardarEntidad' ),
    url('^actualizarEntidad', views.actualizarEntidad, name = 'actualizarEntidad' ),
    url('^uds$', views.uds, name = 'uds' ),
    url('^usd/nueva$', views.crearUDS, name = 'crearUDS' ),
    url('^usd/editar/(?P<id>\d+)$', views.editarUDS, name = 'editarUDS' ),
    url('^uds/eliminar/(?P<id>\d+)$', views.eliminarUDS, name = 'eliminarUDS' ),
    url('^guardarUds', views.guardarUDS, name = 'guardarUDS' ),
    url('^actualizarUds', views.actualizarUDS, name = 'actualizarUDS' ),
]
