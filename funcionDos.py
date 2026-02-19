#algoritmo 2:


def autenticar_usuario(correoRegistrado,contraseñaRegistrada,numeroIntentos):

    for intento in range(1,numeroIntentos):
        correo=input("ingrese su correo: ")
        contraseña=input("ingrese su contraseña: ")

        if correo==correoRegistrado and contraseña==contraseñaRegistrada:
            print("🤙 Login ok")
            return True
        else:
            #calcular el numero de intentos restantes
            print("❎Fallaste en el Login")
    return False
