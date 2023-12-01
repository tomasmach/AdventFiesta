import numpy as np
from collections import Counter

#with open("Day3.txt") as f:
#    zadani = list(zip(*[[int(i) for i in x.strip()] for x in f]))

with open('Day1.txt', 'r') as f:
    zadani = f.read()

print(zadani)

pocitani = [[0, 0]]

for i in range(zadani):
    for j in range(len(zadani[i])):
        if int(zadani[i][j]) == 0:
            pocitani[j][0] += 1
        else:
            pocitani[j][1] += 1

print
