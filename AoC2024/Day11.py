def compute_stone_count(stone, blinks, memo):
    """
    Recursively computes the total number of stones produced by a given stone after a certain number of blinks.
    Uses memoization to optimize repeated calculations.
    """
    if blinks == 0:
        return 1  # A single stone remains unchanged without blinks

    if (stone, blinks) in memo:
        return memo[(stone, blinks)]

    if stone == 0:
        # Rule 1: 0 becomes 1
        result = compute_stone_count(1, blinks - 1, memo)
    elif len(str(stone)) % 2 == 0:
        # Rule 2: Split into two stones
        digits = str(stone)
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        result = compute_stone_count(left, blinks - 1, memo) + compute_stone_count(right, blinks - 1, memo)
    else:
        # Rule 3: Multiply by 2024
        new_stone = stone * 2024
        result = compute_stone_count(new_stone, blinks - 1, memo)

    memo[(stone, blinks)] = result
    return result


def count_stones_after_blinks_optimized(initial_stones, blinks):
    """
    Counts the total number of stones after a specified number of blinks using optimized recursion and memoization.
    """
    memo = {}
    total_stones = sum(compute_stone_count(stone, blinks, memo) for stone in initial_stones)
    return total_stones


# Input data
input_data = [77, 515, 6779622, 6, 91370, 959685, 0, 9861]
num_blinks_75 = 75
num_blinks_25 = 25

#had to optimize the code asthe first one took forever and resulted in a memory error affer approx 44 blinks

total_stones_optimized_25_blinks = count_stones_after_blinks_optimized(input_data, num_blinks_25)
print(f"Part 1: Total stones after 25 blinks: {total_stones_optimized_25_blinks}")

# Calculate the number of stones after 75 blinks
total_stones_optimized_75_blinks = count_stones_after_blinks_optimized(input_data, num_blinks_75)
print(f"Part 2: Total stones after 75 blinks: {total_stones_optimized_75_blinks}")

