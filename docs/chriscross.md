# Chris-Cross

>Deseamos realizar un sistema de registro de ciclistas donde se le pedirá al usuario datos personales y su registro de algún evento que va participar y cual fue su ultimo registro de tiempo. Cada evento tiene una distancia total.
> Se realizara un registro de datos de un competidor en la disciplina de ciclismo.

> Donde presentara las siguientes pantallas:

# MODULO DE CAPTURA DE DATOS PERSONALES
1. NOMBRE
2. EDAD
3. DOMICILIO 1
4. Colonia
5. TELEFono de casa
6. Numero de celular
7. FECHA DE NACIMIENTO
8. CORREO ELECTRONICO


# MODULO DE REGISTRO DEL EVENTOS
1. NOMBRE DE EVENTO
2. DISTANCIA DE LA ACTIVIDAD
3. POR ETAPAS
  A) DE UNA SOLA ETAPAS
  B) DE VARIAS ETAPAS
4. Fecha del eveto

# MODULO DE CONSULTA
1. NOMBRE DE RUTA.
    A)FECHA DEL EVENTO.
      I)CALIFICACION *.
     II)CALIFICACION **.
    III)CALIFICACION ***
3. REPORTES
  A) TIEMPO PROMEDIO POR SEMANA.
      a) Distancia 20.
      b) Distancia 30.
      c) Distancia 40.
      d) Distancia 50.
      e) Distancia 60.
  B) TIEMPO PROMEDIO POR MES.
      a) Distancia 20.
      b) Distancia 30.
      c) Distancia 40.
      d) Distancia 50.
      e) Distancia 60.
> Tendrá las siguientes entidades:
# Implementación de la aplicación
## Entidades
- Participantes(Id_Participante, No.participante, Nombre, Edad, Domicilio, Colonia,Telefono_casa, No celular, Fecha_Nac, correo_electronico, Tipo_bicileta)
- Eventos(Id_evento, Nombre_del_evento, Distancia_evento,Fecha_evento)

POST / Participantes /New
{"Id_Participante","No.participante","Nombre","Edad","Domicilio","Colonia","Telefono_casa","No_celular","Fecha_Nac","Correo_electronico","Tipo_bicileta"}

POST /Eventos/New
{"Id_evento","NOmbre_del_evento","Distancia_evento","Fecha_evento"}

DELETE /Participantes/Id_Participante
UPDATE /Participantes/Id_Participante

GET /Participantes/<Id_Participante>/No.participante
GET /Participantes/<Id_Participante>/Edad
GET /Participantes/<Id_Participante>/Domicilio
GET /Participantes/<Id_Participante>/Telefono_casa
GET /Participantes/<Id_Participante>/No_celular
GET /Participantes/<Id_Participante>/Fecha_Nac
GET /Participantes/<Id_Participante>/Correo_electronico
