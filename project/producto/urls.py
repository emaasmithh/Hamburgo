from django.urls import path
from .views import index

app_name = "producto"

urlpatterns = [
    path("", index, name="index"),    
]