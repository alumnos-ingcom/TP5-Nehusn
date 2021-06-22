################
# Gastón Nehuen Rodriguez Valdez - @nehusn
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from saludo import saludo
def fibonacci(nterm,n1,n2):
    cont = 0
    while cont < nterm:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        cont=cont+1
    return n1
    
def prueba():
    mensaje="fibonacci"
    saludo(mensaje)
    n1, n2 = 0, 1
    nterm=int(input("Que término?: "))
    
    while nterm <= 0:
        nterm=int(input("Valor incorrecto. Ingresar valor positivo: "))
    if nterm == 1:
        print(f"Secuencia hasta {nterm}: ")
        print(n1)
    else:
        fibonacci(nterm,n1,n2)
    
    print("Resultado es: ",fibonacci(nterm,n1,n2))
    
if __name__ == "__main__":
    prueba()

