import numpy as np
import os

def parse_robot_data(input_data):
    """
    Parses the robot data from the input string.
    """
    robots = []
    for line in input_data.strip().splitlines():
        pos, vel = line.split(" v=")
        p_x, p_y = map(int, pos.replace("p=", "").split(","))
        v_x, v_y = map(int, vel.split(","))
        robots.append(((p_x, p_y), (v_x, v_y)))
    return robots


def simulate_robots(robots, width, height, seconds):
    """
    Simulates the movement of robots in a space with wrapping edges.
    """
    counts = np.zeros((height, width), dtype=int)

    for (p_x, p_y), (v_x, v_y) in robots:
        # Compute final position after given seconds, with wrapping
        final_x = (p_x + v_x * seconds) % width
        final_y = (p_y + v_y * seconds) % height
        counts[final_y, final_x] += 1

    return counts


def calculate_safety_factor(counts):
    """
    Calculates the safety factor based on the number of robots in each quadrant.
    """
    height, width = counts.shape
    mid_x, mid_y = width // 2, height // 2

    # Divide into quadrants
    q1 = counts[:mid_y, mid_x + 1:].sum()  # Top-right
    q2 = counts[:mid_y, :mid_x].sum()      # Top-left
    q3 = counts[mid_y + 1:, :mid_x].sum()  # Bottom-left
    q4 = counts[mid_y + 1:, mid_x + 1:].sum()  # Bottom-right

    return q1 * q2 * q3 * q4


# Check if input14.txt exists
input_file = "input14.txt"

if os.path.exists(input_file):
    # Read from input file
    with open(input_file, "r") as file:
        input_data = file.read()
else:
    # Use the example data
    input_data = """
    p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3
    """

# Parse and simulate
robots = parse_robot_data(input_data)
counts = simulate_robots(robots, width=101, height=103, seconds=100)
safety_factor = calculate_safety_factor(counts)
print(safety_factor)


