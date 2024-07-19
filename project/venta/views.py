from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito
from producto.models import Producto, Ingrediente, ProductoIngrediente, OtroProducto2
from django.views.generic import ListView


def index(request):
    return render(request, "venta/index.html")

class ProductoList(ListView):
    model = Producto

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = ProductoIngrediente.objects.get(id=producto_id)
    carrito.agregar(producto)    
    return redirect("producto:producto_list")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = ProductoIngrediente.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("producto:producto_list")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    if producto_id == ProductoIngrediente:
        producto = ProductoIngrediente.objects.get(id=producto_id)
    else:
        producto = OtroProducto2.objects.get(id=producto_id) 

    carrito.restar(producto)
    return redirect("producto:producto_list")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("producto:producto_list")


