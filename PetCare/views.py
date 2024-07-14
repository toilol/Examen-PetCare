from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
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

def login_view(request):
    # Renderiza la página de inicio de sesión (login.html)
    return render(request, 'login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige a la página de inicio después del inicio de sesión exitoso
            return redirect('index')
        else:
            # Maneja el caso de inicio de sesión fallido
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'login.html')
    else:
        # Si no es un POST request, muestra el formulario de inicio de sesión
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')