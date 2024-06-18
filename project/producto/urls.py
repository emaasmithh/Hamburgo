from django.urls import path
from .views import index
from .views import ProductoList

app_name = "producto"

urlpatterns = [
    path("", index, name="index"),
    path("list/", ProductoList.as_view(), name="producto_list"),    
]