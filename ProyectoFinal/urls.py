from django.urls import path
from AppCoder import views
from django.contrib import admin

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('admin/', admin.site.urls),
    path('libros',views.libros, name="Libros"),
    path('autores', views.autores, name='Autores'),
    path('genero', views.generos, name="Géneros"),
    path('busquedaLibro', views.busquedaLibro, name="BusquedaLibro"),
    path('buscar/', views.buscar),
    path('libroFormulario', views.libroFormulario, name="LibroFormulario"),
    path('autorFormulario', views.autorFormulario, name="AutorFormulario"),
    path('generoFormulario', views.generoFormulario, name="GeneroFormulario")
]