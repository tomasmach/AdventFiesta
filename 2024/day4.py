def read_data(filename):
    with open(filename, 'r') as f:
        data = [list(line.strip()) for line in f]  
    print(data)
    return data

def part1(data):
    count = 0
    rows = len(data)
    cols = len(data[0])
    word = "XMAS"
    word_len = len(word)

    directions = [
        (0, 1),   # doprava (horizontálně doprava)
        (1, 0),   # dolů (svisle dolů)
        (1, 1),   # diagonálně dolů doprava
        (1, -1),  # diagonálně dolů doleva
    ]

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:

                # Kontrolujeme slovo ve směru a jeho opačném směru (pozpátku)
                for reverse in [False, True]:
                    match = True
                    for i in range(word_len):
                        if reverse:
                            # Pokud hledám slovo pozpátku, posunu se opačným směrem
                            nx = x - i * dx
                            ny = y - i * dy
                            c = word[i]
                        else:
                            # Pokud hledám slovo dopředu, posunu se ve směru
                            nx = x + i * dx
                            ny = y + i * dy
                            c = word[i]

                        # Ověřím, že nový souřadnice jsou v mřížce
                        if 0 <= nx < rows and 0 <= ny < cols:
                            # Písmeno neodpovídá
                            if data[nx][ny] != c:
                                match = False
                                break
                        else:
                            # Jestli jsem mimo mřížku
                            match = False
                            break
                    # Jestli jsem našel slovo
                    if match:
                        count += 1

    print(count)

def part2(data):
    count = 0
    rows = len(data)
    cols = len(data[0])

    # Procházím mřížku a vynechávám krajové body
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            # Sestavím řetězec z první diagonály (z levého nahoře do pravého doleva)
            diag1_seq = data[x - 1][y - 1] + data[x][y] + data[x + 1][y + 1]
            # Sestavím řetězec z druhé diagonály (z pravého nahoře do levého doleva)
            diag2_seq = data[x - 1][y + 1] + data[x][y] + data[x + 1][y - 1]

            # Zkontroluju, jestli obě diagonály tvoří "MAS" nebo "SAM"
            if (diag1_seq == "MAS" or diag1_seq == "SAM") and \
               (diag2_seq == "MAS" or diag2_seq == "SAM"):
                count += 1

    print(count)

data = read_data("input.txt")
part1(data)
part2(data)
