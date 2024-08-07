from django.contrib import admin
from .models import Producto, Ingrediente, ProductoIngrediente, OtroProducto, Entrada, Bebida

class ProductoAdmin(admin.ModelAdmin):
    list_display = (        
        "nombre", 
        "descripcion",
        "precio",       
        "cantidad",
        "imagen",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    list_filter = ("nombre",)
    date_hierarchy = "fecha_actualizacion"


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Ingrediente)
admin.site.register(ProductoIngrediente)
admin.site.register(OtroProducto)
admin.site.register(Entrada)
admin.site.register(Bebida)

