from django import forms

from .models import Usuario,Noticia,Actividad,UsuarioActividad,Evento,ActividadEvento,UsuarioEvento

class Login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class Registro_form(forms.Form):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    Cedula = forms.IntegerField()
    Fecha_de_Nacimiento = forms.DateField()
    Estado = forms.BooleanField()
    user = forms.CharField()
    password = forms.CharField()
    Tipo = forms.CharField()
    Correo = forms.EmailField()
    Telefono = forms.IntegerField()

class Evento_form(forms.Form):
    Nombre = forms.CharField()
    Descripcion = forms.CharField()
    Fecha = forms.DateField()
    Estado = forms.BooleanField()

class Noticia_form(forms.Form):
    Titulo = forms.CharField()
    Descripcion = forms.CharField()
    Fecha = forms.DateField()
    Estado = forms.BooleanField()


