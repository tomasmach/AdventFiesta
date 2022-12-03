var = []
tmp = []

with open('Day3.txt', 'r') as f:
    data = f.read()

res = data.split("\n")

def part1(res):
    global var
    global tmp
    fin = 0

    for i in res:
        tmp.clear()
        firstpart, secondpart = i[:len(i)//2], i[len(i)//2:]
        for j in range(len(firstpart)):
            for k in range(len(secondpart)):
                if firstpart[j] == secondpart[k] and firstpart[j] not in tmp:
                    var.append(firstpart[j])
                    tmp.append(firstpart[j])
    for i in var:
        if i >= 'A' and i <= 'Z':
            fin += ord(i)-38
        else:
            fin += ord(i)-96
    
    return fin

def part2(res):
    global var
    global tmp
    fin = 0

    for i in range(0, len(res), 3):
        for j in res[i]:
            for k in res[i+1]:
                for l in res[i+2]:
                    if j == k == l and j not in tmp:
                        var.append(j)
                        tmp.append(j)
        tmp.clear()
    for i in var:
        if i >= 'A' and i <= 'Z':
            fin += ord(i)-38
        else:
            fin += ord(i)-96
    
    return fin


if __name__ == '__main__':
    #print(part1(res))
    print(part2(res))