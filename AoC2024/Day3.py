import re

#part1
def sum_valid_mul_instructions(file_path):
    """
    Scans the input file for valid `mul(X,Y)` instructions,
    calculates their results, and sums them up.
    """
    total_sum = 0

    # Define the regex pattern for valid `mul(X,Y)` instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    with open(file_path, 'r') as file:
        for line in file:
            # Find all matches in the current line
            matches = re.findall(pattern, line)
            for match in matches:
                x, y = map(int, match)  # Convert the numbers to integers
                total_sum += x * y      # Calculate and add the result

    return total_sum

#part2
def sum_valid_mul_with_conditions(file_path):
    """
    Scans the input file for valid `mul(X,Y)` instructions and
    considers the enabling (`do()`) and disabling (`don't()`) instructions.
    Processes instructions continuously through each line.
    """
    total_sum = 0
    is_enabled = True  # Multiplications are enabled by default

    # Define regex patterns
    instruction_pattern = r"(do\(\)|don't\(\)|mul\(\s*\d+\s*,\s*\d+\s*\))"

    # Individual regex for extracting numbers from `mul(X,Y)`
    mul_extraction_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    with open(file_path, 'r') as file:
        for line in file:
            # Find all instructions in the order they appear
            instructions = re.findall(instruction_pattern, line)

            for instr in instructions:
                if instr == "do()":
                    is_enabled = True
                elif instr == "don't()":
                    is_enabled = False
                else:
                    # Match and extract numbers from mul(X,Y) if enabled
                    if is_enabled:
                        match = re.match(mul_extraction_pattern, instr)
                        if match:
                            x, y = map(int, match.groups())  # Extract numbers
                            total_sum += x * y              # Calculate and add to sum

    return total_sum

# Path to the input file
file_path = "input3.txt"  # Replace with your file name

# Calculate and display the sum of valid mul instructions
result = sum_valid_mul_instructions(file_path)
print(f"Part 1: The sum of all valid mul instructions is: {result}")

# Calculate and display the sum of valid mul instructions
result = sum_valid_mul_with_conditions(file_path)
print(f"Part 2: The sum of all valid mul instructions (with conditions) is: {result}")
