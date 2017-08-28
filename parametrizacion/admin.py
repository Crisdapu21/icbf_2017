from django.contrib import admin
from parametrizacion.models import *

@admin.register(Ocupaciones)
class OcupacionesAdmin(admin.ModelAdmin):
    pass
@admin.register(Estado_Laboral)
class Estado_LaboralAdmin(admin.ModelAdmin):
    pass
@admin.register(Tipo_Documento)
class Tipo_DocumentoAdmin(admin.ModelAdmin):
    pass
@admin.register(EPS)
class EPSAdmin(admin.ModelAdmin):
    pass
@admin.register(No_EPS)
class No_EPSAdmin(admin.ModelAdmin):
    pass
@admin.register(Metas_Cabeza)
class Metas_CabezaAdmin(admin.ModelAdmin):
    pass
@admin.register(Organizaciones_Civiles)
class Organizaciones_CivilesAdmin(admin.ModelAdmin):
    pass

@admin.register(Paises)
class PaisesAdmin(admin.ModelAdmin):
    pass

@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ('pais', 'departamento')
    search_fields = ('departamento',)

@admin.register(Ciudades)
class CiudadesAdmin(admin.ModelAdmin):
    list_display = ('departamento','ciudad')
    search_fields = ('departamento','ciudad')

@admin.register(Parentezco)
class ParentezcoAdmin(admin.ModelAdmin):
    pass

@admin.register(Nivel_Escolaridad)
class Nivel_EscolaridadAdmin(admin.ModelAdmin):
    pass
