from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Producto,Categoria

# Create your views here.

def index(request):
    return HttpResponse ("Hola mundo")

def nombreProducto(request,Producto_id):
    p = Producto.objects.get(pk=Producto_id)
    return HttpResponse(p.nombre)

def mostrarTemplate(request):
    p=Producto.objects.all()
    return render(request,'hola.html',{'productos':p})

def mostrar(request):
    productos = Producto.objects.all()
    return render(request,'mostrar.html',{'productos':productos})