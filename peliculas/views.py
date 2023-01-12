from django.shortcuts import render
from peliculas.models import Peliculas, Directores, Generos
from peliculas.forms import PeliculasForm, DirectoresForm, GenerosForm

def crear_peliculas(request):
    if request.method == "GET":
        context= {
            "form" : PeliculasForm
        }
        return render(request, "peliculas/crear_peliculas.html", context=context) 
    elif request.method == "POST":
        form = PeliculasForm(request.POST)
        if form.is_valid():
            Peliculas.objects.create(
                nombre = form.cleaned_data["nombre"],
                duracion = form.cleaned_data["duracion"],
                año_de_lanzamiento = form.cleaned_data["año_de_lanzamiento"],
                genero = form.cleaned_data["genero"]
            )
            context= {
                "mensaje" : "Película creada exitosamente"
            }
            return render(request, "peliculas/crear_peliculas.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": PeliculasForm()
            }
            return render(request, "peliculas/crear_peliculas.html", context=context)

def listar_peliculas(request):
    if "search" in request.GET:
        peliculas = Peliculas.objects.filter(nombre__icontains = request.GET["search"])
    else:
        peliculas = Peliculas.objects.all()
    context = {
        "peliculas": peliculas,
    }
    return render(request, "peliculas/listado_peliculas.html", context=context)

def crear_directores(request):
    if request.method == "GET":
        context = {
            "form": DirectoresForm()
        }
        return render(request, "peliculas/crear_director.html", context=context)
    elif request.method == "POST":
        form = DirectoresForm(request.POST)
        if form.is_valid():
            Directores.objects.create(
                nombre = form.cleaned_data["nombre"],
                apellido = form.cleaned_data["apellido"],
                edad = form.cleaned_data["edad"],
                estado = form.cleaned_data["estado"],
            )
            context = {
                "mensaje" : "Director agregado exitosamente"
            }
            return render(request, "peliculas/crear_director.html", context=context)
        else:{
            "form_errors": form.errors,
            "form": DirectoresForm()
        }
        return render(request, "peliculas/crear_director.html", context=context)   

def listar_directores(request):
    if "search" in request.GET:
        directores = Directores.objects.filter(nombre__icontains = request.GET["search"])
    else:
        directores = Directores.objects.all()
    context = {
        "directores": directores,
    }
    return render(request, "peliculas/listado_directores.html", context=context)   

def crear_generos(request):
    if request.method == "GET":
        context= {
            "form" : GenerosForm
        }
        return render(request, "peliculas/crear_generos.html", context=context) 
    elif request.method == "POST":
        form = GenerosForm(request.POST)
        if form.is_valid():
            Generos.objects.create(
                nombre = form.cleaned_data["nombre"],
            )
            context= {
                "mensaje" : "Genero agregado exitosamente"
            }
            return render(request, "peliculas/crear_generos.html", context=context)
        else:
            context = {
                "form_errors": form.errors,
                "form": GenerosForm()
            }
            return render(request, "peliculas/crear_generos.html", context=context)   

def listar_generos(request):
    if "search" in request.GET:
        generos = Generos.objects.filter(nombre__icontains = request.GET["search"])
    else:
        generos = Generos.objects.all()
    context = {
        "generos": generos,
    }
    return render(request, "peliculas/listado_generos.html", context=context)   