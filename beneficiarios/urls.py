from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^beneficiarios$', views.beneficiarios, name='beneficiarios'),
    url('^beneficiario/nuevo$', views.crearBeneficiario, name='crearBeneficiario'),
    url('^guardarBeneficiario$', views.guardarBeneficiario, name='guardarBeneficiario'),
    url('^beneficiario/editar/(?P<id>\d+)$', views.editarBeneficiario, name='editarBeneficiario'),
    url('^actualizarBeneficiario$', views.actualizarBeneficiario, name='actualizarBeneficiario'),
    url('^beneficiario/eliminar/(?P<id>\d+)$', views.eliminarBeneficiario, name='eliminarBeneficiario'),
    url('^beneficiarios/datos_etnicos/(?P<id>\d+)/reporte$', views.DatosEtnicosPDF, name = 'DatosEtnicosPDF'),
    url('^beneficiarios/hechos_victimizantes/(?P<id>\d+)/reporte$', views.HechosVictimizantesPDF, name = 'HechosVictimizantesPDF'),
    url('^guardarNota$', views.guardarNota, name = 'guardarNota'),
    url('^verificarDocumento', views.verificarDocumento, name = 'verificarDocumento' ),
]
