################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def inversion(texto):
    texto_inverso=texto.swapcase()
    return texto_inverso
def prueba():
    mensaje="inversión de mayúsculas"
    saludo(mensaje)
    texto=input("Ingrese texto: ")
    inversion(texto)
    
    resultado=inversion(texto)
    print(f"\x1b[0;42m El texto ingresado es:\x1b[0;37m {texto}")
    print(f"\x1b[0;41m El texto invertido es:\x1b[0;37m {resultado}") 

if __name__ == "__main__":
    prueba()

