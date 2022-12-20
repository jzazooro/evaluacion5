from io import open

def existe(fichero):
    try: 
        f = open(fichero, 'r')
        contenido = f.read()
        f.close()
        if len(contenido) == 0:
            return False
        else:
            return True
    except FileNotFoundError:
        return False

def contador(*arg):
    if existe('ejercicio2/contador.py/contador.txt') == False:
        fichero = open('ejercicio2/contador.txt', 'a+')
        fichero.write('0')
        fichero.seek(0)
        contenido = fichero.read()
    else:
        fichero = open('ejercicio2//contador.txt', 'r')
        contenido = fichero.read()
        fichero.close()
        try:
            contenido=int(contenido)
            if len(arg) != 0:
                fichero = open('ejercicio2/contador.txt', 'w')
                if 'inc' in arg:
                    contenido = int(contenido) + 1
                elif 'dec' in arg:
                    contenido = int(contenido) - 1
                fichero.write(str(contenido))
        except ValueError:
            return 'Error en el fichero'
    fichero.close()
    return contenido