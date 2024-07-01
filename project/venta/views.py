from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito
from producto.models import Producto, Ingrediente, ProductoIngrediente
from django.views.generic import ListView


def index(request):
    return render(request, "venta/index.html")

class ProductoList(ListView):
    model = Producto


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = ProductoIngrediente.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("venta:index")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = ProductoIngrediente.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("venta:index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = ProductoIngrediente.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("venta:index")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("venta:index")


