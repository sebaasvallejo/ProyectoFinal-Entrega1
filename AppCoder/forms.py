from django import forms

class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    genero = forms.CharField()
    fecha = forms.CharField()

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    genero = forms.CharField()

class GeneroFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
