import time

def read_data(file_name):
    with open(file_name, "r") as f:
        data = [list(map(int, line.strip())) for line in f]
    return data

def part1(height_map):
    start_time = time.time()

    rows = len(height_map)
    cols = len(height_map[0])
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Pohyby: nahoru, dolů, doleva, doprava

    def dfs(x, y):
        stack = [(x, y)]
        visited = set()
        reachable_nines = set()

        while stack:
            cx, cy = stack.pop()

            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))

            if height_map[cx][cy] == 9:
                reachable_nines.add((cx, cy))

            for dx, dy in movements:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < rows and 0 <= ny < cols and height_map[nx][ny] == height_map[cx][cy] + 1:
                    stack.append((nx, ny))

        return len(reachable_nines)

    total_score = 0
    for x in range(rows):
        for y in range(cols):
            if height_map[x][y] == 0:
                total_score += dfs(x, y)

    end_time = time.time()
    print(f"Part 1 completed in {end_time - start_time:.2f} seconds")
    return total_score

def part2(height_map):

    start_time = time.time()

    rows = len(height_map)
    cols = len(height_map[0])
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def count_trails(x, y):
        def dfs_trails(cx, cy, path):
            if height_map[cx][cy] == 9:
                return 1

            total_trails = 0
            for dx, dy in movements:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and height_map[nx][ny] == height_map[cx][cy] + 1 and (nx, ny) not in path:
                    total_trails += dfs_trails(nx, ny, path | {(nx, ny)})

            return total_trails

        return dfs_trails(x, y, {(x, y)})

    total_rating = 0
    for x in range(rows):
        for y in range(cols):
            if height_map[x][y] == 0:
                total_rating += count_trails(x, y)

    end_time = time.time()
    print(f"Part 2 completed in {end_time - start_time:.2f} seconds")
    return total_rating


data = read_data("input.txt")

total_score = part1(data)
print(f"The total score of all trailheads is: {total_score}")

total_rating = part2(data)
print(f"The total rating of all trailheads is: {total_rating}")
