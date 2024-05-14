from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from arriendos.forms import RegistroInmuebleForm, RegistroUsuarioForm, SolicitudArriendoForm
from arriendos.models import Inmueble, SolicitudArriendo, Usuario
from arriendos.services import borrar_inmueble
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    inmuebles = Inmueble.objects.all()
    
    # Texto a buscar (Nombre de comuna o Region)
    query = request.GET.get('text_a_buscar')
    if query:
        inmuebles = inmuebles.filter(Q(comuna__region__nombre__icontains=query) | Q(comuna__nombre__icontains=query))
    
    if request.user.is_authenticated:
        solicitudes = SolicitudArriendo.objects.filter(inmueble__propietario=request.user, leido= False)
        request.session["solicitudes"] = len(solicitudes)

    return render(request, 'index.html', {'inmuebles': inmuebles, 'solicitudes': request.session.get("solicitudes", 0)})

def detalle_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    solicitudes = request.session.get("solicitudes", 0)
    return render(request, 'detalle_inmueble.html', {'inmueble':inmueble, 'solicitudes': solicitudes})

@login_required
def solicitud_arriendo(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)

    if not inmueble.disponible:
        return redirect('error_500')
    
    # if request.user.is_authenticated and request.user.usuario.tipo_usuario == 'arrendatario':
    if request.method == 'POST':
        form = SolicitudArriendoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.arrendatario = request.user.usuario
            solicitud.inmueble = inmueble
            solicitud.save()

            messages.success(request, '¡La operación se ha completado con éxito!')
    
    return redirect('index')

@login_required
def eliminar_inmueble(request, id):
    borrado = borrar_inmueble(request.user, id)
    if borrado:
        return redirect('dashboard', estado = 0)
    else:
        print("NO SE BORRO")
        return redirect('error_500')

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registrate.html', {'form': form, 'solicitudes': 0})

@login_required
def crear_inmueble(request):
    if request.method == 'POST':
        form = RegistroInmuebleForm(request.POST, request.FILES)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user.usuario
            inmueble.save()
            return redirect('dashboard', estado = 0) 
    else:
        form = RegistroInmuebleForm()
    return render(request, 'registro_inmueble.html', {'form': form})

@login_required
def actualizar_inmueble(request, id):
    inmueble = get_object_or_404(Inmueble, pk=id)
    if request.method == 'POST':
        form = RegistroInmuebleForm(request.POST, request.FILES, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('dashboard', estado = 0)
    else:
        form = RegistroInmuebleForm(instance=inmueble)
        
    return render(request, 'editar_inmueble.html',{'form':form, 'id': id })

@login_required
def actualizar_datos(request):
    u = get_object_or_404(Usuario, id=request.user.id)

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, instance=u)
        if form.is_valid():

            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            if password:
                user.set_password(password)

            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUsuarioForm(instance=u)

    return render(request, 'actualizacion_datos.html', {'form': form, 'solicitudes': request.session.get("solicitudes", 0)})

@login_required
def mis_solicitudes(request):
    user = request.user
    if user.usuario.tipo_usuario == 'arrendador':
        is_arrendador = True
        solicitudes = SolicitudArriendo.objects.filter(inmueble__propietario=user)
        for sol in solicitudes:
            sol.leido = True
            sol.save()
            request.session["solicitudes"] = 0
    else:
        is_arrendador = False
        solicitudes = SolicitudArriendo.objects.filter(arrendatario=user)

    return render(request,'mis-solicitudes.html', {
        'solicitudes': request.session.get("solicitudes", 0), 
        'interesados': solicitudes,
        'is_arrendador': is_arrendador
    })

def ayuda(request):
    return render(request, 'ayuda.html')

def error_500(request):
    return render(request, 'error_500.html')

def dashboard(request, estado=0):
    inmuebles = Inmueble.objects.filter(propietario=request.user)
    return render(request, 'dashboard.html', {'inmuebles': inmuebles, 'estado': estado})

@login_required
def cambio_estado_solicitud(request):
    estado = request.POST.get("opciones")
    id = request.POST.get("solicitud")

    solicitud = get_object_or_404(SolicitudArriendo, pk=id)
    solicitud.estado = estado
    if estado == "aceptada":
        solicitud.inmueble.disponible = False
        solicitud.inmueble.save()
    solicitud.save()
    return redirect('dashboard', estado = 0)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = '/'