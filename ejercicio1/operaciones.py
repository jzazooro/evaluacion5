def suma(a, b):
    try:
        a=int(a)
        b=int(b)
    except ValueError:
        print("Error: los argumentos deben ser números enteros")
    return a+b

def resta(a, b):
    try:
        a=int(a)
        b=int(b)
    except ValueError:
        print("Error: los argumentos deben ser números enteros")
    return a-b

def multiplicar(a, b):
    try:
        a=int(a)
        b=int(b)
    except ValueError:
        print("Error: los argumentos deben ser números enteros")
    return a*b
    
def dividir(a, b):
    try:
        a=int(a)
        b=int(b)
    except ValueError:
        return "Error: los argumentos deben ser números enteros"
    try: 
        return a/b
    except ZeroDivisionError:
        return"Error: el divisor no puede ser 0"

def main1():
    a, b, c, d = (10, 5, 0, "Hola")
    print( "{} + {} = {}".format(a, b, suma(a, b) ) )
    print( "{} - {} = {}".format(b, d, resta(b, d) ) )
    print( "{} * {} = {}".format(b, b,  multiplicar(b, b) ) )
    print( "{} / {} = {}".format(a, c, dividir(a, c) ) )

main1()