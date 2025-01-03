def parse_input(rules_and_updates):
    """
    Parses the input into ordering rules and updates.
    """
    sections = rules_and_updates.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    return rules, updates


def is_update_in_order(update, rules):
    """
    Checks if the given update is in order according to the rules.
    """
    rule_map = {x: [] for x, y in rules}
    for x, y in rules:
        rule_map[x].append(y)

    index_map = {page: idx for idx, page in enumerate(update)}
    for x, ys in rule_map.items():
        if x in index_map:
            for y in ys:
                if y in index_map and index_map[x] > index_map[y]:
                    return False
    return True


def sum_middle_pages(rules, updates):
    """
    Determines the middle page number of each correctly-ordered update and sums them.
    """
    total = 0
    for update in updates:
        if is_update_in_order(update, rules):
            middle_index = len(update) // 2
            total += update[middle_index]
    return total


# Example input
example_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
def parse_file(file_path):
    """
    Reads the input file and parses it into ordering rules and updates.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return parse_input(content)


# File path for the real data
file_path = "input5.txt"

# Parse the input from the file
rules, updates = parse_file(file_path) #use real data

# Parse input and calculate the result
#rules, updates = parse_input(example_input) #use test data
result = sum_middle_pages(rules, updates)
print("Part 1: " + str(result))


from collections import defaultdict, deque

def topological_sort(nodes, edges):
    """
    Performs topological sorting using Kahn's algorithm.
    """
    in_degree = {node: 0 for node in nodes}
    graph = defaultdict(list)

    # Build graph and calculate in-degrees
    for start, end in edges:
        graph[start].append(end)
        in_degree[end] += 1

    # Start with nodes with no incoming edges
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_order) != len(nodes):
        raise ValueError("Graph has a cycle!")
    return sorted_order


def reorder_update(update, rules):
    """
    Reorders a single update using the page ordering rules.
    """
    update_set = set(update)
    filtered_rules = [(x, y) for x, y in rules if x in update_set and y in update_set]
    return topological_sort(update, filtered_rules)


def sum_middle_pages_incorrect_updates(rules, updates):
    """
    Identifies incorrectly-ordered updates, reorders them, and sums their middle pages.
    """
    total = 0
    for update in updates:
        if not is_update_in_order(update, rules):
            reordered = reorder_update(update, rules)
            middle_index = len(reordered) // 2
            total += reordered[middle_index]
    return total


# Parse input
#rules, updates = parse_input(example_input) #use test data, by removing this line we use the real data from part 1

# Calculate the sum of middle pages after reordering incorrect updates
result_incorrect_updates = sum_middle_pages_incorrect_updates(rules, updates)
print("Part 2: " + str(result_incorrect_updates))
