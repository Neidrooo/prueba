from django.shortcuts import get_object_or_404, render
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

def errores(request):
    try:
        producto = Producto.objects.get(pk=8)
        return render(request,'errores.html',{'producto':producto})
    except:
        return HttpResponse('ERROR HERMANITO MIO')
    
def entrada(request,id):
    producto = Producto.objects.get(pk=id)
    return render(request,'entrada.html',{'producto':producto})

def entrada_error(request,id):
    producto = get_object_or_404(Producto,pk=id)
    return render(request,'entrada_error.html',{'producto':producto})

def mostrar_subconjunto(request):
    producto = Producto.objects.all()
    return render(request,'mostrar_subconjunto.html',{'producto':producto})

def formulario(request,id):
    return render(request,'formulario.html',{'producto':producto,'productos':productos})

def elegir_vistas(request):
    productos = Producto.objects.all()
    return render(request,'elegir_vistas.html',{'productos':productos})

def guardar_bd(request,nombre):
    try:
        c = Categoria(nombre=nombre)
        c.save()
        return render(request,'guardar_bd.html')
    except:
        return HttpResponse('ERROR AL GUARDAR')
    