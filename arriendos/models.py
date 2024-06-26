from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre},  {self.region}"
    
class TipoInmueble(models.Model):
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo


class Usuario(User):
    TIPO_USUARIO_CHOISES = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    ]
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=13)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOISES)
    correo_electronico = models.EmailField(unique=True, default='correo@correo.cl') 

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
        
        
        
class Inmueble(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=300)
    descripcion=models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='img/inmuebles/')
    precio=models.DecimalField(max_digits=10, decimal_places=0)
    comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.CASCADE)
    disponible=models.BooleanField(default=True)
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos = models.PositiveIntegerField()
    cantidad_habitaciones = models.PositiveIntegerField()
    cantidad_banos = models.PositiveIntegerField()
    tipo_de_inmueble = models.ForeignKey(TipoInmueble, related_name='inmuebles', on_delete=models.CASCADE)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    


class SolicitudArriendo(models.Model):
    ESTADO_SOLICITUD = [
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    ]
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    mensaje = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADO_SOLICITUD, default=ESTADO_SOLICITUD[0][0])

    def __str__(self):
        return f"Solicitud de {self.inmueble.nombre} por {self.arrendatario.nombres} {self.arrendatario.apellidos}"    