from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Arreglo de tuplas para las comunas de la Región Metropolitana de Santiago
# Arreglo de tuplas para las comunas de la Región Metropolitana de Santiago
COMUNAS_REGION_METROPOLITANA = [
    ("alhue", "Alhué"),
    ("buin", "Buin"),
    ("calera_de_tango", "Calera de Tango"),
    ("cerrillos", "Cerrillos"),
    ("cerro_navia", "Cerro Navia"),
    ("colina", "Colina"),
    ("conchali", "Conchalí"),
    ("curacavi", "Curacaví"),
    ("el_bosque", "El Bosque"),
    ("el_monte", "El Monte"),
    ("estacion_central", "Estación Central"),
    ("huechuraba", "Huechuraba"),
    ("independencia", "Independencia"),
    ("isla_de_maipo", "Isla de Maipo"),
    ("la_cisterna", "La Cisterna"),
    ("la_florida", "La Florida"),
    ("la_granja", "La Granja"),
    ("la_pintana", "La Pintana"),
    ("la_reina", "La Reina"),
    ("lampa", "Lampa"),
    ("las_condes", "Las Condes"),
    ("lo_barnechea", "Lo Barnechea"),
    ("lo_espejo", "Lo Espejo"),
    ("lo_prado", "Lo Prado"),
    ("macul", "Macul"),
    ("maipu", "Maipú"),
    ("melipilla", "Melipilla"),
    ("nunoa", "Ñuñoa"),
    ("padre_hurtado", "Padre Hurtado"),
    ("penaflor", "Peñaflor"),
    ("penalolen", "Peñalolén"),
    ("pirque", "Pirque"),
    ("puente_alto", "Puente Alto"),
    ("providencia", "Providencia"),
    ("pudahuel", "Pudahuel"),
    ("quilicura", "Quilicura"),
    ("quinta_normal", "Quinta Normal"),
    ("recoleta", "Recoleta"),
    ("renca", "Renca"),
    ("san_bernardo", "San Bernardo"),
    ("san_joaquin", "San Joaquín"),
    ("san_jose_de_maipo", "San José de Maipo"),
    ("san_miguel", "San Miguel"),
    ("san_pedro", "San Pedro"),
    ("san_ramon", "San Ramón"),
    ("santiago", "Santiago"),
    ("talagante", "Talagante"),
    ("til_til", "Til Til"),
    ("vitacura", "Vitacura"),
]


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
    TIPO_INMUEBLE_CHOISES = [
        ('casa','Casa'),
        ('departamento','Departamento'),
        ('parcela','Parcela'),
    ]
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='img/inmuebles/')
    precio=models.DecimalField(max_digits=10, decimal_places=0)
    comuna = models.CharField(max_length=50, choices=COMUNAS_REGION_METROPOLITANA)
    disponible=models.BooleanField(default=True)
    m2_construidos = models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_estacionamientos = models.PositiveIntegerField()
    cantidad_habitaciones = models.PositiveIntegerField()
    cantidad_banos = models.PositiveIntegerField()
    tipo_de_inmueble=models.CharField(max_length=12, choices=TIPO_INMUEBLE_CHOISES)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    


class SolicitudArriendo(models.Model):
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    mensaje = models.TextField(blank=True)
    def __str__(self):
        return f"Solicitud de {self.inmueble.nombre} por {self.arrendatario.nombres} {self.arrendatario.apellidos}"    