from django.urls import path
from .views import *

urlpatterns = [
    path('', verCart, name='ver_cart'),
    path('agregar/<int:id>', agregarProductoCart, name='agregar_cart'),
    path('disminuir/<int:id>', disminuirProductoCart, name='disminuir_cart'),
    path('eliminar/<int:id>', eliminarProductoCart, name='eliminar_cart'),
    path('limpiar/', limpiarCart, name='limpiar_cart'),
]
