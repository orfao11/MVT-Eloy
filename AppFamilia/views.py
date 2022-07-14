from django.http import HttpResponse
from AppFamilia.models import Familia, Mascotas, Vecinos
from django.template import Context, Template, loader
from django.shortcuts import render
from AppFamilia.forms import FamiliaForm,VecinosForm, MascotasForm
# Create your views here.

def inicio(request):
    plantilla=loader.get_template('AppFamilia/index.html')   #Leemos el archivo y lo guardamos en una variable


    documento=plantilla.render()

    return HttpResponse(documento)


def familiarForm(request):

    if request.method=='POST':
        form=FamiliaForm(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            nombre=info["nombre"]
            apellido=info["apellido"]
            edad=info["edad"]
            fecha_de_nacimiento=info["fecha_de_nacimiento"]

            familiar=Familia(nombre=nombre, apellido=apellido, edad= edad, fecha_de_nacimiento= fecha_de_nacimiento)
            familiar.save()
            return render (request, "Appfamilia/index.html")    
    else:
        form=FamiliaForm()
    return render (request, "Appfamilia/familiarForm.html", {"formulario": form})


def mascotaForm(request):

    if (request.method=="POST"):
        form=MascotasForm(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            apodo=info["apodo"]
            raza=info["raza"]
            edad=info["edad"]
        
            mascota=Mascotas(apodo=apodo, raza=raza, edad= edad)
            mascota.save()
            return render (request, "AppFamilia/index.html")    
    else:
        form=MascotasForm()
    return render (request, "AppFamilia/mascotaForm.html", {"formulario": form})


def vecinoForm(request):

    if (request.method=="POST"):
        form=VecinosForm(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            nombre=info["nombre"]
            direccion=info["direccion"]
        
            vecino=Vecinos(nombre=nombre, direccion=direccion)
            vecino.save()
            return render (request, "AppFamilia/index.html")    
    else:
        form=VecinosForm()
    return render (request, "AppFamilia/vecinoForm.html", {"formulario": form})



def busquedaVecino(request):
    return render (request, "Appfamilia/busquedaVecino.html")

def buscar(request):
    if request.GET["nombre"]:
        nom=request.GET["nombre"]
        vecinos=Vecinos.objects.filter(nombre__icontains=nom)
        return render (request, "Appfamilia/resultadosBusqueda.html", {"vecinos":vecinos})
    else:
        return render(request, "Appfamilia/busquedaVecino.html", {"error": "No se ingreso ningun nombre" })