def execute_program(registers, program):
    """
    Executes the program on the 3-bit computer and returns the output as a comma-separated string.

    Args:
        registers: Dictionary with initial register values {"A": int, "B": int, "C": int}.
        program: List of integers representing the program.

    Returns:
        A string of comma-separated outputs from the `out` instruction.
    """
    def get_combo_value(operand):
        """Calculates the value of a combo operand."""
        if operand <= 3:
            return operand
        elif operand == 4:
            return registers["A"]
        elif operand == 5:
            return registers["B"]
        elif operand == 6:
            return registers["C"]
        else:
            raise ValueError("Invalid combo operand.")

    output = []
    ip = 0  # Instruction pointer

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else None

        if opcode == 0:  # adv
            registers["A"] //= 2 ** get_combo_value(operand)
        elif opcode == 1:  # bxl
            registers["B"] ^= operand
        elif opcode == 2:  # bst
            registers["B"] = get_combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if registers["A"] != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            registers["B"] ^= registers["C"]
        elif opcode == 5:  # out
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            registers["B"] = registers["A"] // 2 ** get_combo_value(operand)
        elif opcode == 7:  # cdv
            registers["C"] = registers["A"] // 2 ** get_combo_value(operand)
        else:
            raise ValueError(f"Invalid opcode: {opcode}")

        ip += 2

    return ",".join(map(str, output))

def find_initial_a(program, chunk_size=10**6):
    """
    Finds the lowest positive initial value for register A that causes the program
    to output a copy of itself, searching incrementally in chunks.

    Args:
        program: List of integers representing the program.
        chunk_size: Number of values to test per iteration.

    Returns:
        The lowest positive integer for register A.
    """
    start = 35100000000000#1
    while True:
        print(f"Searching A values from {start} to {start + chunk_size - 1}...")
        for initial_a in range(start, start + chunk_size):
            registers = {"A": initial_a, "B": 0, "C": 0}
            output = execute_program(registers, program)
            output_program = list(map(int, output.split(",")))
            print(output_program)

            if output_program == program:
                return initial_a

        start += chunk_size



#ran for 90.000.000 cycles and no answer...
#ran for 169.000.000

#my input (not read from the file)
#Register A: 47006051
#Register B: 0
#Register C: 0
#Program: 2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0
registers = {"A": 47006051, "B": 0, "C": 0}
program = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 3, 5, 5, 3, 0]
#program = [0, 3, 5, 4, 3, 0]

# Execute the program and print the result
result = execute_program(registers, program)
print(f"Part 1: Output: {result}")
# Find the lowest initial A
lowest_a = find_initial_a(program)
print(f"Part 2: Lowest initial A: {lowest_a}")