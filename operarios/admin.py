from django.contrib import admin
from operarios.models import Operario

@admin.register(Operario)
class OperarioAdmin(admin.ModelAdmin):
    pass
