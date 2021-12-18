import numpy as np

target = 2020
with open('2020Day1.txt', 'r') as f:
    data = f.read()

res = [int(i) for i in data.split()]
print(data)

# https://www.techiedelight.com/find-pair-with-given-sum-array/
def najdiPar1(data, target):
    for i in range(len(data)-1):

        for j in range(i + 1, len(data)):

            if data[i] + data[j] == target:
                nasobeni = data[i] * data[j]
                print('toto -', nasobeni)
                return

def najdiPar2(data, target):
    for i in range(len(data)-2):

        for j in range(i + 1, len(data)-1):

            for k in range(i + 2, len(data)):

                if data[i] + data[j] + data[k] == target:
                    nasobeni = data[i] * data[j] * data[k]
                    print('toto 3 cisla -', nasobeni)
                    return

#najdiPar1(res,target)
#najdiPar2(res,target)