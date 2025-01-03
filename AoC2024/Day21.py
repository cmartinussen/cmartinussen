from collections import deque

def calculate_shortest_sequence(keypad, start, target):
    """
    BFS to find the shortest sequence of moves from start to target.
    """
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    queue = deque([(start, "")])  # (current_position, path_so_far)
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == target:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if (nx, ny) in keypad and keypad[(nx, ny)] != " ":
                queue.append(((nx, ny), path + move))

    return None  # Should not reach here if the target is reachable

def calculate_code_complexity(code, numeric_keypad):
    """
    Calculate the complexity for a given code.
    """
    start_position = (3, 2)  # Starting at 'A' on the numeric keypad
    total_length = 0

    for char in code:
        # Find the target position on the numeric keypad
        target_position = next(pos for pos, val in numeric_keypad.items() if val == char)

        # Calculate the shortest sequence to this target
        sequence = calculate_shortest_sequence(numeric_keypad, start_position, target_position)
        total_length += len(sequence) + 1  # +1 for the 'A' press

        # Update the start position for the next character
        start_position = target_position

    numeric_part = int("".join(filter(str.isdigit, code)))
    return total_length * numeric_part

def main():
    numeric_keypad = {
        (0, 0): '7', (0, 1): '8', (0, 2): '9',
        (1, 0): '4', (1, 1): '5', (1, 2): '6',
        (2, 0): '1', (2, 1): '2', (2, 2): '3',
        (3, 1): '0', (3, 2): 'A'
    }

    # Define the codes to be entered
    codes = ["029A", "980A", "179A", "456A", "379A"]

    # Calculate total complexity
    total_complexity = sum(calculate_code_complexity(code, numeric_keypad) for code in codes)

    print("Sum of complexities:", total_complexity)

if __name__ == "__main__":
    main()
