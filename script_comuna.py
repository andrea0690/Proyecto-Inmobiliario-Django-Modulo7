import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()

from arriendos.models import Inmueble, Comuna

with open("inmuebles_por_comuna.txt", "w", encoding="utf-8") as f:
    comunas = Comuna.objects.all()
    for comuna in comunas:
        f.write(f"Comuna: {comuna.nombre}\n")
        inmuebles = Inmueble.objects.filter(comuna=comuna, disponible=True)
        for inmueble in inmuebles:
            f.write(f" - Nombre: {inmueble.nombre}\n")
            f.write(f"   Descripción: {inmueble.descripcion}\n")
        f.write("\n")
