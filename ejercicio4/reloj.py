import datetime
import os
import time

while True:
    os.system('cls')
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    time.sleep(1)