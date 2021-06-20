################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def paridad(numero):
    temp=bin(numero)
    n = str(temp)
    if int(n[len(n)-1]) ==0:
        return True
    else:
        return False
def prueba():
    mensaje="Par o Impar"
    saludo(mensaje)
    numero=int(input("Ingrese un número: "))
    resultado=paridad(numero)
    paridad(numero)
    print(paridad(numero))
    
    
if __name__ == "__main__":
    prueba()