import datetime
import os
import time


def main4():
    while True:
        os.system('cls')
        print(datetime.datetime.now().strftime('%H:%M:%S'))
        time.sleep(1)

main4()