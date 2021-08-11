import json
from modules.storage import store_string


# funcion asistente que guardar los datos de usuario
def guardar_participante(nombre=None, edad=None, fecha=None):
    # estructuramos un diccionario de python para guardarlo
    #  como json.
    datos = {
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
