# script_consultar_inmuebles.py

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()
from arriendos.models import Inmueble, Region  

output_filename = "inmuebles_por_region.txt"

with open(output_filename, "w") as f:
    regiones = Region.objects.all()
    for region in regiones:
        f.write(f"Region: {region.nombre}\n")
        inmuebles = Inmueble.objects.filter(comuna__region=region, disponible=True)
        if inmuebles:
            for inmueble in inmuebles:
                f.write(f"  Inmueble: {inmueble.nombre}\n")
                f.write(f"    Dirección: {inmueble.direccion}\n")
                f.write(f"    Precio: {inmueble.precio}\n")
                f.write(f"    Descripción: {inmueble.descripcion}\n")
                f.write(f"    Tipo de Inmueble: {inmueble.tipo_de_inmueble}\n")
                f.write(f"    Comuna: {inmueble.comuna}\n")
                f.write(f"    Propietario: {inmueble.propietario}\n")
        else:
            f.write("  No hay inmuebles disponibles para arriendo en esta región.\n")
        f.write("\n")  
print(f"Los resultados se han guardado en {output_filename}")
