## Chris-Cross
>Autor: Reyes Christian

___


# Concepto de la aplicación ##

>Deseamos realizar un sistema de registro de ciclistas donde se le pedirá al usuario datos personales y su registro de algún evento que va participar y cual fue su ultimo registro de tiempo. Cada evento tiene una distancia total.
> Se realizara un registro de datos de un competidor en la disciplina de ciclismo.

___

# Aplicación

> Este proyecto se puede usar para los eventos que hay de competencia de ciclismo, donde se lleva registros a los eventos y se lleva un record del ciclista.

___


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
3. Fecha del eveto

# MODULO DE CONSULTA

1. Id del participante
      . Nombre del participante
      . Numero de participante
      . Nombre del evento
      . Fecha del evento
      . Distancia
      . FECHA DEL EVENTO.
3. REPORTES
  A) TIEMPO PROMEDIO POR SEMANA
      a) Distancia 20.
      b) Distancia 30.
      c) Distancia 40.
      d) Distancia 50.
      e) Distancia 60.



# Descripción de la aplicación

  La aplicación tendrá el objetivo de llevar el registro de un ciclista
y para saber historial de participaciones en eventos donde sepamos el
record que lleva como la distancias que ha recorrido y tiempo que realizo
por evento.


. Registro de datos del Participantes
  Aquí llevara los datos generales como es numero que identifica el
  registro del participante, nombre del participante, domicilio, colonia,
  teléfono tanto de casa como un numero de celular, fecha de nacimiento.
. Registro de eventos que existen donde los participantes pueden registrarse
  donde se captura fecha cuando va ser al evento que se esta registrando, la
  distancia que cuenta el recorrido del evento.
. Reportes del ciclista.


  En este área del programa la finalidad que tiene es llevar el registro de
  los eventos que ha participado

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


# Evaluación - Computo en la Nube

> Este proyecto llevara el registro de participantes de deportistas que practican la disciplina de ciclismo llevando sus datos personales y eventos que se hayan registrado. Así poder consultar tanto para ver sus datos generales como los eventos que hayan participado.

# Funcionamiento generales

## Commit

- Crear un fork del proyecto storage-api

- Entregable, señalar cual es el commit-hash, a partir del que ustedes realizaron el fork:

| Concepto | Commit Hash |
| --- | --- |
| Creación de Fork | 7c205d3b455c24d48a96b01fac200d858da39a52|

- Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones

- Entregable, señalar el commit-hash que contiene la creacion de dichos archivos. - Archivos en. /docs,./routes,./modules,./models, nombrados con el slug de su proyecto.

| Concepto | Commit Hash |
| --- | --- |
| Creación de docs/chriscross | e7020945a9f1aaf477393f10313c56b2361682b9 |

# Mock-Ups

> Para hacer una mejor planificación del proyecto, se ocupa realizar un bosquejo de como quedaría el proyecto de manera visual de manera gráfico y para esto debemos de realizar bosquejos de como queremos que quede el proyecto de manera visual.

> En la siguiente figura es la pantalla tentativamente quedaría como se muestra en la imagen. Es la pantalla de captura de datos de los participantes, donde se les pide nombre, edad, fecha de nacimiento. Para que quede grabado la información hay que presionar el botón de guardar o en caso que se quiera cancelar el proceso de captura se le debe presionar el botón de cancelar.

![/](/usuarios/mac/github/storage-api/docs/pantalla de registro.png)


## En proceso de edición

# Casos de uso.

## Agregar participantes


> El usuario puede agregar participantes para la actividad de ciclismo.
> curl http://localhost:8080/chriscross/participante \
      -X POST \
      -H "Content-Type: application/json" \
      -d '{"id_part":10,nombre":"foo", "edad": 1, "fecha": "2021-01-10"}

## Agregar eventos.

> El usuario puede agregar diferentes eventos cons us fechas que se van ha realizar y especificar la distancia total del recorrido

>curl http://localhost:8080/chriscross/evento \
        -X POST \
        -H "Content-Type: application/json" \
        -d '{"nombre_evento":"rosarito_ensenada", "distancia": 80, "fecha": "2021-01-10"}

## Consultar información de participantes

> Esta en construcción, pendiente

## Consulta de eventos.

> Esta en construcción, pendiente


# Documentación para el proyecto

 Después de que se termine el desarrollo del código del proyecto que aun esta en construcción, debemos de realizar un análisis sobre las áreas de oportunidades que tuvimos y los aciertos para poder documentarlo y que posteriormente puedan otros colaboradores seguir con el desarrollo o mejoramiento del proyecto.
