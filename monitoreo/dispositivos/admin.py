from django.contrib import admin
from .models import Zona, Categoria, Dispositivo

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "ubicacion", "creado_en", "actualizado_en")
    search_fields = ("nombre", "ubicacion")
