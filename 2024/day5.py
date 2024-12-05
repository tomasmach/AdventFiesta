def read_data(rules_file, updates_file):
    with open(rules_file, 'r') as f:
        rules = [tuple(map(int, line.split('|'))) for line in f.read().strip().split('\n')]

    with open(updates_file, 'r') as f:
        updates = [list(map(int, line.split(','))) for line in f.read().strip().split('\n')]

    return rules, updates


def part1(rules, updates):

    def is_valid(update):
        for x, y in rules:
            if x in update and y in update and update.index(x) > update.index(y):
                return False
        return True

    valid_middle_values = []
    for update in updates:
        if is_valid(update):
            valid_middle_values.append(update[len(update) // 2])

    return sum(valid_middle_values)


def part2(rules, updates):

    def is_valid(update):
        for x, y in rules:
            if x in update and y in update and update.index(x) > update.index(y):
                return False
        return True

    def reorder(update):
        graph = {}
        in_degree = {}

        for x, y in rules:
            if x in update and y in update:
                if x not in graph:
                    graph[x] = []
                if y not in in_degree:
                    in_degree[y] = 0
                if x not in in_degree:
                    in_degree[x] = 0
                graph[x].append(y)
                in_degree[y] += 1

        queue = [node for node in update if in_degree.get(node, 0) == 0]

        sorted_update = []
        while queue:
            current = queue.pop(0)
            sorted_update.append(current)
            for neighbor in graph.get(current, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_update

    fixed_middle_values = []
    for update in updates:
        if not is_valid(update):
            fixed_update = reorder(update)
            fixed_middle_values.append(fixed_update[len(fixed_update) // 2])

    return sum(fixed_middle_values)

rules, updates = read_data('input.txt', 'seznam.txt')

print(part1(rules, updates))
print(part2(rules, updates))
