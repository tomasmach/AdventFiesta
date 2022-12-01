with open('Day1.txt', 'r') as f:
    data = f.readlines()

#calories = 0
calories = []


def part1(data):
    global calories
    var = 0
    for line in data:
        if line == "\n":
            if var > calories:
                calories = var
                var = 0
            else:
                var = 0
        else:
            var += int(line.strip())

def part2(data):
    global calories
    var = 0

    for line in data:
        if line == "\n":
            calories.append(var)
            var = 0
        else:
            var += int(line.strip())
    calories.append(var)
    
    calories.sort(reverse = True)
    print(calories)
    #print(calories[:3])
    print(sum(calories[:3]))


if __name__ == '__main__':
    #part1(data)
    part2(data)
    #print(calories)