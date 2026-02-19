#Algoritmo 2: Rutina para LOGIN de usuario con correo y contraseña, se permiten hasta 3 intentos

#Variables de datos almacenados en BD
correoBD="correo@gmail.com"
contraseñaBD="admin123"


intentosPermitidos=3
contadorIntentos=0

#ciclo para controlar el numero de intentos
while contadorIntentos<intentosPermitidos:

    #Variables que digita el usuarios
    correoDigitado=input("Digita tu correo: ")
    contraseñaDigita=input("Digita tu contraseña: ")

    #Evaluar si el login es efectivo
    if correoDigitado==correoBD and contraseñaDigita==contraseñaBD:
        print("ok")

        #Se rompe/termina el ciclo
        break

    else:
        print("falle")
        contadorIntentos+=1

#Necesito mensajes que indiquen el numero de intentos que llevo y cuantos me quedan