import os
from collections import defaultdict

def next_secret_number(secret):
    """
    Generate the next secret number in the sequence.
    """
    # Step 1: Multiply by 64, mix, and prune
    secret ^= (secret * 64)
    secret %= 16777216

    # Step 2: Divide by 32, mix, and prune
    secret ^= (secret // 32)
    secret %= 16777216

    # Step 3: Multiply by 2048, mix, and prune
    secret ^= (secret * 2048)
    secret %= 16777216

    return secret

def simulate_buyer_sequence(initial_secret, count):
    """
    Simulate the sequence of secret numbers for a buyer.
    :param initial_secret: The initial secret number of the buyer.
    :param count: Number of secret numbers to generate.
    :return: The list of secret numbers in the sequence.
    """
    secret = initial_secret
    sequence = []
    for _ in range(count):
        secret = next_secret_number(secret)
        sequence.append(secret)
    return sequence

def get_prices(sequence):
    """
    Convert a sequence of secret numbers to prices (ones digit of each secret).
    :param sequence: List of secret numbers.
    :return: List of prices.
    """
    return [num % 10 for num in sequence]

def find_best_sequence(initial_secrets, target_length=2000):
    """
    Determine the best sequence of 4 price changes to maximize bananas.
    :param initial_secrets: List of initial secrets for each buyer.
    :param target_length: Number of prices to generate for each buyer.
    :return: The best sequence and the total bananas collected.
    """
    all_changes = []

    for initial_secret in initial_secrets:
        secret_sequence = simulate_buyer_sequence(initial_secret, target_length)
        prices = get_prices(secret_sequence)

        # Calculate price changes
        changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        all_changes.append((prices, changes))

    # Use a defaultdict to precompute all sequences of length 4 for faster lookup
    change_sequences = defaultdict(list)
    for buyer_index, (prices, changes) in enumerate(all_changes):
        for idx in range(len(changes) - 3):
            seq = tuple(changes[idx:idx + 4])
            change_sequences[seq].append((buyer_index, idx + 4))

    # Try all possible 4-change sequences
    max_bananas = 0
    best_sequence = None

    for i in range(-9, 10):
        for j in range(-9, 10):
            for k in range(-9, 10):
                for l in range(-9, 10):
                    target_changes = (i, j, k, l)
                    bananas = 0

                    if target_changes in change_sequences:
                        for buyer_index, price_idx in change_sequences[target_changes]:
                            bananas += all_changes[buyer_index][0][price_idx]

                    if bananas > max_bananas:
                        max_bananas = bananas
                        best_sequence = target_changes

    return best_sequence, max_bananas

def main():
    # Check if input22.txt exists
    input_file = "input22.txt"
    if os.path.exists(input_file):
        with open(input_file, "r") as file:
            initial_secrets = list(map(int, file.readlines()))
    else:
        # Default example secrets if file is not found
        initial_secrets = [1, 2, 3, 2024]

    # Part 1: Original problem
    print("--- Part 1 ---")
    total = 0
    for initial_secret in initial_secrets:
        secret_sequence = simulate_buyer_sequence(initial_secret, 2000)
        last_secret = secret_sequence[-1]
        print(f"Buyer with initial secret {initial_secret}: 2000th secret = {last_secret}")
        total += last_secret

    print("Part 1 Sum of 2000th secrets:", total)

    # Part 2: Find the best sequence of changes
    print("--- Part 2 ---")
    best_sequence, max_bananas = find_best_sequence(initial_secrets, 2000)
    print(f"Best sequence of changes: {best_sequence}")
    print(f"Maximum bananas collected: {max_bananas}")

if __name__ == "__main__":
    main()
