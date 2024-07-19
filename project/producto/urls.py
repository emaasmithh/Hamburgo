from django.urls import path
from .views import index
from .views import ProductoList, agregar_producto, mostrar_detalle_producto, ProductoDetail, ProductoIngredienteUpdate, crear_producto_ingrediente, producto_list, OtroProductoDetail,  agregar_otro_producto, crear_otro_producto_2, crear_entrada_2, crear_bebida_2

app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("list/", producto_list, name="producto_list"),  
    path("agregar_producto/<int:producto_id>", agregar_producto, name="agregar_producto"),
    path("producto_detail/<int:pk>", ProductoDetail.as_view(), name="detalle_producto"),
    path("crear_producto_ingrediente/<int:producto_id>", crear_producto_ingrediente, name="crear_producto_ingrediente"),
    path("otro_producto_detail/<int:pk>", OtroProductoDetail.as_view(), name="otro_producto_detail"),
    path("agregar_otro_producto/<int:otro_producto_id>", agregar_otro_producto, name="agregar_otro_producto"),   
    path("crear_otro_producto_2/<int:producto_id>", crear_otro_producto_2, name="crear_otro_producto_2"),  
    path("crear_entrada_2/<int:producto_id>", crear_entrada_2, name="crear_entrada_2"),
    path("crear_bebida_2/<int:producto_id>", crear_bebida_2, name="crear_bebida_2"), 
]