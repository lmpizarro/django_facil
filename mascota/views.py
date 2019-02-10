from django.shortcuts import render, redirect
from .forms import MascotaForm

# Create your views here.

def index(request):
    return render(request, 'mascota/index.html')



def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:index')
    else:
        form = MascotaForm()

    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_crear(request):
    pass


def mascota_listar(request):
    pass
