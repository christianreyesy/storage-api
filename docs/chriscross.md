# Chris-Cross

>Deseamos realizar un sistema de registro de ciclistas donde se le pedirá al usuario datos personales y su registro de algún evento que va participar y cual fue su ultimo registro de tiempo y distancia que recorrió en ese tiempo.
> Se realizara un registro de datos de un competidor en la disciplina de ciclismo.

> Donde presentara las siguientes pantallas:

# MODULO DE CAPTURA DE DATOS PERSONALES
1. NOMBRE
2. EDAD
3. DOMICILIO 1
4. DOMICILIO 2
5. TELEFONO 1
6. TELEFONO 2
7. FECHA DE NACIMIENTO
8. CORREO ELECTRONICO
9. TIPO DE BICICLETA
  A) MONTAÑA
  B) RUTA
# MODULO DE REGISTRO DEL EVENTOS
1. NOMBRE DE EVENTO
2. DISTANCIA DE LA ACTIVIDAD
3. POR ETAPAS
  A) DE UNA SOLA ETAPAS
  B) DE VARIAS ETAPAS
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
- Participantes(Id_Participante, No.participante, Nombre, edad, Domicilio, Colonia,Telefono_casa, No celular, Fecha_Nac, correo_electronico, Tipo_bicileta)
- Eventos(Id_evento, NOmbre_del_evento, Distancia_evento)

POST / Participantes /New
{"Id_Participante","No.participante","Nombre","Edad","Domicilio","Colonia","Telefono_casa","No_celular","Fecha_Nac","Correo_electronico","Tipo_bicileta"}

POST /Eventos/New 
