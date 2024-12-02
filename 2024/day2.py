def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read().split("\n")
    return data

def part1(data):
    answer = 0
    for line in data:
        levels = [int(x) for x in line.split()]
        increasing = None
        for i in range(len(levels) - 1):
            diff = levels[i + 1] - levels[i]
            if diff > 0:
                if increasing is None:
                    increasing = True
                elif not increasing:
                    break
            elif diff < 0:
                if increasing is None:
                    increasing = False
                elif increasing:
                    break
            else:
                break
            if abs(diff) > 3:
                break
        else:
            answer += 1
    return answer

def part2(data):

    def is_safe(line):
        increasing = None
        for i in range(len(line) - 1):
            diff = line[i + 1] - line[i]
            if diff > 0:
                if increasing is None:
                    increasing = True
                elif not increasing:
                    return False
            elif diff < 0:
                if increasing is None:
                    increasing = False
                elif increasing:
                    return False
            else:
                return False
            if abs(diff) > 3:
                return False
        return True

    answer = 0
    for line in data:
        levels = [int(x) for x in line.split()]
        
        if is_safe(levels):
            answer += 1
        else:

            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i + 1:]
                if is_safe(new_levels):
                    answer += 1
                    break

    return answer


data = read_data("input.txt")
print(part1(data))
print(part2(data))
