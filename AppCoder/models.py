from django.db import models

class Libro(models.Model):
    titulo=models.CharField(max_length=40)
    autor=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    fecha=models.CharField(max_length=40)

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor}"

class Autor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    genero= models.CharField(max_length=40)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Genero: {self.genero}"

class Genero(models.Model):
    nombre= models.CharField(max_length=40)
    descripcion= models.CharField(max_length=180)
    
    def __str__(self):
        return (f'Nombre del género: {self.nombre}')
