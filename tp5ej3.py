################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def trib(n):
    if n < 3:
        return n
    return trib(n-1) + trib(n-2) + trib(n-3)

def prueba():
    mensaje="tribonacci"
    saludo(mensaje)
    
    n=int(input("Ingrese termino: "))
    while n <= 0:
        n=int(input("Valor incorrecto. Ingresar valor positivo: "))
        
    trib(n)
    print("Resultado es:",trib(n))
    
if __name__ == "__main__":
    prueba()

