with open("day4.txt") as f:
    data = f.read().strip()

res = data.split("\n")

def part1(input):
    var = 0

    for i in input:
        a,b = i.split(",")
        a1,a2 = map(int,a.split("-"))
        b1,b2 = map(int,b.split("-"))
        if a1 <= b1 <= b2 <= a2 or (
            b1 <= a1 <= a2 <= b2):
            var += 1 
    return(var)   

def part2(input):
    var = 0

    for i in input:
        a,b = i.split(",")
        a1,a2 = map(int,a.split("-"))
        b1,b2 = map(int,b.split("-"))
        if a2 >= b1 and a1 <= b2 or (
            b2 >= a1 and b1 <= a2):
            var += 1
    return(var)

if __name__ == '__main__':
    print(part1(res))
    print(part2(res))
