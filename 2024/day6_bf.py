import time

def read_data(file_name):
    with open(file_name, "r") as f:
        data = [list(line.strip()) for line in f] 
    return data

def part1(data):
    start_time = time.time()  # Začátek měření času

    # Tvůj původní kód pro part1
    rows = len(data)
    cols = len(data[0])
    movements = [
        (-1, 0),  # Nahoru: snížit řádek o 1
        (0, 1),   # Doprava: zvýšit sloupec o 1
        (1, 0),   # Dolu: zvýšit řádek o 1
        (0, -1)   # Doleva: snížit sloupec o 1
    ]
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == "^":
                pos_x = x
                pos_y = y
                break
    in_bound = True
    moves = [(pos_x, pos_y)]
    while in_bound:
        for x, y in movements:
            while True:
                if pos_x < 0 or pos_x >= rows or pos_y < 0 or pos_y >= cols:
                    #print("CO SE DĚJE DOPIČE")
                    in_bound = False
                    break
                #print(f"X:Y {pos_x}:{pos_y}, char = {data[pos_x][pos_y]}")
                if (0 <= pos_x + x < rows) and (0 <= pos_y + y < cols) and data[pos_x + x][pos_y + y] == "#":
                    #print(f"Hash na {pos_x + 1}:{pos_y - 1}")
                    break
                pos_x = pos_x + x
                pos_y = pos_y + y
                if (pos_x, pos_y) not in moves:
                    moves.append((pos_x, pos_y))

    print(len(moves) - 1)
    end_time = time.time()  # Konec měření času
    print(f"Part 1 completed in {end_time - start_time:.2f} seconds")  # Výpis času

def part2(data):
    start_time = time.time()  # Začátek měření času

    rows = len(data)
    cols = len(data[0])
    movements = [
        (-1, 0),  # Nahoru: snížit řádek o 1
        (0, 1),   # Doprava: zvýšit sloupec o 1
        (1, 0),   # Dolu: zvýšit řádek o 1
        (0, -1)   # Doleva: snížit sloupec o 1
    ]
    
    # Najdi počáteční pozici '^'
    pos_x, pos_y = None, None
    for x in range(rows):
        for y in range(cols):
            if data[x][y] == "^":
                pos_x = x
                pos_y = y
                break
        if pos_x is not None:
            break

    if pos_x is None or pos_y is None:
        #print("Symbol '^' nebyl nalezen v datech.")
        return

    start_x = pos_x  # Uložení počáteční pozice
    start_y = pos_y  # Uložení počáteční pozice
    result = 0

    for i in range(rows):
        for j in range(cols):
            temp_x = start_x  # Použití temp_x místo pos_x
            temp_y = start_y  # Použití temp_y místo pos_y
            moves = []         # Resetování moves pro každou novou pozici
            in_bound = True
            hash_try_count = 0  # Počet pokusů o hash

            if data[i][j] == "^":
                continue

            if data[i][j] != '.':
                continue  # Přeskočit pozice, které už jsou překážky

            # Dočasně umístit překážku
            data[i][j] = '#'
            hash_try_count += 1
            print(f"Testing new # position at ({i}, {j}).")

            while in_bound:
                for move_index, (dx, dy) in enumerate(movements, start=1):
                    #print(f"Trying movement {move_index}: direction ({dx}, {dy})")
                    while True:
                        if temp_x < 0 or temp_x >= rows or temp_y < 0 or temp_y >= cols:
                            in_bound = False
                            break
                        else:
                            try:
                                current_char = data[temp_x][temp_y]
                            except IndexError:
                                in_bound = False
                                break

                        if (0 <= temp_x + dx < rows) and (0 <= temp_y + dy < cols) and data[temp_x + dx][temp_y + dy] == "#":
                            break
                        temp_x += dx
                        temp_y += dy
                        if (temp_x, temp_y, dx, dy) in moves:
                            result += 1
                            in_bound = False
                            break
                        else:
                            moves.append((temp_x, temp_y, dx, dy))

                    if not in_bound:
                        break

                if not in_bound:
                    break

            data[i][j] = '.'

    print(f"\nPočet detekovaných cyklů: {result}")

    end_time = time.time()  # Konec měření času
    print(f"Part 2 completed in {end_time - start_time:.2f} seconds")  # Výpis času

# Spuštění programu
data = read_data("input.txt")
part1(data)
#print("\nPart 2")
part2(data)
