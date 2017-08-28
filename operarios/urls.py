from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^perfil$', views.perfil, name = 'perfil'),
    url('^perfil/cambiarPass$', views.cambiar_pass, name = 'cambiar_pass'),
    url('^actualizar_password$', views.actualizar_password, name = 'actualizar_password'),
    url('^operarios$', views.operarios, name = 'operarios'),
    url('^operario/nuevo$', views.crearOperario, name = 'crearOperario' ),
    url('^activarOperario$', views.activarOperario, name = 'activarOperario' ),
    url('^guardarOperario$', views.guardarOperario, name = 'guardarOperario' ),
    url('^operario/editar/(?P<id>\d+)$', views.editarOperario, name='editarOperario'),
    url('^operario/eliminar/(?P<id>\d+)$', views.eliminarOperario, name='eliminarOperario'),
    url('^actualizarOperario$', views.actualizarOperario, name = 'actualizarOperario'),
    url('^verificarEmail', views.verificarEmail, name = 'verificarEmail' ),
]
