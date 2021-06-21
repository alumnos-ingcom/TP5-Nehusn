################
# Gastón Nehuen Rodriguez Valdez - @nehus
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def a_binario(num):
    num_binario=format(num,"b")
    return num_binario

def prueba():
    mensaje="Texto binario"
    saludo(mensaje)
    num=int(input("Ingrese número: "))
    a_binario(num)
    resultado=a_binario(num)
    print(f"El numero ingresado es: {num}")
    print(f"El numero en binario es: {resultado}")
    
if __name__ == "__main__":
    prueba()

