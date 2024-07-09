from django.shortcuts import render,redirect,get_object_or_404
from .models import Servicio
from .forms import ServicioForm
# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html', context)

def crud(request):
    servicio = Servicio.objects.all()
    return render(request, 'crud.html', {'servicio': servicio})
