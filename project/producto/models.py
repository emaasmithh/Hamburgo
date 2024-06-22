from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.FloatField()
    cantidad = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
   
