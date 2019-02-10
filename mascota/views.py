from django.shortcuts import render, redirect
from .forms import MascotaForm
from .models import Mascota

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


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')

    context = {'mascotas': mascota}

    return render(request, 'mascota/mascota_list.html', context)


def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)

    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')

    return render(request, 'mascota/mascota_form.html', {'form': form})


def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})
