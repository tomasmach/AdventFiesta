def read_data(file_name):
    data = []
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        numbers = list(map(int, line.replace(":", "").strip().split()))
        data.append(numbers)

    return data

def part1(data):
    operators = ["+", "*"]  # Operátory
    fin_number = []

    # Zpracování každého řádku
    for row in data:
        target = row[0]  # První číslo je cílové
        numbers = row[1:]  # Zbytek čísel

        # Vygeneruj všechny kombinace operátorů
        num_operators = len(numbers) - 1
        num_combinations = 2 ** num_operators  # 2 operátory (2^n kombinací)
        for combination in range(num_combinations):
            ops = []
            temp = combination
            for operator_index in range(num_operators):
                ops.append(operators[temp % 2])  # Rozhodni, který operátor použít
                temp //= 2

            # Vyhodnocení výrazu zleva doprava
            result = numbers[0]
            for j in range(num_operators):
                if ops[j] == "+":
                    result += numbers[j + 1]
                elif ops[j] == "*":
                    result *= numbers[j + 1]

            # Kontrola výsledku
            if result == target:
                expression = f"{numbers[0]}"
                for j in range(num_operators):
                    expression += f" {ops[j]} {numbers[j + 1]}"
                fin_number.append(result)
                break
    
    print(f"Součet všech správných výsledků: {sum(fin_number)}")

def part2(data):
    operators = ["+", "*", "||"]  # Přidáme nový operátor
    fin_number = []

    # Zpracování každého řádku
    for row in data:
        target = row[0]  # První číslo je cílové
        numbers = row[1:]  # Zbytek čísel

        # Vygeneruj všechny kombinace operátorů
        num_operators = len(numbers) - 1
        num_combinations = 3 ** num_operators  # 3 operátory (3^n kombinací)
        for combination in range(num_combinations):
            ops = []
            temp = combination
            for operator_index in range(num_operators):
                ops.append(operators[temp % 3])  # Rozhodni, který operátor použít
                temp //= 3

            # Vyhodnocení výrazu zleva doprava
            result = numbers[0]
            for j in range(num_operators):
                if ops[j] == "+":
                    result += numbers[j + 1]
                elif ops[j] == "*":
                    result *= numbers[j + 1]
                elif ops[j] == "||":
                    result = int(f"{result}{numbers[j + 1]}")  # Zřetězení jako číslo

            # Kontrola výsledku
            if result == target:
                expression = f"{numbers[0]}"
                for j in range(num_operators):
                    expression += f" {ops[j]} {numbers[j + 1]}"
                fin_number.append(result)
                break
    
    print(f"Součet všech správných výsledků: {sum(fin_number)}")


# Načtení dat ze souboru
data = read_data("input.txt")

# Zpracování načtených dat
part1(data)
part2(data)
