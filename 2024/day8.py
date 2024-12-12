import time
from itertools import combinations
from math import gcd

def read_data(file_name):
    """Načte data ze souboru a vrátí je jako 2D seznam."""
    with open(file_name, "r") as f:
        data = [list(line.strip()) for line in f]
    return data

def bresenham(x0, y0, x1, y1):
    """
    Implementace Bresenhamova algoritmu pro získání všech bodů na přímce
    mezi (x0, y0) a (x1, y1).
    """
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    
    if dy <= dx:
        err = dx / 2.0
        while x != x1:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
        points.append((x, y))  # Přidej poslední bod
    else:
        err = dy / 2.0
        while y != y1:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
        points.append((x, y))  # Přidej poslední bod
    return points

def part1(antenna_map):
    """Spočítá počet jedinečných poloh antinodů v mapě podle Part 1."""
    start_time = time.time()

    rows = len(antenna_map)
    cols = len(antenna_map[0])
    antinodes = set()

    # Vytvoř slovník frekvence -> seznam pozic
    freq_dict = {}
    for i in range(rows):
        for j in range(cols):
            freq = antenna_map[i][j]
            if freq != '.':
                freq_dict.setdefault(freq, []).append((i, j))

    # Pro každou frekvenci, najdi antinody podle Part 1 pravidel
    for freq, positions in freq_dict.items():
        if len(positions) < 2:
            continue
        for a, b in combinations(positions, 2):
            ax, ay = a
            bx, by = b
            # Antinoda na jedné straně
            cx, cy = 2 * bx - ax, 2 * by - ay
            if 0 <= cx < rows and 0 <= cy < cols:
                antinodes.add((cx, cy))
            # Antinoda na druhé straně
            cx, cy = 2 * ax - bx, 2 * ay - by
            if 0 <= cx < rows and 0 <= cy < cols:
                antinodes.add((cx, cy))

    end_time = time.time()
    print(f"Part 1 completed in {end_time - start_time:.2f} seconds")
    return len(antinodes)

def part2(antenna_map):
    """Spočítá počet jedinečných poloh antinodů v mapě podle Part 2."""
    start_time = time.time()

    rows = len(antenna_map)
    cols = len(antenna_map[0])
    antinodes = set()

    # Vytvoř slovník frekvence -> seznam pozic antén
    freq_dict = {}
    for i in range(rows):
        for j in range(cols):
            freq = antenna_map[i][j]
            if freq != '.':
                freq_dict.setdefault(freq, []).append((i, j))

    # Pro každou frekvenci s dvěma nebo více anténami
    for freq, positions in freq_dict.items():
        if len(positions) < 2:
            continue

        # Pro každou dvojici antén
        for (ax, ay), (bx, by) in combinations(positions, 2):
            dx = bx - ax
            dy = by - ay
            g = gcd(dx, dy)
            dx //= g
            dy //= g

            # Procházení přímky v obou směrech
            # Směr vpřed (z bodu a):
            x, y = ax, ay
            # Jdeme po směru dx, dy
            while 0 <= x < rows and 0 <= y < cols:
                antinodes.add((x, y))
                x += dx
                y += dy

            # Směr vzad (z bodu a):
            x, y = ax - dx, ay - dy
            while 0 <= x < rows and 0 <= y < cols:
                antinodes.add((x, y))
                x -= dx
                y -= dy

            # Směr vpřed (z bodu b):
            x, y = bx, by
            while 0 <= x < rows and 0 <= y < cols:
                antinodes.add((x, y))
                x += dx
                y += dy

            # Směr vzad (z bodu b):
            x, y = bx - dx, by - dy
            while 0 <= x < rows and 0 <= y < cols:
                antinodes.add((x, y))
                x -= dx
                y -= dy

    end_time = time.time()
    print(f"Part 2 completed in {end_time - start_time:.2f} seconds")
    return len(antinodes)

if __name__ == "__main__":
    # Načtení dat
    antenna_map = read_data("input.txt")

    # Výpočet Part 1
    unique_antinodes_part1 = part1(antenna_map)
    print(f"The number of unique antinode locations (Part 1) is: {unique_antinodes_part1}")

    # Výpočet Part 2
    unique_antinodes_part2 = part2(antenna_map)
    print(f"The number of unique antinode locations (Part 2) is: {unique_antinodes_part2}")
