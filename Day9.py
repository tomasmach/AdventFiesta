import numpy as np
import time
start_time = time.time()

with open('Day9.txt', 'r') as f:
    zadani = f.read()

res = [int(i) for i in zadani.split('\n')]

print(res)

def hledejCisla (Pocitej):
    rady = len(Pocitej)
    sloupce = len(Pocitej[0])
    print(rady, sloupce)
    #for i in range(len(ToJsouZaseHovna)):
        

hledejCisla(res)