
from django import forms


class EntrenadoresFormulario (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email = forms.EmailField()

class ClientesFormulario (forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    edad = forms.IntegerField()

class ActividadesFromulario (forms.Form):
    nombre= forms.CharField(max_length=40)
    intensidad = forms.CharField(max_length=10)