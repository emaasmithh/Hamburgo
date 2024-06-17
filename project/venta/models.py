from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from producto.models import Producto
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cliente")
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.usuario.username
    
class ElementoCarrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} para {self.cliente.usuario.username}"
    
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    elementos = models.ManyToManyField(ElementoCarrito)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    completado = models.BooleanField(default=False)
    numero_orden = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"Orden #{self.numero_orden} de {self.cliente.usuario.username}"



