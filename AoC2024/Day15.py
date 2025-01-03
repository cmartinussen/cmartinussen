import os

def parse_warehouse(input_data):
    """
    Parses the warehouse map and returns the robot position, box positions, and walls.
    """
    lines = input_data.strip().splitlines()
    warehouse = [list(line) for line in lines]
    robot_pos = None
    boxes = set()
    walls = set()

    for y, row in enumerate(warehouse):
        for x, char in enumerate(row):
            if char == '@':
                robot_pos = (x, y)
            elif char == 'O':
                boxes.add((x, y))
            elif char == '#':
                walls.add((x, y))

    return robot_pos, boxes, walls, len(lines), len(lines[0])

def parse_moves(input_moves):
    """
    Parses the robot moves, ignoring any whitespace or newlines.
    """
    return list(input_moves.strip().replace('\n', ''))

def move_robot(robot_pos, direction):
    """
    Calculates the new position of the robot based on the direction.
    """
    x, y = robot_pos
    if direction == '^':
        return x, y - 1
    elif direction == 'v':
        return x, y + 1
    elif direction == '<':
        return x - 1, y
    elif direction == '>':
        return x + 1, y
    return x, y

def simulate_warehouse(robot_pos, boxes, walls, moves, height, width):
    """
    Simulates the robot and box movements in the warehouse.
    """
    for move in moves:
        next_pos = move_robot(robot_pos, move)

        if next_pos in walls:
            continue  # Robot cannot move into walls

        if next_pos in boxes:
            # Attempt to push the box
            next_box_pos = move_robot(next_pos, move)
            if next_box_pos not in walls and next_box_pos not in boxes:
                # Move box and robot
                boxes.remove(next_pos)
                boxes.add(next_box_pos)
                robot_pos = next_pos
            else:
                continue  # Box cannot be pushed, robot stays in place
        else:
            # Move robot
            robot_pos = next_pos

    return robot_pos, boxes

def calculate_gps_sum(boxes, height, width):
    """
    Calculates the sum of the GPS coordinates of the boxes.
    """
    gps_sum = 0
    for x, y in boxes:
        gps_sum += 100 * y + x
    return gps_sum

# Check if input15.txt exists
input_file = "inputf15.txt"
if os.path.exists(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    warehouse_map, robot_moves = data.split("\n\n")
else:
    # Example Input
    warehouse_map = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
"""
    robot_moves = """
<^^>>>vv<v>>v<<
"""

# Parse inputs
robot_pos, boxes, walls, height, width = parse_warehouse(warehouse_map.strip())
moves = parse_moves(robot_moves)

# Simulate the warehouse
final_robot_pos, final_boxes = simulate_warehouse(robot_pos, boxes, walls, moves, height, width)

# Calculate GPS sum
gps_sum = calculate_gps_sum(final_boxes, height, width)
print("Final Warehouse State:")
for y in range(height):
    row = ""
    for x in range(width):
        if (x, y) in walls:
            row += "#"
        elif (x, y) in boxes:
            row += "O"
        elif (x, y) == final_robot_pos:
            row += "@"
        else:
            row += "."
    print(row)

print(f"Sum of GPS coordinates: {gps_sum}")
