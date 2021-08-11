import bottle
import datetime as dt
from modules.bottles import BottleJson
from modules.chriscross import guardar_participante

app = BottleJson()

@app.post("/participante")
def post_de_participante():
    """
    Ejemplo de solicitud con curl

    ```
    curl http://localhost:8080/chriscross/participante \
        -X POST \
        -H "Content-Type: application/json" \
        -d '{"nombre":"foo", "edad": 1, "fecha": "2021-01-10"}'
    ```
    """
    try:
        # Aqui codificacmos toda la logica que pueda
        # fallar debido a malformaciones de datos
        # proporcinados por el usuario.
        payload = bottle.request.json
        edad = payload["edad"]
        nombre = payload["nombre"]
        # uso de la funcion `dt.date.fromisoformat`
        # para interpetar la fecha a de formato iso.
        fecha = dt.date.fromisoformat(payload["fecha"])
        # llamada a la funcion asistente en 
        # `modules/chriscross.py`.
        guardar_participante(
            nombre=nombre,
            edad=edad,
            fecha=fecha.isoformat(), # codificacion de la fecha a cadena de texto en format iso.
        )
    except Exception as e:
        # bloque que se ejecuta cuando ocurre algun fallo
        print(e)
        raise bottle.HTTPError(500, "Error en los datos")
    # si no hay fallo aqui continua el codigo.
    raise bottle.HTTPError(201, "Registrado")
