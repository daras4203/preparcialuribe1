#algoritmo 1: Crear una lista de 5 ingenieros (1 ingeniero es un diccionario)

def crear_lista_ingenieros(cantidadIngenieros):
    ingenieros=[]
    
    for _ in range(cantidadIngenieros):
        nuevoIngeniero={}
        nuevoIngeniero[id]=int(input("id:  "))
        nuevoIngeniero["nombres"]=input("nombres:  ")
        ingenieros.append(nuevoIngeniero)
    return ingenieros
#Funcion crear una lista de ingeniero





    