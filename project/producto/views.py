from django.shortcuts import render, redirect
from .models import Producto
from venta.models import Carrito

from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
def index(request):
    return render(request, "producto/index.html")

class ProductoList(ListView):
    model = Producto

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("producto:producto_list")

