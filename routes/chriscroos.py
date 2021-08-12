import bottle
import datetime as dt
from modules.bottles import BottleJson
from modules.chriscross import guardar_participante
from modules.chriscross import guardar_eventos
app = BottleJson()

@app.post("/participante")
def post_de_participante():
    """
    Ejemplo de solicitud con curl

    ```
    curl http://localhost:8080/chriscross/participante \
        -X POST \
        -H "Content-Type: application/json" \
        -d '{"id_part":10,nombre":"foo", "edad": 1, "fecha": "2021-01-10"}'
    ```
    """
    try:
        # Aqui codificacmos toda la logica que pueda
        # fallar debido a malformaciones de datos
        # proporcinados por el usuario.

        payload = bottle.request.json
        id_part = payload["id_part"]
        nombre = payload["nombre"]
        edad = payload["edad"]

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

    @app.post("/evento")
    def post_de_evento():
        """
        Ejemplo de solicitud con curl

        ```
        curl http://localhost:8080/chriscross/evento \
            -X POST \
            -H "Content-Type: application/json" \
            -d '{"nombre_evento":"rosarito_ensenada", "distancia": 80, "fecha": "2021-01-10"}'
        ```
        """
        try:
            # Aqui codificacmos toda la logica que pueda
            # fallar debido a malformaciones de datos
            # proporcinados por el usuario.

            payload = bottle.request.json
            id_evento = payload["id_evento"]
            nombre_evento = payload["nombre_evento"]
            distancia=payload["distancia"]

            # uso de la funcion `dt.date.fromisoformat`
            # para interpetar la fecha a de formato iso.
            fecha = dt.date.fromisoformat(payload["fecha"])
            # llamada a la funcion asistente en
            # `modules/chriscross.py`.
            guardar_participante(
                id_evento=id_evento,
                nombre_evento=nombre_evento,
                distancia=distancia,
                fecha=fecha.isoformat(), # codificacion de la fecha a cadena de texto en format iso.
            )
        except Exception as e:
            # bloque que se ejecuta cuando ocurre algun fallo
            print(e)
            raise bottle.HTTPError(500, "Error en los datos")
        # si no hay fallo aqui continua el codigo.
        raise bottle.HTTPError(201, "Registrado")
