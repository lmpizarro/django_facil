# Create your views here.

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'adopcion/index.html')


def solicitud_crear(request):
    pass

def solicitud_listar(request):
    pass
