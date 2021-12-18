import numpy as np
import time
start_time = time.time()

with open('zadani.txt', 'r') as f:
    data = f.read()

res = [str(i) for i in data.split()]
print(res)

def smer(zadek):
    dopredu = 0
    hloubka = 0
#    aim = 0
    for i in range(len(zadek)):
        print(zadek[i])
        if zadek[i] == 'forward':
            dopredu = dopredu + int(zadek[i+1])
#            hloubka = aim * int(zadek[i+1]) + hloubka
        elif zadek[i] == 'up':
            hloubka = hloubka - int(zadek[i+1])
#            aim = aim - int(zadek[i+1])
        elif zadek[i] == 'down':
            hloubka = hloubka + int(zadek[i+1])
#            aim = aim + int(zadek[i+1])
        else:
            print(dopredu, hloubka)

def smer1(zadek):
    dopredu = 0
    hloubka = 0
    aim = 0
    for i in range(len(zadek)):
        print(zadek[i])
        if zadek[i] == 'forward':
            dopredu = dopredu + int(zadek[i+1])
            hloubka = aim * int(zadek[i+1]) + hloubka
        elif zadek[i] == 'up':
#            hloubka = hloubka - int(zadek[i+1])
            aim = aim - int(zadek[i+1])
        elif zadek[i] == 'down':
#            hloubka = hloubka + int(zadek[i+1])
            aim = aim + int(zadek[i+1])
        else:
            print(dopredu, hloubka)

#smer(res)
smer1(res)
print(time.time() - start_time)