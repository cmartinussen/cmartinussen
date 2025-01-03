def count_word_in_grid(grid, word):
    """
    Counts all occurrences of the given word in the grid in all possible directions.
    """
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    total_count = 0

    # Define all possible directions (dx, dy)
    directions = [
        (0, 1),   # Horizontal right
        (1, 0),   # Vertical down
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (0, -1),  # Horizontal left
        (-1, 0),  # Vertical up
        (-1, -1), # Diagonal up-left
        (-1, 1)   # Diagonal up-right
    ]

    def is_valid_position(x, y):
        """Checks if a position is valid in the grid."""
        return 0 <= x < rows and 0 <= y < cols

    # Check for the word in all directions
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                # Check if the word can fit in the current direction
                if all(
                    is_valid_position(x + dx * i, y + dy * i) and 
                    grid[x + dx * i][y + dy * i] == word[i]
                    for i in range(word_len)
                ):
                    total_count += 1

    return total_count


# Read the grid from the input file
def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


# Path to the input file
file_path = "input4.txt"  # Replace with your file name

# Define the word to search for
word_to_find = "XMAS"

# Read the grid and count occurrences
grid = read_grid(file_path)
result = count_word_in_grid(grid, word_to_find)
print(f"Part 1: The word '{word_to_find}' appears {result} times in the grid.")


#part 2 (does not work with real data, only test data)
def count_x_mas_by_centers(grid):
    """
    Counts all occurrences of the X-MAS pattern in the grid, including diagonal patterns.
    Starts by locating all 'A' positions and evaluates from there.
    """
    rows, cols = len(grid), len(grid[0])
    total_count = 0

    def is_valid(x, y):
        """Checks if a position is within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def matches_pattern(start_x, start_y, pattern, dx, dy):
        """
        Validates if a given pattern exists starting from (start_x, start_y)
        in the direction (dx, dy).
        """
        for i in range(len(pattern)):
            x, y = start_x + i * dx, start_y + i * dy
            if not is_valid(x, y) or grid[x][y] != pattern[i]:
                return False
        return True

    # Find all centers (positions of 'A')
    centers = [(x, y) for x in range(rows) for y in range(cols) if grid[x][y] == 'A']

    # Evaluate each center
    for x, y in centers:
        # Check horizontal arms
        left_horizontal = matches_pattern(x - 1, y - 1, "MAS", 1, 0) or \
                          matches_pattern(x - 1, y - 1, "SAM", 1, 0)
        right_horizontal = matches_pattern(x - 1, y + 1, "MAS", 1, 0) or \
                           matches_pattern(x - 1, y + 1, "SAM", 1, 0)

        # Check diagonal arms
        left_diagonal = matches_pattern(x - 1, y - 1, "MAS", 1, 1) or \
                        matches_pattern(x - 1, y - 1, "SAM", 1, 1)
        right_diagonal = matches_pattern(x - 1, y + 1, "MAS", 1, -1) or \
                         matches_pattern(x - 1, y + 1, "SAM", 1, -1)

        # If any horizontal or diagonal arms match, count the pattern
        if (left_horizontal and right_horizontal) or (left_diagonal and right_diagonal):
            total_count += 1

    return total_count


# Test input
example_grid_with_centers = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    ".........."
]

# Count X-MAS occurrences in the example input starting from centers
result_with_centers = count_x_mas_by_centers(example_grid_with_centers)
print(result_with_centers)#example data

# Count X-MAS occurrences in the example input including diagonals
result_with_diagonals = count_x_mas_by_centers(grid)
print(f"Part 2: Number of X-MAS patterns: {result_with_diagonals}")

