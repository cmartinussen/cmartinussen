def is_design_possible(towel_patterns, design):
    """
    Determines if a design can be constructed using available towel patterns.

    Args:
        towel_patterns: List of strings representing towel patterns.
        design: A string representing the desired design.

    Returns:
        True if the design is possible, False otherwise.
    """
    # Use dynamic programming to check if the design can be formed
    dp = [False] * (len(design) + 1)
    dp[0] = True  # Base case: empty design is always possible

    for i in range(1, len(design) + 1):
        for pattern in towel_patterns:
            if i >= len(pattern) and dp[i - len(pattern)] and design[i - len(pattern):i] == pattern:
                dp[i] = True
                break

    return dp[len(design)]

def count_possible_designs(towel_patterns, designs):
    """
    Counts how many designs can be constructed using the available towel patterns.

    Args:
        towel_patterns: List of strings representing towel patterns.
        designs: List of strings representing desired designs.

    Returns:
        The number of designs that can be constructed.
    """
    return sum(1 for design in designs if is_design_possible(towel_patterns, design))
def count_design_arrangements(towel_patterns, design):
    """
    Counts the number of ways a design can be constructed using available towel patterns.

    Args:
        towel_patterns: List of strings representing towel patterns.
        design: A string representing the desired design.

    Returns:
        The number of ways the design can be constructed.
    """
    # Use dynamic programming to count arrangements
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # Base case: empty design has exactly one arrangement

    for i in range(1, len(design) + 1):
        for pattern in towel_patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[len(design)]

def total_design_arrangements(towel_patterns, designs):
    """
    Calculates the total number of arrangements for all designs.

    Args:
        towel_patterns: List of strings representing towel patterns.
        designs: List of strings representing desired designs.

    Returns:
        The total number of arrangements for all designs.
    """
    return sum(count_design_arrangements(towel_patterns, design) for design in designs)

def read_input_file(file_name):
    """
    Reads towel patterns and designs from an input file.

    Args:
        file_name: Name of the input file.

    Returns:
        A tuple (towel_patterns, designs).
    """
    with open(file_name, 'r') as file:
        lines = file.read().strip().split('\n')
        separator_index = lines.index('')
        towel_patterns = lines[:separator_index][0].split(', ')
        designs = lines[separator_index + 1:]
        return towel_patterns, designs

# Example input
default_towel_patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
default_designs = [
    "brwrr",
    "bggr",
    "gbbr",
    "rrbgbr",
    "ubwu",
    "bwurrg",
    "brgr",
    "bbrgwb"
]

input_file = "input19.txt"
try:
    towel_patterns, designs = read_input_file(input_file)
except FileNotFoundError:
    towel_patterns, designs = default_towel_patterns, default_designs

# Count possible designs
result = count_possible_designs(towel_patterns, designs)
print(f"Part 1: Number of possible designs: {result}")

# Calculate total arrangements
result = total_design_arrangements(towel_patterns, designs)
print(f"Part 2: Total number of design arrangements: {result}")
