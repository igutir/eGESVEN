from django import forms
from django.contrib.auth.models import User
from .models import Producto, Perfil

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class ActualizarUsuarioForm(forms.ModelForm):

    #username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']


class ActualizarPerfilForm(forms.ModelForm):

    #rut = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    #telefono = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Perfil
        fields = ['telefono', 'fecha_nacimiento']

