from collections import deque
import os

def parse_garden_map(input_map):
    """
    Parses the input garden map into a 2D list.
    """
    return [list(line) for line in input_map.strip().splitlines()]


def get_neighbors(x, y, rows, cols):
    """
    Returns the valid neighbors of a cell in the garden map.
    """
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows:
            yield nx, ny


def bfs_region(garden_map, start, visited):
    """
    Performs BFS to find all cells in a region and calculate its area and perimeter.
    """
    rows, cols = len(garden_map), len(garden_map[0])
    queue = deque([start])
    region_type = garden_map[start[1]][start[0]]
    area = 0
    perimeter = 0

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        area += 1

        # Calculate perimeter and explore neighbors
        for nx, ny in get_neighbors(x, y, rows, cols):
            if garden_map[ny][nx] == region_type and (nx, ny) not in visited:
                queue.append((nx, ny))
            elif garden_map[ny][nx] != region_type:
                perimeter += 1

        # Add to perimeter for edges of the map
        if x == 0 or x == cols - 1:
            perimeter += 1
        if y == 0 or y == rows - 1:
            perimeter += 1

    return area, perimeter


def calculate_total_fencing_cost(input_map):
    """
    Calculates the total cost of fencing all regions in the garden map.
    """
    garden_map = parse_garden_map(input_map)
    rows, cols = len(garden_map), len(garden_map[0])
    visited = set()
    total_cost = 0

    for y in range(rows):
        for x in range(cols):
            if (x, y) not in visited:
                area, perimeter = bfs_region(garden_map, (x, y), visited)
                total_cost += area * perimeter

    return total_cost


# Example input
example_map = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

file_path="input12.txt"
input_data=""
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()

example_map=input_data

# Calculate the total fencing cost for the example map
total_fencing_cost = calculate_total_fencing_cost(example_map)
print("Part 1: " + str(total_fencing_cost))
