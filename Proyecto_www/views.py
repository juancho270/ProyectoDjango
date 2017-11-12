from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from Proyecto_www.forms import Login_form, Registro_form,Evento_form,Noticia_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Proyecto_www.models import Usuario
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Usuario,Evento,Noticia
from django.core.urlresolvers import reverse_lazy


def index(request):
    context = {}
    if request.user.is_anonymous:
        return render(request, 'Proyecto_www/usuarios/usuarioPublico.html', context)
    if request.user.usuario.tipo == "administrador":
        return render(request, 'Proyecto_www/usuarios/administrador.html', context)
    if request.user.usuario.tipo == "usuario":
        return render(request, 'Proyecto_www/usuarios/usuarioPublicoLogeado.html', context)
    if request.user.usuario.tipo == "gerente":
        return render(request, 'Proyecto_www/usuarios/gerente.html', context)
    if request.user.usuario.tipo == "operador":
        return render(request, 'Proyecto_www/usuarios/operador.html', context)


def registrarUsuario(request):
    context = {}
    form = Registro_form()
    context['form_registro'] = form
    if request.method == 'POST':
        form = Registro_form(request.POST)
        if form.is_valid():
            Nombre = request.POST.get("Nombre")
            Apellido = request.POST.get("Apellido")
            Cedula = request.POST.get("Cedula")
            Fecha_de_Nacimiento = request.POST.get("Fecha_de_Nacimiento")
            Estado = request.POST.get("Estado")
            if Estado == 'on':
                Estado = True
            else:
                Estado = False
            user = request.POST.get("user")
            password = request.POST.get("password")
            Tipo = request.POST.get("Tipo")
            Correo = request.POST.get("Correo")
            Telefono = request.POST.get("Telefono")
            principal = User(password=make_password(password), username=user, first_name=Nombre, last_name=Apellido,
                             email=Correo)
            principal.save()
            registro = Usuario(user=principal, nombre=Nombre, cedula=Cedula, correo=Correo, telefono=Telefono,
                               tipo=Tipo, estado=Estado,
                               fecha_nacimiento=Fecha_de_Nacimiento)
            registro.save()

        else:
            return render(request, 'Proyecto_www/usuarios/administradorMenu/registrar.html')
    else:
        return render(request, 'Proyecto_www/usuarios/administradorMenu/registrar.html', context)


def consultarUsuario(request):
    obj = Usuario.objects.all()
    obj2 = User.objects.all()
    for abc in obj:
        Nombre = abc.nombre
        Cedula = abc.cedula
        Tipo = abc.tipo
        Estado = abc.estado
        Telefono = abc.telefono
        Correo = abc.correo

    for abc in obj2:
        Apellido = abc.last_name
        Ultimo_login = abc.last_login
        print(Apellido)

    context = {
        "obj": obj,
        "obj2": obj2,
        "Nombre": Nombre,
        "Cedula": Cedula,
        "Tipo": Tipo,
        "Estado": Estado,
        "Telefono": Telefono,
        "Correo": Correo,
        "Apellido": Apellido,
        "Ultimo_login": Ultimo_login,
    }
    return render(request, 'Proyecto_www/usuarios/administradorMenu/consultar.html', context)


def login_page(request):
    context = {}
    form = Login_form()
    context['form_login'] = form
    if request.method == "POST":
        form = Login_form(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'Proyecto_www/usuarios/login.html', context)
        context['form'] = form
        return render(request, 'Proyecto_www/usuarios/login.html', context)

    else:
        if request.user.is_anonymous:
            return render(request, 'Proyecto_www/usuarios/login.html', context)
        else:
            return redirect('index')


