from django.shortcuts import render

# Impportamos el modelo de usuario que ya biene en django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Importamos las clases para el CRUD
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

# importamos nuestro form presonalizado
from apps.usuario.forms import RegistroForm


# Creamos nuestra clase para crear usuarios
class RegistroUsuario(CreateView):
    #Creamos los atributos
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy("mascota:mascota_listar")
