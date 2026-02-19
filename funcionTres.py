#Algoritmo 3:

def calcular_promedio(mediciones):
    for medicion in mediciones:
        sumar+=medicion
    promedio=sumar/len(mediciones)
    return promedio
    

def clasificar_promedio(promedioMedicion):
    if promedioMedicion>0 and promedioMedicion<=250:
        return("Operacion detenida por falta de agua")
    elif promedioMedicion>250 and promedioMedicion <=400:
        return("operando con normalidad")
    else:
        return("Deben abrirse las compuertas de la represa")

   