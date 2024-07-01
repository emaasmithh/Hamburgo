from django import forms

from . import models

class ProductoIngredienteForm(forms.ModelForm):
    class Meta:
        model = models.ProductoIngrediente
        fields = ["ingrediente"]