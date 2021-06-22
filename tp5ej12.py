################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def comparar(lista1,lista2):
    lista1.sort()
    lista2.sort()
    if lista1==lista2:
        return True
    else:
        return False
    
def prueba():
    mensaje="comparación de listas"
    saludo(mensaje)
    
    lista1=[]
    lista2=[]
    ingreso1=0
    ingreso2=0
    
    while ingreso1 != "":
        ingreso1=input("\x1b[0;46mIngrese contenido de la lista 1: "+"\x1b[0;37m"+"\x1b[0;31m")
        lista1.append(ingreso1)
    else:
        lista1.pop()
    
    while ingreso2 != "":
        ingreso2=input("\x1b[0;44mIngrese contenido de la lista 2: "+"\x1b[0;37m"+"\x1b[0;31m")
        lista2.append(ingreso2)
    else:
        lista2.pop()
    
    comparar(lista1, lista2)
    
    resultado=comparar(lista1,lista2)
    if resultado==True:
        print("\x1b[0;42m",resultado,"\x1b[0;37m")
    else:
        print("\x1b[0;41m",resultado,"\x1b[0;37m")
    


if __name__ == "__main__":
    prueba()
    

