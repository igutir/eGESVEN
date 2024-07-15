from typing import Any
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.urls import reverse_lazy

from .forms import ProductoForm, ActualizarUsuarioForm, ActualizarPerfilForm
from .models import Producto, Categoria, Perfil

import requests

# Create your views here.


def home(request):

    productos_carrusel = Producto.objects.filter(imagen_carrusel__startswith="cover/carrusel/")

    data = {
        'productos' : productos_carrusel
    }

    return render(request, "index.html", data)

def categoria(request, id):

    categoria = get_object_or_404(Categoria, id = id)

    productos_categoria = Producto.objects.filter(categoria_id=id)

    data = {
        'categoria' : categoria,
        'productos_categoria' : productos_categoria
    }

    return render(request, "categoria.html", data)

def explorar(request):

    productos = Producto.objects.all()


    data = {
        'productos' : productos
    }

    return render(request, "explorar.html", data)

def producto(request, id):

    producto = get_object_or_404(Producto, id = id)

    data = {
        'producto' : producto
    }

    return render(request, "producto.html", data)


@login_required(login_url="login/")
@permission_required(['eGESVEN.add_producto', 'eGESVEN.delete_producto'], login_url="login/")
def mantenedor_productos(request):

    return render(request, "mantenedor/producto/mantenedor_productos.html")


@login_required(login_url="login/")
@permission_required(['eGESVEN.add_producto'], login_url="login/")
def agregar_producto(request):

    data = {
        "form_producto": ProductoForm,
        "mensaje": ""
    }

    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Producto agregado"
        else:
            data["mensaje"] = "Error"
            data["form"] = formulario

    return render(request, "mantenedor/producto/agregar.html", data)

@login_required(login_url="login/")
@permission_required(['eGESVEN.change_producto', 'eGESVEN.delete_producto'], login_url="login/")
def modificar_producto_lista(request):

    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }

    return render(request, "mantenedor/producto/listado_productos.html", data)

@login_required(login_url="login/")
@permission_required(['eGESVEN.change_producto'], login_url="login/")
def modificar_producto(request, idproducto):

    producto = get_object_or_404(Producto, id = idproducto)

    data = {
        "form_producto": ProductoForm(instance=producto)
    }

    if request.method == "POST":
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)

        if formulario.is_valid:
            formulario.save()
            return redirect(to="modificar_producto_lista")
        else:
            data["mensaje"] = "Error"
            data["form"] = formulario

    return render(request, "mantenedor/producto/modificar.html", data)

@login_required(login_url="login/")
@permission_required(['eGESVEN.delete_producto'], login_url="login/")
def eliminar_producto(request, idproducto):

    producto = get_object_or_404(Producto, id = idproducto)

    producto.delete()

    return redirect(to="modificar_producto_lista")


def login_usuario(request):

    print('Bienvenido ' + request.user.username)

    if request.user.groups.filter(name="usuario"):
        print("Grupo: Usuario")

    return render(request, "registration/login.html")

def editar_perfil(request):

    usuario = get_object_or_404(User, id = request.user.id)
    perfil = get_object_or_404(Perfil, user_id = request.user.id)

    print(perfil)

    data = {
        "form_user": ActualizarUsuarioForm(instance=usuario),
        "form_profile": ActualizarPerfilForm(instance=perfil)
    }

    if request.method == "POST":

        form_usuario = ActualizarUsuarioForm(request.POST, instance=request.user)
        form_perfil = ActualizarPerfilForm(request.POST, instance=request.user.perfil)

        if form_usuario.is_valid and form_perfil.is_valid:

            form_usuario.save()
            form_perfil.save()

            return redirect(to="editar_perfil")
        else:

            form_usuario = ActualizarUsuarioForm(instance=request.user)
            form_perfil = ActualizarPerfilForm(instance=request.user.perfil)

            data['form_usuario'] = form_usuario
            data['form_perfil'] = form_perfil

    return render(request, 'registration/editar_perfil.html', data)

def registro_usuario(request):

    data = {
        "mensaje": ""
    }

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password = request.POST.get("password")

        usuario = User()
        usuario.set_password(password)
        usuario.username = nombre
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo

        grupoUsuario = Group.objects.get(name="usuario")

        try:
            usuario.save()
            usuario.groups.add(grupoUsuario)

            user = authenticate(username=usuario.username, password=password)
            login(request, user)

            return redirect(to="home")

        except:
            data["mensaje"] = "Hubo un error"

    return render(request, "registration/registro.html")


