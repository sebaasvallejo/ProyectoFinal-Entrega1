from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Libro, Autor, Genero
from AppCoder.forms import LibroFormulario, AutorFormulario, GeneroFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http.request import QueryDict

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def libros(request):
      return render(request, "AppCoder/libros.html")

def autores(request):
      return render(request, "AppCoder/autores.html")

def generos(request):
      return render(request, "AppCoder/generos.html")

def libroFormulario(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro (titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"], fecha=informacion["fecha"])
            libro.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = LibroFormulario
    return render(request, "AppCoder/libroFormulario.html", {"miFormulario":miFormulario})

def autorFormulario(request):
    if request.method == "POST":
        miFormulario = AutorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            autor = Autor (nombre=informacion["nombre"], apellido=informacion["apellido"], genero=informacion["genero"])
            autor.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AutorFormulario
    return render(request, "AppCoder/autorFormulario.html", {"miFormulario":miFormulario})

def generoFormulario(request):
    if request.method == "POST":
        miFormulario = GeneroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            genero = Genero (nombre=informacion["nombre"], descripcion=informacion["descripcion"])
            genero.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = GeneroFormulario
    return render(request, "AppCoder/generoFormulario.html", {"miFormulario":miFormulario})

def busquedaLibro(request):
    return render(request, "AppCoder/busquedaLibro.html")

def buscar(request):
      if  request.GET["libro"]:
            respuesta = f"Estoy buscando el libro: {request.GET['libro'] }"
      else:
            respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

