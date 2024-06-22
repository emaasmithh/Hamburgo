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
    
    def agregar_carrito(self):
        pass
    
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    elementos = models.ManyToManyField(ElementoCarrito)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    completado = models.BooleanField(default=False)
    numero_orden = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"Orden #{self.numero_orden} de {self.cliente.usuario.username}"
    

class Carrito():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]

        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": float(producto.precio),
                "cantidad": 1,
                "descripcion": producto.descripcion,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio  

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True


  



