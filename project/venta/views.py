from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, OrdenCompra
from producto.models import Producto, Ingrediente, ProductoIngrediente, OtroProducto2, Entrada2, Bebida2
from venta.forms import MetodoPagoForm
from django.views.generic import ListView
from django.core.mail import send_mail
from django.conf import settings



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

def total_carrito_2(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += float(value["acumulado"])
    return total

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
                comentarios=comentarios,
                precio_total = total_carrito_2(request),               
                
            )
        precio_total = total_carrito_2(request)
        carrito = Carrito(request)
        items_carrito = carrito.obtener_detalle_pedido()
        detalles_pedido = f"Dirección de entrega: {direccion_entrega}\nPrecio total: $ {precio_total}\nMétodo de pago: {metodo_pago}\n"
        for item in items_carrito:
            detalles_pedido += f"{item["nombre"]} X {item["cantidad"]} --> descripción: {item["descripcion"]}\n"

        enviar_notificacion_pedido(detalles_pedido)

        carrito.limpiar()
            # Procesa la selección del método de pago aquí
        return redirect('venta:confirmacion_compra')  # Redirige a la página de confirmación
    
    else:
        form = MetodoPagoForm()  # Crea una instancia del formulario si el método no es POST

    context = {
        'form': form,  # Asegúrate de pasar el formulario al contexto
    }
    return render(request, 'venta/compra.html', context)






def enviar_notificacion_pedido(detalle_pedido):
    mensaje = detalle_pedido
    
    send_mail(
        'Nuevo pedido realizado',
        mensaje,
        settings.DEFAULT_FROM_EMAIL,  # Debe ser una dirección de correo válida en settings.py
        ['emaasmithh@hotmail.com'],  # Aquí debes poner la dirección de correo del negocio
        fail_silently=False,
    )

def confirmar_pedido(request):
    
    return render(request, 'venta/confirmacion_compra.html')



