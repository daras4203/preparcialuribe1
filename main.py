#Centralizamos en llamado a las funciones y ejecutar solo este codigo
from funcionUno import crear_lista_ingenieros
from funcionDos import autenticar_usuario
from funcionTres import calcular_promedio,clasificar_promedio

#Ejecutar la logica de negocio

#como incluir en el main la funcion 1
#1. Datos quemados que simulen una BD
correoBD="correo@gmail.com"
contraseñaBD="admin123"

#2. Ejecutamos la funcion de login

todoSaliobien=autenticar_usuario(correoBD,contraseñaBD,3)

#. Ejecutar el codigo dependiendo del login
if todoSaliobien:
    #4. Crear la lista de mediciones
    mediciones=[120,250,340,500,301,310,300,40,87,500]

    #5. Obtener el promedio de las mediciones
    promedio=calcular_promedio(mediciones)

    #6. Clasificar segun el promedio la operacion
    estadoOperacion=clasificar_promedio(promedio)

    print(estadoOperacion)
else:
    print("😣 No se continua por que el login no fue exitoso")