from django.contrib import admin
from . models import productos, TipoProducto, tipo2

class tipo2Admin(admin.ModelAdmin):
    search_fields = ('tipo2_name'),
    ordering = ['tipo2_name']
class productosAdmin(admin.ModelAdmin):
    ordering = ('Tipo2'),
    autocomplete_fields = ['Tipo2']
# Register your models here.
admin.site.register(productos, productosAdmin) 
admin.site.register(TipoProducto)
admin.site.register(tipo2, tipo2Admin)