def logout_page(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        logout(request)
        return redirect('login')


def seleccionarUsuario(request):
    obj = Usuario.objects.all()
    for abc in obj:
        Nombre = abc.nombre

    context = {
        "obj": obj,
        "Nombre": Nombre
    }

    form = Registro_form()
    context['form_registro'] = form

    return render(request, 'Proyecto_www/usuarios/administradorMenu/seleccionar.html', context)

def modificarUsuario(request,nombre):
    if request.method == 'POST':
        form = Registro_form(request.POST)

        if form.is_valid():
            Nombre = request.POST.get("Nombre")
            Apellido = request.POST.get("Apellido")
            Cedula = request.POST.get("Cedula")
            Fecha_de_Nacimiento = request.POST.get("Fecha_de_Nacimiento")
            Estado = request.POST.get("Estado")
            if Estado == 'on':
                Estado = True
            else:
                Estado = False
            user = request.POST.get("user")
            password = request.POST.get("password")
            Tipo = request.POST.get("Tipo")
            Correo = request.POST.get("Correo")
            Telefono = request.POST.get("Telefono")
            print(Nombre)
            principal = User(password=make_password(password), username=user, first_name=Nombre, last_name=Apellido,
                             email=Correo)
            principal.save()
            registro = Usuario(user=principal, nombre=Nombre, cedula=Cedula, correo=Correo, telefono=Telefono,
                               tipo=Tipo, estado=Estado,
                               fecha_nacimiento=Fecha_de_Nacimiento)
            registro.save()

        else:
            render(request, 'Proyecto_www/usuarios/administradorMenu/modificar.html')
    else:
        render(request, 'Proyecto_www/usuarios/administradorMenu/modificar.html')

def registrarEvento(request):
    context = {}
    form = Evento_form()
    context['form_evento'] = form
    if request.method == 'POST':
        form = Evento_form(request.POST)
        if form.is_valid():
            Nombre = request.POST.get("Nombre")
            Descripcion = request.POST.get("Descripcion")
            Fecha = request.POST.get("Fecha")
            Estado = request.POST.get("Estado")
            if Estado == 'on':
                Estado = True
            else:
                Estado = False
            registro = Evento(nombre=Nombre,descripcion=Descripcion,fecha=Fecha,estado=Estado)
            registro.save()
            return render(request, 'Proyecto_www/usuarios/operador.html',context)
        else:
            render(request, 'Proyecto_www/usuarios/operadorMenu/crearEvento.html',context)
    else:
        return render(request, 'Proyecto_www/usuarios/operadorMenu/crearEvento.html', context)

def consultarEvento(request):
    obj = Evento.objects.all()
    for abc in obj:
        Nombre = abc.nombre
        Descripcion = abc.descripcion
        Fecha = abc.fecha
        Estado=abc.estado


    context = {
        "obj": obj,
        "Nombre": Nombre,
        "Descripcion": Descripcion,
        "Fecha": Fecha,
        "Estado": Estado,
    }
    return render(request, 'Proyecto_www/usuarios/operadorMenu/consultarEvento.html', context)

def registrarNoticia(request):
    context = {}
    form = Noticia_form()
    context['form_noticia'] = form
    if request.method == 'POST':
        form = Noticia_form(request.POST)
        if form.is_valid():
            Titulo = request.POST.get("Titulo")
            Descripcion = request.POST.get("Descripcion")
            Fecha = request.POST.get("Fecha")
            Estado = request.POST.get("Estado")
            if Estado == 'on':
                Estado = True
            else:
                Estado = False
            registro = Noticia(titulo=Titulo,descripcion=Descripcion,fecha=Fecha,estado=Estado)
            registro.save()
            return render(request, 'Proyecto_www/usuarios/administrador.html',context)
        else:
           return render(request, 'Proyecto_www/usuarios/administradorMenu/registrarNoticia.html',context)
    else:
        return render(request, 'Proyecto_www/usuarios/administradorMenu/registrarNoticia.html', context)

def consultarNoticia(request):
    obj = Noticia.objects.all()
    for abc in obj:
        Titulo = abc.titulo
        Descripcion = abc.descripcion
        Fecha = abc.fecha
        Estado=abc.estado


    context = {
        "obj": obj,
        "Titulo": Titulo,
        "Descripcion": Descripcion,
        "Fecha": Fecha,
        "Estado": Estado,
    }
    return render(request, 'Proyecto_www/usuarios/administradorMenu/consultarNoticia.html', context)