from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   url('^guardarComposicionFamiliar$', views.guardarComposicionFamiliar, name = 'guardarComposicionFamiliar'),
   url('^traerFamiliar/(?P<id>\d+)$', views.traerFamiliar, name = 'traerFamiliar'),
   url('^guardarCabeza_Nucleo$', views.guardarCabeza_Nucleo, name = 'guardarCabeza_Nucleo'),
] 
