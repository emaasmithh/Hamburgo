from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.utils import timezone

from producto.models import Producto, ProductoIngrediente, Ingrediente
class UserManager(BaseUserManager):
    def create_user(self, email, nombre, password=None):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, password):
        user = self.create_user(email=email, nombre=nombre, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email

class Cliente(models.Model):
    usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="cliente")
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    

    def __str__(self) -> str:
        return self.usuario.username  
       
    

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
                "nombre": producto.producto.nombre,
                "acumulado": float(producto.producto.precio),
                "cantidad": 1,
                "descripcion": producto.producto.descripcion,                                                        
            }            
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.producto.precio
             

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
            self.carrito[id]["acumulado"] -= producto.producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True 

    def obtener_detalle_pedido(self):
        detalle_pedido = []
        for item_id, item_info in self.carrito.items():
            detalle_pedido.append({
                'nombre': item_info['nombre'],                
                'descripcion': item_info['descripcion'],
                'cantidad': item_info['cantidad']
            })
        return detalle_pedido


class OrdenCompra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario que realizó la compra
    precio_total = models.FloatField(null=True, blank=True)
    metodo_pago = models.CharField(max_length=50)
    metodo_entrega = models.CharField(max_length=50, blank=True, null=True)
    direccion_entrega = models.TextField(blank=True)
    comentarios = models.TextField(blank=True)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    detalles_pedido = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Orden de compra {self.pk} - Usuario: {self.usuario.username}'