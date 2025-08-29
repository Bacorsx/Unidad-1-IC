from django.contrib import admin
from .models import Zona, Categoria, Dispositivo

admin.site.register([Categoria, Zona])
admin.site.register(Dispositivo)

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "ubicacion", "created_at", "updated_at","deleted_at")
    search_fields = ("nombre", "ubicacion")