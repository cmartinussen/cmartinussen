from collections import deque
import os

def parse_map_and_find_positions(map_lines):
    """
    Parse the racetrack map and find start (S) and end (E) positions.

    Args:
        map_lines: List of strings representing the map.

    Returns:
        Tuple of the parsed map, start position, and end position.
    """
    racetrack = []
    start = end = None
    for y, line in enumerate(map_lines):
        row = []
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
                row.append('.')
            elif char == 'E':
                end = (x, y)
                row.append('.')
            else:
                row.append(char)
        racetrack.append(row)
    return racetrack, start, end

def find_cheats_with_exact_saving(map_lines, exact_saving):
    """
    Finds all cheats that save exactly `exact_saving` picoseconds.

    Args:
        map_lines: List of strings representing the map.
        exact_saving: Exact saving required for a cheat to be considered.

    Returns:
        The number of cheats that save exactly `exact_saving` picoseconds.
    """
    racetrack, start, end = parse_map_and_find_positions(map_lines)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    width, height = len(racetrack[0]), len(racetrack)

    def bfs(start_pos, cheat_allowed):
        """Performs BFS and returns all reachable states."""
        queue = deque([(start_pos[0], start_pos[1], 0, cheat_allowed)])  # x, y, steps, cheats_left
        visited = set()
        paths = {}

        while queue:
            x, y, steps, cheat_left = queue.popleft()

            if (x, y, cheat_left) in visited:
                continue
            visited.add((x, y, cheat_left))

            if (x, y) == end:
                paths[(x, y, cheat_left)] = min(paths.get((x, y, cheat_left), float('inf')), steps)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < width and 0 <= ny < height:
                    if racetrack[ny][nx] == '#':
                        if cheat_left > 0:
                            queue.append((nx, ny, steps + 1, cheat_left - 1))
                    else:
                        queue.append((nx, ny, steps + 1, cheat_left))

        return paths

    normal_path = bfs(start, cheat_allowed=0)
    cheat_paths = bfs(start, cheat_allowed=2)

    unique_cheats = set()

    for cheat_pos, cheat_steps in cheat_paths.items():
        for normal_pos, normal_steps in normal_path.items():
            saving = normal_steps - cheat_steps
            if saving == exact_saving:
                unique_cheats.add(cheat_pos)

    return len(unique_cheats)

def read_input_file(file_name):
    """
    Reads the racetrack map from an input file.

    Args:
        file_name: Name of the input file.

    Returns:
        List of strings representing the map.
    """
    with open(file_name, 'r') as file:
        return file.read().strip().split('\n')

# Example input
example_map = [
    "###############",
    "#...#...#.....#",
    "#.#.#.#.#.###.#",
    "#S#...#.#.#...#",
    "#######.#.#.###",
    "#######.#.#...#",
    "#######.#.###.#",
    "###..E#...#...#",
    "###.#######.###",
    "#...###...#...#",
    "#.#####.#.###.#",
    "#.#...#.#.#...#",
    "#.#.#.#.#.#.###",
    "#...#...#...###",
    "###############",
]

# Check for input file
input_file = "input200.txt"
try:
    map_lines = read_input_file(input_file)
except FileNotFoundError:
    map_lines = example_map

# Find cheats with exact saving of 64 picoseconds
exact_saving = 12
result = find_cheats_with_exact_saving(map_lines, exact_saving)
print(f"Number of cheats saving exactly {exact_saving} picoseconds: {result}")

#does not work