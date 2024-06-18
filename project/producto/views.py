from django.shortcuts import render, redirect
from .models import Producto
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
def index(request):
    return render(request, "producto/index.html")

class ProductoList(ListView):
    model = Producto
