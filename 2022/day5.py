""" [G]         [P]         [M]    
    [V]     [M] [W] [S]     [Q]    
    [N]     [N] [G] [H]     [T] [F]
    [J]     [W] [V] [Q] [W] [F] [P]
[C] [H]     [T] [T] [G] [B] [Z] [B]
[S] [W] [S] [L] [F] [B] [P] [C] [H]
[G] [M] [Q] [S] [Z] [T] [J] [D] [S]
[B] [T] [M] [B] [J] [C] [T] [G] [N]
 1   2   3   4   5   6   7   8   9 """


stacks =  {"1": ["B", "G", "S", "C",],
           "2": ["T", "M", "W", "H", "J", "N", "V", "G"],
           "3": ["M", "Q", "S"],
           "4": ["B", "S", "L", "T", "W", "N", "M"],
           "5": ["J", "Z", "F", "T", "V", "G", "W", "P"],
           "6": ["C", "T", "B", "G", "Q", "H", "S"],
           "7": ["T", "J", "P", "B", "W"],
           "8": ["G", "D", "C", "Z", "F", "T", "Q", "M"],
           "9": ["N", "S", "H", "B", "P", "F"]}

data = [x.strip() for x in open('input.txt').readlines()]

def part1(data):
    global stacks

    for i in data:
        move, from_stack, to_stack = i.replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
        move = int(move)
        for j in range(move):
            stacks[to_stack].append(stacks[from_stack].pop())
    
    for k in stacks.keys():
        print(stacks[k][-1])

def part2(data):
    for i in data:
        move, from_stack, to_stack = i.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
        move = int(move)

        stacks[to_stack] += stacks[from_stack][move * -1:]
        del stacks[from_stack][move * -1:]

    for k in stacks.keys():
        print(stacks[k][-1])

if __name__ == "__main__":
    #part1(data)
    part2(data)
