from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from arriendos.forms import RegistroUsuarioForm, SolicitudArriendoForm
from arriendos.models import Inmueble
from arriendos.services import borrar_inmueble

# Create your views here.
def index(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'index.html', {'inmuebles': inmuebles})

def detalle_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    return render(request, 'detalle_inmueble.html', {'inmueble':inmueble})

@login_required
def solicitud_arriendo(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    # if request.user.is_authenticated and request.user.usuario.tipo_usuario == 'arrendatario':
    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST)
        if form.is_valid():
            print("Es valido ", form.is_valid())
            solicitud = form.save(commit=False)
            solicitud.arrendatario = request.user.usuario
            solicitud.inmueble = inmueble
            solicitud.save()
    
    return redirect('index')

def eliminar_inmueble(request, id):

    if request.user.is_superuser:
        borrado = borrar_inmueble(id)
        if borrado:
            return redirect('index')
        else:
            print("NO SE BORRO")
            return redirect('index')
    
    print("No tienes permisos para hacer esto")
    return redirect('index')


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Para poder guardar la contraseña de forma encriptada
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registration/registrate.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = '/'