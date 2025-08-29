from django.db import models

class BaseMode(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo")
    ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=True)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre