# Re-implementing the solution due to the reset

from math import gcd
from itertools import product

def solve_claw_machine(A, B, prize, max_presses=100):
    """
    Solve a single claw machine configuration.
    
    Parameters:
    A: (A_x, A_y) movement for button A.
    B: (B_x, B_y) movement for button B.
    prize: (prize_x, prize_y) target coordinates for the prize.
    max_presses: Maximum presses of each button to consider.
    
    Returns:
    Minimum cost to win the prize or None if it's not possible.
    """
    A_x, A_y = A
    B_x, B_y = B
    prize_x, prize_y = prize

    # Iterate over all possible presses of A and B within bounds
    min_cost = float('inf')
    found_solution = False

    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            # Check if this combination satisfies the equations
            if a * A_x + b * B_x == prize_x and a * A_y + b * B_y == prize_y:
                cost = 3 * a + 1 * b  # Calculate cost
                min_cost = min(min_cost, cost)
                found_solution = True

    return min_cost if found_solution else None


def solve_all_claw_machines(claw_machines, max_presses=100):
    """
    Solve all claw machine configurations.
    
    Parameters:
    claw_machines: List of tuples (A, B, prize) for each machine.
    max_presses: Maximum presses of each button to consider.
    
    Returns:
    Total prizes won and total cost.
    """
    total_cost = 0
    prizes_won = 0

    for A, B, prize in claw_machines:
        cost = solve_claw_machine(A, B, prize, max_presses)
        if cost is not None:
            prizes_won += 1
            total_cost += cost

    return prizes_won, total_cost


# Example claw machines
claw_machines = [
    ((94, 34), (22, 67), (8400, 5400)),
    ((26, 66), (67, 21), (12748, 12176)),
    ((17, 86), (84, 37), (7870, 6450)),
    ((69, 23), (27, 71), (18641, 10279))
]

def parse_input_file(filename):
    """
    Parses the input file to extract claw machine configurations.
    """
    claw_machines = []
    with open(filename, 'r') as file:
        data = file.read().strip().split("\n\n")
        for machine_data in data:
            lines = machine_data.strip().splitlines()
            A = tuple(map(int, lines[0].replace("Button A: X+", "").replace("Y+", "").split(",")))
            B = tuple(map(int, lines[1].replace("Button B: X+", "").replace("Y+", "").split(",")))
            p1, p2 = map(int, lines[2].replace("Prize: X=", "").replace("Y=", "").split(","))
            prize = (p1+10000000000000, p2+10000000000000)
            claw_machines.append((A, B, prize))
    return claw_machines


# Read the input file
input_file = "input13.txt"
claw_machines = parse_input_file(input_file)

# Solve for all machines
prizes_won, total_cost = solve_all_claw_machines(claw_machines)
print(prizes_won, total_cost) #total cost is the part 1!
