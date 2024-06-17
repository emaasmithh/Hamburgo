from django.urls import path
from .views import index

app_name = "venta"

urlpatterns = [
    path("", index, name="index"),    
]