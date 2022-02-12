from django.contrib import admin
from django.urls import path
from AppProyecto.views import entrenadores_formulario, clientes_formulario, actividades_formulario

urlpatterns = [
    path("entrenadores/", entrenadores_formulario, name= "EntrenadoresFomulario"),
    path("clientes/", clientes_formulario, name= "ClientesFomulario"),
    path("actividades/", actividades_formulario, name= "ActividadesFomulario"),
  ]