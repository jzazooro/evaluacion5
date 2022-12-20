from ejercicio1.operaciones import suma, resta, multiplicar, dividir

a, b, c, d = (10, 5, 0, "Hola")

print( "{} + {} = {}".format(a, b, suma(a, b) ) )

print( "{} - {} = {}".format(b, d, resta(b, d) ) )

print( "{} * {} = {}".format(b, b,  multiplicar(b, b) ) )

print( "{} / {} = {}".format(a, c, dividir(a, c) ) )