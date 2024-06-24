from django.urls import path
from .views import index
from .views import ProductoList, agregar_producto, mostrar_detalle_producto, ProductoDetail, ProductoUpdate


app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("list/", ProductoList.as_view(), name="producto_list"),  
    path("agregar_producto/<int:producto_id>", agregar_producto, name="agregar_producto"),
    path("detail/<int:pk>", ProductoDetail.as_view(), name="detalle_producto"),
    path("update/<int:pk>", ProductoUpdate.as_view(), name="producto_update"),     
]