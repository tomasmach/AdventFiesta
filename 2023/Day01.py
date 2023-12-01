with open('input.txt', 'r') as f:
    data = f.read()
    data = data.split()

def part1(data):
    number = 0

    for line in data:
        characters = [char for char in line]

        for i in characters:
            if i.isdigit():
                break
        for j in reversed(characters):
            if j.isdigit():
                break
        number += int(i) * 10 + int(j)

    print(number)

def part2(data):
    number = 0
    word_to_number = {
        "one": "one1one", "two": "two2two", "three": "three3three", "four": "four4four", "five": "five5five",
        "six": "six6six", "seven": "seven7seven", "eight": "eight8eight", "nine": "nine9nine"
    }

    for line in data:
        for word, digit in word_to_number.items():
            line = line.replace(word, digit)

        characters = [char for char in line]
        for i in characters:
            if i.isdigit():
                break
        for j in reversed(characters):
            if j.isdigit():
                break
        number += int(i) * 10 + int(j)

    print(number)

part1(data)
part2(data)
