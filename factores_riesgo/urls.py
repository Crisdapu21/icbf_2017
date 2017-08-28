from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   url('^contactos$', views.contactos, name = 'contactos' ),
   url('^mantenimientos/tiposContactos$', views.tiposContactos, name = 'tiposContactos' ),
   url('^mantenimientos/tiposContactos/nuevo$', views.creartipoContacto, name = 'creartipoContacto' ),
   url('^mantenimientos/tiposContactos/editar/(?P<id>\d+)$', views.editartipoContacto, name = 'editartipoContacto' ),
   url('^mantenimientos/tiposContactos/eliminar/(?P<id>\d+)$', views.eliminartipoContacto, name = 'eliminartipoContacto' ),
   url('^guardartipoContacto', views.guardartipoContacto, name = 'guardartipoContacto' ),
   url('^actualizartipoContacto', views.actualizartipoContacto, name = 'actualizartipoContacto' ),
   url('^contactos/nuevo$', views.crearContacto, name = 'crearContacto' ),
   url('^guardarContacto$', views.guardarContacto, name = 'guardarContacto' ),
   url('^importarContactos$', views.importarContactos, name = 'importarContactos' ),
   url('^editarContactos$', views.editarContactos, name = 'editarContactos' ),
   url('^eliminarContactos$', views.eliminarContactos, name = 'eliminarContactos' ),
   url('^actualizarContacto', views.actualizarContacto, name = 'actualizarContacto' ),
   url('^contacto/editar/(?P<id>\d+)$', views.editarContacto, name='editarContacto'),
   url('^contacto/eliminar/(?P<id>\d+)$', views.eliminarContacto, name='eliminarContacto'),
   url('^contacto/reporte/(?P<id>\d+)$', views.reporteContacto, name = 'reporteContacto' ),
   url('^contacto/reporte/pdf/(?P<id>\d+)$', views.ContactoPDF, name = 'ContactoPDF'),
   url('^uploads/', views.upload_file, name="upload_file"),
   url('^notas/nueva/(?P<id>\d+)$', views.crearNota, name = 'crearNota' ),
   url('^guardarNota$', views.guardarNota, name = 'guardarNota' ),
   url('^mantenimientos/uploads/formatoContactos$', views.importarExcel, name = 'importarExcel' )
]
