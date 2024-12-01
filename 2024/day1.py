def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().split()
    data = [int(x) for x in data]
    return data

def part1(data):
    right = []
    left = []
    fin_number = 0

    for i in range(0, len(data), 2):
        left.append(data[i])
        right.append(data[i+1])

    left.sort()
    right.sort()

    for i in range(len(left)):
        fin_number += abs(left[i] - right[i])

    return(fin_number)


def part2(data):
    right = []
    left = []
    fin_number = 0

    for i in range(0, len(data), 2):
        left.append(data[i])
        right.append(data[i+1])

    for i in range(len(left)):
        prave_cislo = right.count(left[i])
        fin_number += left[i] * prave_cislo

    return(fin_number)

data = read_data("test_input.txt")
print(part1(data))
print(part2(data))
