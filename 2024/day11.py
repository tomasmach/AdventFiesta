def part1(data, blinks):
    stones = list(map(int, data.split()))

    for _ in range(blinks):
        new_stones = []
        append = new_stones.append

        for stone in stones:
            if stone == 0:
                # Rule 1: Replace with a stone engraved with 1
                append(1)
            elif len(str(stone)) % 2 == 0:
                # Rule 2: Split into two stones, left and right halves
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                append(left)
                append(right)
            else:
                # Rule 3: Replace with stone * 2024
                append(stone * 2024)

        # Update stones with the new state after the blink
        stones = new_stones
        print(_)

    return len(stones)


initial_data = "125 17"
blinks = 25
result = part1(initial_data, blinks)
print(result)
