################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def paridad(numero):
    temp=bin(numero)
    n = str(temp)
    if int(n[len(n)-1]) ==0:
        return True
    else:
        return False
def prueba():
    saludo="Pares e impares "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese un número: "))
    resultado=paridad(numero)
    paridad(numero)
    print(paridad(numero))
    
    
if __name__ == "__main__":
    prueba()