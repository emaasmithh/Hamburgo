from django.urls import path
from .views import index, ProductoList, agregar_producto, eliminar_producto, limpiar_carrito, restar_producto


app_name = "venta"

urlpatterns = [
    path("", ProductoList.as_view(), name="index"), 
    path("agregar_producto/<int:producto_id>", agregar_producto, name="agregar"),
    path("eliminar_producto/<int:producto_id>", eliminar_producto, name="eliminar"),
    path("restar_producto/<int:producto_id>", restar_producto, name="restar"),
    path("limpiar_carrito/", limpiar_carrito, name="limpiar"),        
]