from ejercicio1.operaciones import*
from ejercicio2.contador import*
from ejercicio4.reloj import*

def main1():
    a, b, c, d = (10, 5, 0, "Hola")
    print( "{} + {} = {}".format(a, b, suma(a, b) ) )
    print( "{} - {} = {}".format(b, d, resta(b, d) ) )
    print( "{} * {} = {}".format(b, b,  multiplicar(b, b) ) )
    print( "{} / {} = {}".format(a, c, dividir(a, c) ) )

def main2():
    contador('inc')
    contador('inc')
    contador('inc')
    contador('dec')
    contador('')
    contador('dec')

def main4():
    while True:
        os.system('cls')
        print(datetime.datetime.now().strftime('%H:%M:%S'))
        time.sleep(1)

def main():
    a=int(input("Elija el ejercicio a ejecutar: "))
    if a==1:
        main1()
    elif a==2:
        main2()
    elif a==3:
        main3()
    elif a==4:
        main4()
    else:
        print("Error: el ejercicio no existe")
