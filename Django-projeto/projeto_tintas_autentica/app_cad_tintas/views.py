from django.shortcuts import render
from .models import tinta

def home(request):
    return render (request,'tintas/home.html')

def tintas(request):
    colors = tinta ()
    colors.marca = request.POST.get('marca')
    colors.modelo = request.POST.get('modelo')
    colors.ano = request.POST.get('ano')
    colors.cor = request.POST.get('cor')
    colors.codigo = request.POST.get('codigo')
    colors.save()
    tintas = {
        'tintas': tinta.objects.all()
    }

    return render(request, r'tintas/autenticacolor.html', tintas)