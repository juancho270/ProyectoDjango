# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User)
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=100)
    telefono =  models.IntegerField()
    fecha_nacimiento = models.DateField()
    estado = models.BooleanField()
    correo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion= models.TextField()
    fecha= models.DateTimeField()
    estado = models.BooleanField()

    def __unicode__(self):
        return self.nombre

#link donde enseñan las formas en que podemos heredar de un modelo ya hecho de django

#https://es.stackoverflow.com/questions/8026/modificar-el-modelo-de-usuario-de-django
#https://miguelgomez.io/django/extender-user-django/


class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField()
    fecha= models.DateTimeField()
    estado = models.BooleanField()

class UsuarioActividad(models.Model):
    usuario = models.ForeignKey(Usuario)
    actividad = models.ForeignKey(Actividad)

class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion= models.TextField()
    fecha= models.DateTimeField()
    estado = models.BooleanField()

class ActividadEvento(models.Model):
    actividad = models.ForeignKey(Actividad)
    evento = models.ForeignKey(Evento)

class UsuarioEvento(models.Model):
    usuario = models.ForeignKey(Usuario)
    evento = models.ForeignKey(Evento)