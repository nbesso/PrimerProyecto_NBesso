
from django.shortcuts import render
from django.http import HttpResponse
from AppProyecto.forms import EntrenadoresFormulario, ActividadesFromulario, ClientesFormulario
from AppProyecto.models import Entrenadores, Actividades, Clientes



# Create your views here.

def entrenadores_formulario (request):
    if request.method == 'POST':
        entFormulario = EntrenadoresFormulario(request.POST)
        print(entFormulario)

        if entFormulario.is_valid:
            
            informacion = entFormulario.data
            
            r_nombre = informacion['nombre']
            r_apellido = informacion['apellido']
            r_email = informacion['email']

            entrenadores = Entrenadores(nombre=r_nombre, apellido=r_apellido, email=r_email)
            
            entrenadores.save()
    
    entFormulario = EntrenadoresFormulario()

    return render(request, 'AppProyecto/entrenadoresformulario.html', {"entFormulario": entFormulario})


def clientes_formulario (request):
    if request.method == 'POST':
        clFormulario = ClientesFormulario(request.POST)
        print(clFormulario)

        if clFormulario.is_valid:
            
            informacion = clFormulario.data
            
            r_nombre = informacion['nombre']
            r_apellido = informacion['apellido']
            r_email = informacion['email']
            r_edad = informacion['edad']

            clientes = Clientes(nombre=r_nombre, apellido=r_apellido, email=r_email, edad=r_edad)
            
            clientes.save()
    
    clFormulario = ClientesFormulario()

    return render(request, 'AppProyecto/clientesformulario.html', {"clFormulario": clFormulario})


def actividades_formulario (request):
    if request.method == 'POST':
        actFormulario = ActividadesFromulario(request.POST)
        print(actFormulario)

        if actFormulario.is_valid:
            
            informacion = actFormulario.data
            
            r_nombre = informacion['nombre']
            r_intensidad = informacion['intensidad']
            
            actividades = Actividades(nombre=r_nombre, intensidad = r_intensidad)
            
            actividades.save()
    
    actFormulario = ActividadesFromulario()

    return render(request, 'AppProyecto/actividadesformulario.html', {"actFormulario": actFormulario})
