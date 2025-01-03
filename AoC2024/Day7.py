import os
from itertools import product

def parse_calibration_input(input_data):
    """
    Parses the calibration input data into test values and their associated numbers.
    """
    equations = []
    for line in input_data.strip().splitlines():
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        equations.append((test_value, numbers))
    return equations


def evaluate_expression(numbers, operators):
    """
    Evaluates the expression formed by the numbers and operators left-to-right.
    """
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
    return result


def is_valid_equation(test_value, numbers):
    """
    Checks if a test value can be obtained by inserting any combination of + and * between the numbers.
    """
    num_operators = len(numbers) - 1
    for operators in product("+*", repeat=num_operators):
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False


def calculate_total_calibration(input_data):
    """
    Calculates the total calibration result by summing test values of valid equations.
    """
    equations = parse_calibration_input(input_data)
    total_calibration = 0
    for test_value, numbers in equations:
        if is_valid_equation(test_value, numbers):
            total_calibration += test_value
    return total_calibration


# Example input
example_calibration_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def calculate_total_calibration_from_file_if_exists(file_path):
    """
    Reads calibration data from a file and calculates the total calibration result.
    Only runs if the file exists.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            input_data = file.read()
        return calculate_total_calibration(input_data)
    else:
        return None


# File path for input7.txt
file_path = "input7.txt"

# Calculate results for both the example input and input7.txt (if available)
example_result = calculate_total_calibration(example_calibration_input)
file_result = calculate_total_calibration_from_file_if_exists(file_path)

print("Part 1:" + str(example_result), str(file_result))
