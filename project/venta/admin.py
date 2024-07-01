from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "usuario",
        "celular",
        "direccion",
    )
    list_display_links = ("usuario",)
    list_filter = ("usuario",)
    

admin.site.register(Cliente, ClienteAdmin)
