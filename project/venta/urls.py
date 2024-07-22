from django.urls import path
from .views import index, ProductoList, agregar_producto, eliminar_producto, limpiar_carrito, restar_producto, ver_carrito, comprar, confirmar_pedido


app_name = "venta"

urlpatterns = [
    path("", ProductoList.as_view(), name="index"), 
    path("agregar_producto/<int:producto_id>", agregar_producto, name="agregar"),
    path("eliminar_producto/<int:producto_id>", eliminar_producto, name="eliminar"),
    path("restar_producto/<int:producto_id>", restar_producto, name="restar"),
    path("limpiar_carrito/", limpiar_carrito, name="limpiar"),     
    path("ver_carrito/", ver_carrito, name="ver_carrito"),
    path("compra/", comprar, name="compra"),
    path("confirmacion_compra/", confirmar_pedido, name="confirmacion_compra"),   
]