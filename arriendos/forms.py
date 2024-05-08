from django import forms
from .models import SolicitudArriendo, Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario']
        widgets = {
            'password': forms.PasswordInput(),
        }

class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = ['inmueble', 'mensaje']