import numpy as np

with open("Day3.txt") as f:
    data = list(zip(*[[int(i) for i in x.strip()] for x in f]))

def Pocitej(neco):

    l = len(neco[0]) / 2
    gamma = "".join("1" if sum(c) > l else "0" for c in neco)
    epsilon = "".join("1" if x == "0" else "0" for x in gamma)
    print(int(gamma, 2) * int(epsilon, 2))

Pocitej(data)