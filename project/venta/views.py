from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, OrdenCompra
from producto.models import Producto, Ingrediente, ProductoIngrediente, OtroProducto2
from venta.forms import MetodoPagoForm
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

def ver_carrito(request):
    return render(request, "venta/ver_carrito.html")

def comprar(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            metodo_pago = form.cleaned_data['metodo_pago']
            direccion_entrega = form.cleaned_data['direccion_entrega']
            comentarios = form.cleaned_data['comentarios']

            # Guardar la orden de compra en la base de datos
            orden_compra = OrdenCompra.objects.create(
                usuario=request.user,  # Suponiendo que tienes un sistema de autenticación de usuarios
                metodo_pago=metodo_pago,
                direccion_entrega=direccion_entrega,
                comentarios=comentarios
            )
            # Procesa la selección del método de pago aquí
            return redirect('venta:confirmacion_compra')  # Redirige a la página de confirmación
    
    else:
        form = MetodoPagoForm()  # Crea una instancia del formulario si el método no es POST

    context = {
        'form': form,  # Asegúrate de pasar el formulario al contexto
    }
    return render(request, 'venta/compra.html', context)

def confirmacion_compra(request):
    return render(request,"venta/confirmacion_compra.html")


