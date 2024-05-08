# Proyecto Inmobiliaria - Módulo 7 - Hito 2. Bootcamp Python

## Participante: Andrea Gutierrez
## Los Requeriemientos de este desafio con imagenes detalladas de las tablas, se encuentra en la carpeta Hito/Hito2.pdf 

### 1. Utilizando las migraciones realice lo siguiente:
 
#### a. Poblar la base de datos con todas las regiones y comunas de Chile usando loaddata. (2 puntos) 
#### b. Poblar de tipos de inmuebles en la base de datos usando loaddata. (2 puntos) 
#### c. Poblar la base de datos con varios inmuebles y usuarios usando loaddata. (1 punto).

## Solución:

#### a. Para poblar la base de datos con todas las regiones de Chile y sus respectivas comunas, se creó un json con el nombre regiones.json (Ubicado en /arriendos/fixtures/regiones.json) y luego se cargó la data con el comando:

```bash
python3 manage.py loaddata arriendos/fixtures/regiones.json
````

#### b. Para poblar de tipos de inmuebles en la base de datos usando loaddata, primero  se creó un modelo TipoInmueble, a partir de este modelo se creó un json con el nombre tipo_de_inmueble.json (Ubicado en /arriendos/fixtures/tipo_de_inmueble.json) y luego se cargó la data con el comando:
```bash
python3 manage.py loaddata arriendos/fixtures/tipo_de_inmueble.json
```

#### c.Poblar la base de datos con varios inmuebles y usuarios usando loaddata se creó un json con el nombre inmuebles.json (Ubicado en /arriendos/fixtures/inmuebles.json) y luego se cargó la data con el comando:
```bash
python3 manage.py loaddata arriendos/fixtures/arriendos.json
```
#### c1. Para poblar la base de datos con varios usuarios usando loaddata se creó un json con el nombre usuarios.json (Ubicado en /arriendos/fixtures/usuarios_nuevos.json) y luego se cargó la data con el comando:
```bash
python3 manage.py loaddata arriendos/fixtures/usuarios_nuevos.json
```
##

### 2. Consultar listado de inmuebles para arriendo separado por comunas, solo usando los campos "nombre" y "descripción" en un script python que se conecta a la DB usando DJango y SQL guardando los resultados en un archivo de texto. (3 Puntos)

## Solución:

#### Para este requerimiento se creó un archivo script_comuna.py que contiene todo el código python para hacer la consulta en base de datos a través del ORM de Django.

#### La respuesta de la ejecución de este archivo se encuentra en el archivo inmuebles_por_comuna.txt tal como lo solicita el desafío.

##

### 3.Consultar listado de inmuebles para arriendo separado por regiones en un script python que se conecta a la DB usando DJango y SQL guardando los resultados en un archivo de texto. (2 Puntos)

## Solución:

#### Para este requerimiento se creó un archivo script_region.py que contiene todo el código python para hacer la consulta en base de datos a través del ORM de Django.

#### La respuesta de la ejecución de este archivo se encuentra en el archivo inmuebles_por_region.txt tal como lo solicita el desafío.