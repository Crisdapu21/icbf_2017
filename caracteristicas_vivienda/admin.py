from django.contrib import admin
from caracteristicas_vivienda.models import *

@admin.register(Tipo_Vivienda)
class Tipo_Vivienda(admin.ModelAdmin):
    pass

@admin.register(Tipo_Tenencia_Vivienda)
class Tipo_Tenencia_Vivienda(admin.ModelAdmin):
    pass

@admin.register(Tipo_Cama)
class Tipo_Cama(admin.ModelAdmin):
    pass

@admin.register(Servicios_Domiciliarios)
class Servicios_Domiciliarios(admin.ModelAdmin):
    pass

@admin.register(Fuente_Agua_Consumible)
class Fuente_Agua_Consumible(admin.ModelAdmin):
    pass

@admin.register(Periodo_Agua)
class Periodo_Agua(admin.ModelAdmin):
    pass

@admin.register(Uso_Agua)
class Uso_Aguas(admin.ModelAdmin):
    pass

@admin.register(Tratamiento_Basuras)
class Tratamiento_Basuras(admin.ModelAdmin):
    pass

@admin.register(Tipo_Sanitario)
class Tipo_Sanitario(admin.ModelAdmin):
    pass

@admin.register(Servicios_Comunitarios)
class Servicios_Comunitarios(admin.ModelAdmin):
    pass
