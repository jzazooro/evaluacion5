from ejercicio2.contador import*
from ejercicio4.reloj import*

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