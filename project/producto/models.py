from django.db import models
from django.utils import timezone


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=255)
    precio_extra = models.FloatField()

    def __str__(self) -> str:
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ingrediente = models.ManyToManyField(Ingrediente, blank=True)
    precio = models.FloatField()
    cantidad = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
   

    
class ProductoIngrediente(models.Model):    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ingrediente = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.producto.nombre

