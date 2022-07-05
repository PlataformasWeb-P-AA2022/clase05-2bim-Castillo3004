from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

from ventas.models import *

from ventas.forms import *



def index(request):

    concesionarios = Concesionario.objects.all()

    informacion_template = {'concesionarios': concesionarios, 'numero_concesionarios': len(concesionarios)}
    return render(request, 'index.html', informacion_template)


## Crear

def crear_concesionario(request):
    """
    """
    if request.method=='POST':
        formulario = ConcesionarioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = ConcesionarioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearConcesionario.html', diccionario)

def crear_auto(request):
    """
    """
    if request.method=='POST':
        formulario = AutoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = AutoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearAuto.html', diccionario)

def crear_moto(request):
    """
    """
    if request.method=='POST':
        formulario = MotoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = MotoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearMoto.html', diccionario)

def crear_auto_concesionario(request, id):
    """
    """
    concesionario = Concesionario.objects.get(pk=id)
    if request.method=='POST':
        formulario = AutoConcesionarioForm(concesionario, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = AutoConcesionarioForm(concesionario)
    diccionario = {'formulario': formulario, 'concesionario': concesionario}

    return render(request, 'crearAutoConcesionario.html', diccionario)

def crear_moto_concesionario(request, id):
    """
    """
    concesionario = Concesionario.objects.get(pk=id)
    if request.method=='POST':
        formulario = MotoConcesionarioForm(concesionario, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MotoConcesionarioForm(concesionario)
    diccionario = {'formulario': formulario, 'concesionario': concesionario}

    return render(request, 'crearMotoConcesionario.html', diccionario)

# Obtener 

def obtener_concesionario(request, id):

    concesionario = Concesionario.objects.get(pk=id)

    informacion_template = {'concesionario': concesionario}
    return render(request, 'obtenerConcesionario.html', informacion_template)

def obtener_auto(request, id):

    auto = Auto.objects.get(pk=id)

    informacion_template = {'auto': auto}
    return render(request, 'obtenerAuto.html', informacion_template)

def obtener_moto(request, id):

    moto = Moto.objects.get(pk=id)

    informacion_template = {'moto': moto}
    return render(request, 'obtenerMoto.html', informacion_template)

# Editar

def editar_concesionario(request, id):
    """
    """
    concesionario = Concesionario.objects.get(pk=id)
    if request.method=='POST':
        formulario = ConcesionarioForm(request.POST, instance=concesionario)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ConcesionarioForm(instance=concesionario)
    diccionario = {'formulario': formulario}

    return render(request, 'editarConcesionario.html', diccionario)

def editar_auto(request, id):
    """
    """
    auto = Auto.objects.get(pk=id)
    if request.method=='POST':
        formulario = AutoForm(request.POST, instance=auto)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = AutoForm(instance=auto)
    diccionario = {'formulario': formulario}

    return render(request, 'editarAuto.html', diccionario)

def editar_moto(request, id):
    """
    """
    moto = Moto.objects.get(pk=id)
    if request.method=='POST':
        formulario = MotoForm(request.POST, instance=moto)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = MotoForm(instance=moto)
    diccionario = {'formulario': formulario}

    return render(request, 'editarMoto.html', diccionario)


# Eliminar

def eliminar_concesionario(request, id):
    """
    """
    concesionario = Concesionario.objects.get(pk=id)
    concesionario.delete()
    return redirect(index)

def eliminar_auto(request, id):
    """
    """
    auto = Auto.objects.get(pk=id)
    auto.delete()
    return redirect(index)

def eliminar_moto(request, id):
    """
    """
    moto = Moto.objects.get(pk=id)
    moto.delete()
    return redirect(index)





