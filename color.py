import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def color_letra():
    num = random.randint(31,36)
    color=f"\x1b[0;{num}m"
    return color
    
def prueba():
    
    for i in range(0,100):
        color_a=color_letra()
        print(f"{color_a}",i)

prueba()