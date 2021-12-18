import numpy as np
import time
start_time = time.time()

with open('Day1.txt', 'r') as f:
    data = f.read()

res = [int(i) for i in data.split()]
print(res)

def porovnejVelikost1(data):
    pocet = 0
    for i in range(len(data)- 1):
        if data[i] < data[i+1]:
            pocet = pocet + 1
            #print(data[i])
            print (pocet)

def porovnejVelikost2(data):
    pocet1 = 0
    for i in range(len(data)- 3):
        cislo_1 = data[i] + data[i+1] + data[i+2]
        cislo_2 = data[i+1] + data[i+2] + data[i+3]
        if cislo_1 < cislo_2:
            pocet1 = pocet1 + 1
            #print(data[i])
            print (pocet1)

porovnejVelikost1(res)
porovnejVelikost2(res)
print(time.time() - start_time)