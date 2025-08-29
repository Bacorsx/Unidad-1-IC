from django.contrib import admin
from .models import Zona, Categoria, Dispositivo

admin.site.register([Categoria, Zona])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "consumo", "estado", "created_at", "updated_at", "deleted_at")
    list_filter = ("estado", "zona", "categoria", "consumo")
    search_fields = ("nombre",)
    readonly_fields = ("created_at", "updated_at", "deleted_at")

    fieldsets = (
        (None, {
            "fields": ("nombre", "consumo", "estado", "zona", "categoria")
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            # Si quieres bloquear edición a no-superusuarios:
            return ("nombre", "consumo", "estado", "zona", "categoria",
                    "created_at", "updated_at", "deleted_at")
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    