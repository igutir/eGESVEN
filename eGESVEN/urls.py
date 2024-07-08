from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', home, name="home"),
    path('explorar/', explorar, name="explorar"),
    path('categoria/<int:id>/', categoria, name="categoria"),

    ##Paginas para el pokemon
    path('pokedex_api/', pokedex_api, name="pokedex_api"),
    path('quepokemoneres/', quepokemoneres, name="quepokemoneres"),

    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('registro_usuario/', registro_usuario, name="registro_usuario"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="pw/password_change_form.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="pw/password_change_done.html"), name="password_change_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="pw/password_reset_form.html", email_template_name='pw/password_reset_email.html'), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="pw/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="pw/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="pw/password_reset_complete.html"), name="password_reset_complete"),

    path("perfil/", editar_perfil, name="editar_perfil"),
    #path("editarperfil/", ProfileUpdate.as_view(), name="editar_perfil_usuario"),

    path('j/<int:id>/', producto, name="producto"),
    path('mantenedor/', mantenedor_productos, name="mantenedor_productos"),
    path('mantenedor/agregar_producto/', agregar_producto, name="agregar_producto"),
    path('mantenedor/listado_productos/', modificar_producto_lista, name="modificar_producto_lista"),
    path('mantenedor/listado_productos/u/<int:idproducto>/', modificar_producto, name="modificar_producto"),
    path('mantenedor/listado_productos/d/<idproducto>/', eliminar_producto, name="eliminar_producto"),
]