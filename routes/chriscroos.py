import json
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord

app = BottleJson()

def almacenar_dato(Nombre = None, Edad=None, Fech_Nac = None):
    print ("Datos del participante")
    print (Nombre, Edad, Fecha)
    para_almacenar = {"Nombre": Nombre, "Edad": Edad, "Fecha": Fech_Nac}
    json_text = json.dumps (para almacenar)
    store_string('mi-carpeta', nombre, para_almacenar)
    return "Exito"
