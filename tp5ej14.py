################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def es_capicua(num):
    reverse_txt= num[::-1]
    if num==reverse_txt:
        return True
    else:
        return False

def prueba():
    mensaje="Numeros Capicúa"
    saludo(mensaje)
    num=input("Ingrese número: ")
    resultado=es_capicua(num)
    print(resultado)
if __name__ == "__main__":
    prueba()