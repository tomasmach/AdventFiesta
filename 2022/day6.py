with open('input.txt', 'r') as f:
    data = f.read()


def part1(data):
    for i in range(0, len(data)-14):
        if len(set(data[i: i+14])) == 14:
            return i + 14


if __name__ == '__main__':
    print(part1(data))
