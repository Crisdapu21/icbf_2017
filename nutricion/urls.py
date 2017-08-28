from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^beneficiarios/medidas_antropometricas/(?P<id>\d+)$', views.medidasAntropometricas, name = 'medidasAntropometricas'),
    url('^beneficiarios/medidas_antropometricas/(?P<id>\d+)/reporte$', views.MedidasAntropometricasPDF, name = 'MedidasAntropometricasPDF'),
    url('^beneficiarios/enfermedades/(?P<id>\d+)/reporte$', views.EnfermedadesPDF, name = 'EnfermedadesPDF'),
    url('^guardarNutricion$', views.guardarNutricion, name = 'guardarNutricion'),
    url('^guardarMedidasAntropometricas$', views.guardarMedidasAntropometricas, name = 'guardarMedidasAntropometricas'),
]
