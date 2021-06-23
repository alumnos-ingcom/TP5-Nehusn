import random

def color_letra():
    num = random.randint(31,36)
    color=f"\x1b[{num};{num}m"
    return color

def color_fondo():
    num = random.randint(40,47)
    color=f"\x1b[{num};{num}m"
    return color

def color_rgb():
    letra = random.randint(31,36)
    fondo = random.randint(40,47)
    num=random.randint(0,7)
    color=f"\x1b[{num};{letra};{fondo}m"
    return color
def prueba():
    
    for i in range(0,100):
        color_a=color_rgb()
        print(f"{color_a}",i)