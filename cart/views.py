from django.shortcuts import render, redirect

from .cart import Cart
from eGESVEN.models import Producto

def verCart(request):
    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }

    print(productos)

    return render(request, 'cart.html', data)

def agregarProductoCart(request, id):
    carro = Cart(request)
    producto = Producto.objects.get(id=id)

    carro.agregar(producto)

    return redirect(to="ver_cart")

def disminuirProductoCart(request, id):
    carro = Cart(request)
    producto = Producto.objects.get(id=id)

    carro.disminuir(producto)

    return redirect(to="ver_cart")

def eliminarProductoCart(request, id):
    carro = Cart(request)
    producto = Producto.objects.get(id=id)

    carro.eliminar(producto)

    return redirect(to="ver_cart")

def limpiarCart(request):
    carro = Cart(request)
    carro.limpiar()

    return redirect(to="ver_cart")
