from collections import deque
import os

def simulate_falling_bytes_and_find_path(grid_size, byte_positions):
    """
    Simulates falling bytes and calculates the shortest path from (0,0) to (grid_size-1, grid_size-1).

    Args:
        grid_size: Size of the memory grid (int).
        byte_positions: List of tuples representing the positions of falling bytes.

    Returns:
        Minimum steps required to reach the bottom-right corner, or -1 if unreachable.
    """
    # Initialize grid
    grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]

    # Simulate falling bytes
    for x, y in byte_positions:
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = True  # Mark as corrupted

    # Breadth-First Search (BFS) to find the shortest path
    def is_valid(nx, ny):
        return 0 <= nx < grid_size and 0 <= ny < grid_size and not grid[ny][nx]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0)])  # (x, y, steps)
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, steps = queue.popleft()

        # Check if we've reached the bottom-right corner
        if (x, y) == (grid_size - 1, grid_size - 1):
            return steps

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1  # If unreachable
def simulate_falling_bytes_and_find_path_2(grid_size, byte_positions):
    """
    Simulates falling bytes and calculates the shortest path from (0,0) to (grid_size-1, grid_size-1).

    Args:
        grid_size: Size of the memory grid (int).
        byte_positions: List of tuples representing the positions of falling bytes.

    Returns:
        Minimum steps required to reach the bottom-right corner, or -1 if unreachable.
    """
    # Initialize grid
    grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]

    def is_valid(nx, ny):
        return 0 <= nx < grid_size and 0 <= ny < grid_size and not grid[ny][nx]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs():
        """Performs BFS to check if the exit is reachable."""
        queue = deque([(0, 0)])  # (x, y)
        visited = set()
        visited.add((0, 0))

        while queue:
            x, y = queue.popleft()

            if (x, y) == (grid_size - 1, grid_size - 1):
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False

    # Simulate falling bytes
    for i, (x, y) in enumerate(byte_positions):
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = True  # Mark as corrupted

        # Check if the exit is unreachable
        if not bfs():
            return f"{x},{y}"

    return "-1,-1"  # If the path is never blocked
def read_input_file(file_name):
    """Reads the byte positions from an input file."""
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return [tuple(map(int, line.strip().split(','))) for line in file.readlines()]
    return None

# Example input
example_grid_size = 71
example_byte_positions = [
    (5, 4), (4, 2), (4, 5), (3, 0), (2, 1), (6, 3), (2, 4), (1, 5), (0, 6),
    (3, 3), (2, 6), (5, 1), (1, 2), (5, 5), (2, 5), (6, 5), (1, 4), (0, 4),
    (6, 4), (1, 1), (6, 1), (1, 0), (0, 5), (1, 6), (2, 0)
]

# Read input file if available
input_file = "input18.txt"
byte_positions = read_input_file(input_file) or example_byte_positions

# Run for the input
result = simulate_falling_bytes_and_find_path(example_grid_size, byte_positions[:1024])
print(f"Part 1: Minimum steps to reach the exit: {result}")

result = simulate_falling_bytes_and_find_path_2(example_grid_size, byte_positions)
print(f"Part 2: First byte that prevent exit: {result}")
