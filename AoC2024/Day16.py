import os
import heapq

def parse_maze(input_data):
    """
    Parses the maze input and finds the start and end positions.
    """
    lines = input_data.strip().splitlines()
    maze = [list(line) for line in lines]
    start = None
    end = None

    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)

    return maze, start, end

def move(position, direction):
    """
    Calculate the next position given the current position and direction.
    """
    x, y = position
    if direction == 'N':
        return x, y - 1
    elif direction == 'E':
        return x + 1, y
    elif direction == 'S':
        return x, y + 1
    elif direction == 'W':
        return x - 1, y

def turn(direction, rotation):
    """
    Calculate the new direction after rotating clockwise or counterclockwise.
    """
    directions = ['N', 'E', 'S', 'W']
    idx = directions.index(direction)
    if rotation == 'CW':
        return directions[(idx + 1) % 4]
    elif rotation == 'CCW':
        return directions[(idx - 1) % 4]

def find_lowest_score_and_path(maze, start, end):
    """
    Uses a priority queue to find the lowest score path from start to end.
    Returns the lowest score and all tiles that are part of the best paths.
    """
    width = len(maze[0])
    height = len(maze)
    directions = ['N', 'E', 'S', 'W']

    # Priority queue: (score, x, y, direction, path)
    queue = [(0, start[0], start[1], 'E', set())]
    visited = set()
    best_paths = set()
    lowest_score = float('inf')

    while queue:
        score, x, y, direction, path = heapq.heappop(queue)

        # If we've reached the end, record the path if it's optimal
        if (x, y) == end:
            if score < lowest_score:
                lowest_score = score
                best_paths = path | {(x, y)}
            elif score == lowest_score:
                best_paths |= path | {(x, y)}
            continue

        # Skip if already visited with this direction
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # Add current position to the path
        new_path = path | {(x, y)}

        # Move forward
        next_pos = move((x, y), direction)
        nx, ny = next_pos
        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] != '#':
            heapq.heappush(queue, (score + 1, nx, ny, direction, new_path))

        # Rotate clockwise
        new_direction = turn(direction, 'CW')
        heapq.heappush(queue, (score + 1000, x, y, new_direction, new_path))

        # Rotate counterclockwise
        new_direction = turn(direction, 'CCW')
        heapq.heappush(queue, (score + 1000, x, y, new_direction, new_path))

    return lowest_score, best_paths

def mark_best_path(maze, best_paths):
    """
    Marks the tiles that are part of the best paths on the maze.
    """
    for y, row in enumerate(maze):
        for x, _ in enumerate(row):
            if (x, y) in best_paths:
                maze[y][x] = 'O'
    return maze

def print_maze(maze):
    """
    Prints the maze.
    """
    for row in maze:
        print(''.join(row))

# Check if input16.txt exists
input_file = "input16.txt"
if os.path.exists(input_file):
    with open(input_file, "r") as file:
        maze_input = file.read()
else:
    # Example input
    maze_input = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

# Parse the maze
maze, start, end = parse_maze(maze_input)

# Find the lowest score and best paths
lowest_score, best_paths = find_lowest_score_and_path(maze, start, end)
print(f"Part 1: Lowest score: {lowest_score}")
print(f"Part 2: Tiles part of best paths: {len(best_paths)}") # does not work

# Mark and print the maze with best paths
marked_maze = mark_best_path(maze, best_paths)
#print_maze(marked_maze)
