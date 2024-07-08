from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la categoria', unique=True)

    def __str__(self):
        return self.nombre

class Compania(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to="cover", null=True, blank=True)
    imagen_carrusel = models.ImageField(upload_to="cover/carrusel", null=True, blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    compania = models.ForeignKey(Compania,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    telefono = models.IntegerField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Usuario(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class Compra(models.Model):
    fechacompra = models.DateField()
    totalcompra = models.IntegerField()
    numerotarjeta = models.IntegerField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.fechacompra

class Compra_producto(models.Model):
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__(self):
        return self.compra
