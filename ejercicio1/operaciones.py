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