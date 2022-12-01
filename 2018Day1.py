j = 0
seen = {j}
with open('2018Day1.txt', 'r') as f:
    res = f.read()

res = [int(i) for i in res.split('\n')]

while True:
    for i in res:
        j = j + i

        if j in seen:
            print(j)
            
        seen.add(f)
