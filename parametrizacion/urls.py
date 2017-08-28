from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url('^ajaxDepartamentos$', views.ajaxDepartamentos, name = 'ajaxDepartamentos' ),
    url('^ajaxCiudades$', views.ajaxCiudades, name = 'ajaxCiudades' ),
    url('^logs$', views.listadoLogs, name = 'listadoLogs' )
]
