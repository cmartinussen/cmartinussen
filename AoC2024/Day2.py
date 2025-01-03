def is_report_safe(report):

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are increasing or all are decreasing
    all_increasing = all(0 < diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff < 0 for diff in differences)

    return all_increasing or all_decreasing

def count_safe_reports(file_path):
    safe_count = 0

    # Read the file and evaluate each report
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_report_safe(report):
                safe_count += 1

    return safe_count

def can_be_safe_with_dampener(report):

    for i in range(len(report)):
        # Create a new report with the current level removed
        modified_report = report[:i] + report[i+1:]
        if is_report_safe(modified_report):
            return True
    return False


def count_safe_reports_with_dampener(file_path):
    safe_count = 0

    # Read the file and evaluate each report
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_report_safe(report) or can_be_safe_with_dampener(report):
                safe_count += 1

    return safe_count


# Path to the input file
file_path = "input2.txt"

#part1
safe_reports1 = count_safe_reports(file_path)

#part2
safe_reports2 = count_safe_reports_with_dampener(file_path)

print(f"The number of safe reports in part 1 is: {safe_reports1}")
print(f"The number of safe reports in part 2 is: {safe_reports2}")