import json
from modules.storage import (
     store_string,
     storage_bytes,
     query_storage,
     get_storage_file
)


# funcion asistente que guardar los datos de usuario
def guardar_participante(id_part=None, nombre=None, edad=None, fecha=None):
    # estructuramos un diccionario de python para guardarlo
    #  como json.
    datos = {
        "id_part": id_part,
        "nombre": nombre,
        "edad": edad,
        "fecha": fecha,
    }
    # definimos el nombre del archivo a guardar.
    filename = f"{fecha}-{nombre.strip(' ')}.json"
    # funcion de almacenamiento de archivos
    store_string(
        "participantes", # definimos en que colleccion
        filename, # definimos el nombre del archivo
        json.dumps(datos) # definimos el contenido del archivo
    )


def guardar_eventos (id_evento=None, nomb_evento=None,fecha_evento=None,distancia)
    datos = {
        "id_evento": id_evento,
        "nomb_evento": nombre,
        "fecha_evento": fecha_evento,
        "distancia": distancia,
    }
    filename = f"{fecha_evento}-{nombre.strip(' ')}.json"
    storage_string(
    "eventos",
    filename,
    json.dumps (datos)
    )
