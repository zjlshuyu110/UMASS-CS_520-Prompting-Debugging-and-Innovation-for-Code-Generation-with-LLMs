def get_odd_collatz(n):
    """
    Returns a sorted list of all unique odd numbers in the Collatz sequence of n.
    """
    if n <= 0:
        # Though constraint guarantees n > 0, robust code handles it.
        return []

    current = n
    odd_numbers = set()

    while True:
        # 1. Check and collect if odd
        if current % 2 != 0:
            odd_numbers.add(current)

        # 2. Check termination
        if current == 1:
            break

        # 3. Apply Collatz rule
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1

    # 4. Return sorted list
    return sorted(list(odd_numbers))