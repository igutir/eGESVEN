from django.contrib import admin
from .models import *

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email']

admin.site.register(Categoria)
admin.site.register(Compania)
admin.site.register(Producto)
admin.site.register(Perfil)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Compra)
admin.site.register(Compra_producto)
