################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def a_binario(num):
    num_binario=format(num,"b")
    return num_binario

def a_numero(binario):
    num_normal=int(binario,2)
    return num_normal

def prueba():
    mensaje="Texto binario"
    saludo(mensaje)
    num=int(input("Ingrese número: "))
    binario=input("Ingrese binario: ")
    a_binario(num)
    a_numero(binario)
    resultado=a_binario(num)
    resultado_1=a_numero(binario)
    
    print(f"\nEl numero ingresado es: {num}")
    print(f"El numero en binario es: {resultado}")
    print(f"\nEl binario ingresado es: {binario}")
    print(f"El numero convertido es: {resultado_1}")
    
if __name__ == "__main__":
    prueba()

