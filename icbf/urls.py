from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^', include('login.urls', namespace='login')),
   url(r'^', include('operarios.urls', namespace='operarios')),
   url(r'^', include('beneficiarios.urls', namespace='beneficiarios')),
   url(r'^', include('caracteristicas_vivienda.urls', namespace='caracteristicas_vivienda')),
   url(r'^', include('composicion_familiar.urls', namespace='composicion_familiar')),
   url(r'^', include('relaciones_comunitarias.urls', namespace='relaciones_comunitarias')),
   url(r'^', include('nutricion.urls', namespace='nutricion')),
   url(r'^', include('salud.urls', namespace='salud')),
   url(r'^', include('parametrizacion.urls', namespace='parametrizacion')),
   url(r'^', include('calendario.urls', namespace='calendario')),
]
