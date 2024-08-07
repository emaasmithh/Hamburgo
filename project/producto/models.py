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
    precio = models.FloatField()
    cantidad = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
       
   
class ProductoIngrediente(models.Model):    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ingrediente = models.ManyToManyField(Ingrediente, blank=True)

    def __str__(self):
        return self.producto.nombre
    
    def aumentar_precio(self, precio_extra):
        self.producto.precio += precio_extra
        self.save()

    def agregar_descripcion(self, descripcion):
        self.producto.descripcion += f" (extra {descripcion})"
        self.save()

class OtroProducto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()    
    precio = models.FloatField()
    cantidad = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
class Entrada(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()    
    precio = models.FloatField()
    cantidad = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
class Bebida(models.Model):     
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField()
    cantidad = models.FloatField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    fecha_actualizacion = models.DateField(null=True, blank=True, editable=False, default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
class OtroProducto2(models.Model):    
    producto = models.ForeignKey(OtroProducto, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.producto.nombre
    
    def aumentar_precio(self, precio_extra):
        self.producto.precio += precio_extra
        self.save()

    def agregar_descripcion(self, descripcion):
        self.producto.descripcion += f" (extra {descripcion})"
        self.save()

class Entrada2(models.Model):    
    producto = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.producto.nombre
    
    def aumentar_precio(self, precio_extra):
        self.producto.precio += precio_extra
        self.save()

    def agregar_descripcion(self, descripcion):
        self.producto.descripcion += f" (extra {descripcion})"
        self.save()

class Bebida2(models.Model):
    producto = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.producto.nombre
    
    def aumentar_precio(self, precio_extra):
        self.producto.precio += precio_extra
        self.save()

    def agregar_descripcion(self, descripcion):
        self.producto.descripcion += f" (extra {descripcion})"
        self.save()




    

    
    

