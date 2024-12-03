import re

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def part1():
    pattern = r'mul\((\d+),(\d+)\)'
    result = 0
    for i in data.split("\n"):
        matches = re.findall(pattern, i)
        for match in matches:
            num1, num2 = match
            result += int(num1) * int(num2)

    print(result)

def part2():
    pattern = r'mul\((\d+),(\d+)\)'
    result = 0
    for subl in data.split("do()"):
        sublines2 = subl.split("don't()")
        for match in re.findall(pattern, sublines2[0]):
            num1, num2 = match
            result += int(num1) * int(num2)

    print(result)

data = read_data("input.txt")
part1()
part2()