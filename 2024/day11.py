import time
from collections import Counter

def part1(data, blinks):
    start_time = time.time()
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

    end_time = time.time()  # End measuring time
    elapsed = end_time - start_time
    print(f"Function part1 completed in {elapsed:.6f} seconds")

    return len(stones)

def part1_optimized(data, blinks):
    start_time = time.time()  # Start measuring time
    
    # Initial stones as a frequency dictionary
    stones = Counter(map(int, data.split()))

    for _ in range(blinks):
        new_stones = Counter()
        
        for stone, count in stones.items():
            if stone == 0:
                # Rule 1: Replace with a stone engraved with 1
                new_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                # Rule 2: Split into two stones, left and right halves
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_stones[left] += count
                new_stones[right] += count
            else:
                # Rule 3: Replace with stone * 2024
                new_stones[stone * 2024] += count
        
        stones = new_stones
        print(f"Blink {_ + 1}: Total stones {sum(stones.values())}, Unique stones: {len(stones)}")

    end_time = time.time()  # End measuring time
    elapsed = end_time - start_time
    print(f"Function part1_optimized completed in {elapsed:.6f} seconds")

    return sum(stones.values())

initial_data = "120 17"
blinks = 25
result = part1_optimized(initial_data, blinks)
print(result)
