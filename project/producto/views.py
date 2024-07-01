from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, ProductoIngrediente, Ingrediente
from .forms import ProductoIngredienteForm
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

def mostrar_detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    context = {"producto": producto}
    return render(request, "detalle_producto.html", context)

class ProductoDetail(DetailView):
    model = Producto

class IngredienteDetail(DetailView):
    model = Ingrediente
    template_name = 'producto/producto_detail.html'
    context_object_name = 'objeto1'


class ProductoIngredienteUpdate(UpdateView):
    model = ProductoIngrediente
    form_class = ProductoIngredienteForm
    success_url = reverse_lazy("producto:producto_list")     

def crear_producto_ingrediente(request, producto_id):
    producto_base = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        ingredientes_seleccionados = request.POST.getlist('ingredientes')
        
        # Crear una instancia de ProductoIngrediente
        producto_ingrediente = ProductoIngrediente.objects.create(producto=producto_base)
        
        # Agregar los ingredientes seleccionados al ProductoIngrediente
        for ingrediente_id in ingredientes_seleccionados:
            ingrediente = Ingrediente.objects.get(pk=ingrediente_id)
            producto_ingrediente.ingrediente.add(ingrediente)
            if ingrediente:
                producto_ingrediente.producto.aumentar_precio(ingrediente.precio_extra)
        
        producto_ingrediente.save()

        carrito = Carrito(request)
        carrito.agregar(producto_ingrediente)
        
        # Redirigir a alguna página de confirmación o a la lista de productos
        return redirect("producto:producto_list")
    
    # Obtener los ingredientes disponibles para mostrar en el formulario
    ingredientes_disponibles = Ingrediente.objects.all()
    
    context = {
        'producto_base': producto_base,
        'ingredientes_disponibles': ingredientes_disponibles,
    }
    return render(request, 'producto/producto_list.html', context)

class ProductoIngredienteDetail(DetailView):
    model = ProductoIngrediente
    template_name = "venta/carrito.html"

