import numpy as np
import time
start_time = time.time()

with open('Day4.txt', 'r') as f:
    zadani = f.read()

res = [int(i) for i in zadani.split(',')]

def pocitejPalivo(zadani):
    minPalivo = 9999999999
    horizont = 0
    for x in range(max(res)):
        palivo = 0
        for i in range(len(zadani)):
            aktualniVysledek = zadani[i] - x

            if aktualniVysledek < 0:
                aktualniVysledek = aktualniVysledek * -1

            palivo = palivo + aktualniVysledek * (aktualniVysledek + 1)/2

        if palivo < minPalivo:
            horizont = x
            minPalivo = palivo

    print(minPalivo, horizont)

pocitejPalivo(res)
print(time.time() - start_time)