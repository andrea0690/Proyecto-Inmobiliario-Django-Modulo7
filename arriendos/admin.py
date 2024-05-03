from django.contrib import admin

from arriendos.models import Inmueble, SolicitudArriendo, Usuario

# Register your models here.


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(SolicitudArriendo)