from django.shortcuts import render,redirect,get_object_or_404
from .models import Servicio
from .forms import ServicioForm
# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html', context)

def crud(request):
    servicio = Servicio.objects.all()
    return render(request, 'crud.html', {'servicios': servicio})

def editar(request, servicio_id):
    servicio = get_object_or_404(Servicio, id_servicio=servicio_id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio)  # Añade request.FILES aquí
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'editar.html', {'form': form})

def agregar(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = ServicioForm()
    return render(request, 'agregar.html', {'form': form})

def borrar(request,pk):
    context={}
    try:
        servicio = Servicio.objects.get(id_servicio=pk)
        servicio.delete()
        mensaje= "datos eliminados"
    except Servicio.DoesNotExist:
        mensaje= "error, el servicio no existe"

    servicios = Servicio.objects.all()
    context = {'servicios': servicios, 'mensaje': mensaje}
    return render(request, 'crud.html', context)

def carrito(request):
    servicio = Servicio.objects.all()  # Obtener todos los servicios
    context = {
        'servicios': servicio
    }
    return render(request, 'carrito.html', context)