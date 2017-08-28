from django.contrib import admin
from entidad_administradora_servicio.models import *

@admin.register(Entidad_Administradora)
class Entidad_AdministradoraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_documento','numero_documento')
    search_fields = ('nombre','tipo_documento','numero_documento')

@admin.register(Modalidades_servicio)
class Modalidades_servicioAdmin(admin.ModelAdmin):
    pass

@admin.register(UDS)
class UDS_AdministradoraAdmin(admin.ModelAdmin):
    list_display = ('entidad','nombre', 'modalidad','pais','departamento','ciudad','direccion')
    search_fields = ('entidad','nombre','modalidad','pais','departamento','ciudad','direccion')
