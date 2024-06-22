from django.urls import path
from .views import index
from .views import ProductoList, agregar_producto


app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("list/", ProductoList.as_view(), name="producto_list"),  
    path("agregar_producto/<int:producto_id>", agregar_producto, name="agregar_producto")      
]