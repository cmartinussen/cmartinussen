from collections import deque
import os

def parse_topographic_map(input_map):
    """
    Parses the input topographic map into a 2D list of integers.
    """
    return [[int(char) for char in line] for line in input_map.strip().splitlines()]


def find_trailheads(topographic_map):
    """
    Identifies all trailhead positions (height 0) in the topographic map.
    """
    trailheads = []
    for y, row in enumerate(topographic_map):
        for x, height in enumerate(row):
            if height == 0:
                trailheads.append((x, y))
    return trailheads


def dfs_trail_rating(topographic_map, start, memo):
    """
    Performs DFS to calculate the trail rating for a single trailhead.
    The rating is the number of distinct hiking trails starting from the trailhead.
    Uses memoization to optimize repeated calculations for the same position.
    """
    rows, cols = len(topographic_map), len(topographic_map[0])
    x, y = start

    # If already calculated, return the cached result
    if (x, y) in memo:
        return memo[(x, y)]

    # If the height is 9, it is the end of a trail
    if topographic_map[y][x] == 9:
        return 1

    # Explore neighbors and count trails
    total_trails = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows:
            # Only continue to neighbors with height exactly one greater
            if topographic_map[ny][nx] == topographic_map[y][x] + 1:
                total_trails += dfs_trail_rating(topographic_map, (nx, ny), memo)

    # Cache the result
    memo[(x, y)] = total_trails
    return total_trails


def calculate_total_trail_rating(input_map):
    """
    Calculates the sum of ratings of all trailheads on the topographic map.
    """
    topographic_map = parse_topographic_map(input_map)
    trailheads = find_trailheads(topographic_map)
    memo = {}  # Memoization for DFS results
    total_rating = sum(dfs_trail_rating(topographic_map, trailhead, memo) for trailhead in trailheads)
    return total_rating


def bfs_trail_score(topographic_map, start):
    """
    Performs BFS to calculate the trail score for a single trailhead.
    A trail score is the count of unique positions with height 9 reachable from the trailhead.
    """
    rows, cols = len(topographic_map), len(topographic_map[0])
    visited = set()
    queue = deque([start])
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # If we reach a height of 9, add it to reachable nines
        if topographic_map[y][x] == 9:
            reachable_nines.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows:
                # Only move to neighbors with height exactly one greater
                if topographic_map[ny][nx] == topographic_map[y][x] + 1:
                    queue.append((nx, ny))

    return len(reachable_nines)


def calculate_total_trail_score(input_map):
    """
    Calculates the sum of scores of all trailheads on the topographic map.
    """
    topographic_map = parse_topographic_map(input_map)
    trailheads = find_trailheads(topographic_map)
    total_score = sum(bfs_trail_score(topographic_map, trailhead) for trailhead in trailheads)
    return total_score


# Example input
example_map = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
file_path="input10.txt"
input_data=""
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()

example_map=input_data

# Calculate the total trail score for the example map
total_trail_score = calculate_total_trail_score(example_map)
print("Part 1: " + str(total_trail_score))

# Calculate the total trail rating for the example map
total_trail_rating = calculate_total_trail_rating(example_map)
print("Part 2: " + str(total_trail_rating))
