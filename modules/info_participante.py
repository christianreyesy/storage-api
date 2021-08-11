from os import environ, urandom
import hashlib
import datetime
from bottle import response, request
import jwt
import binascii
from functools import wraps
import models.auth as mauth







import json
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)


#
# ...
#

def almacenar_datos(id_participante=None, nombre=None, edad=None, domicilio=None,colonia=None):
    print("Desde modulo almacenar_datos")
    print(id_partipante,nombre, edad, domicilio,colonia)
    para_almacenar = {"id_partipante": id_partipante,"nombre": nombre, "edad": edad, "domicilio":domicilio, "colonia" :colonia}
    nombre_de_archivo = f"{id_partipante}-{nombre}.json"
    datos = store_string(
        "vg_info/Carpeta",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return datos

    def almacenar_eventos(id_partipante=None, id_evento=None, nomb_evento=None, distancia_evento=None,fecha_evento=None):
        print("Desde modulo almacenar_eventos")
        para_almacenar = {"id_partipante":id_partipante, "id_evento":id_evento, "nomb_evento":nomb_evento,"fecha_evento":fecha_evento}
        json_text = json.dumps(para_almacenar)
        nombre_de_archivo=f"{id_partipante}-{id_evento}-{nomb_evento}.json"
        datos = store_string (
        "vg_info/Carpeta2",
        nombre_de_archivo,
        json.dumps(para_almacenar)
        )

        pass
