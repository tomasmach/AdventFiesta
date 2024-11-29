import numpy as np
import time
import math
start_time = time.time()

with open('2019Day1.txt', 'r') as f:
    res = f.read()

res = [int(i) for i in res.split('\n')]

#print(res)

listVysledku = []

for i in range(len(res)):
    pocet = res[i]/3
    pocet = math.floor(pocet)
    pocet = pocet - 2
    listVysledku.append(pocet)

print(sum(listVysledku))
