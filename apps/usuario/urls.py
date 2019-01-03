from django.conf.urls import url

#Importamos la vista de nuestra app
from apps.usuario.views import RegistroUsuario


urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
]