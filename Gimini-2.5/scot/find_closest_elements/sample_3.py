from typing import List, Tuple, Optional
# Implementation 3: Functional Style using min() with a Key
# Generates (distance, a, b) tuples and uses min() to find the minimum
# based on the first element (distance).
# ----------------------------------------------------------------------
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Functional approach: generates (distance, a, b) tuples for all pairs
    and uses the built-in min() function with a custom key.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    s = sorted(numbers)

    # Generate a list of (distance, a, b) tuples for all adjacent pairs.
    # The min function will automatically sort/compare by the first element (distance).
    # If distances are tied, it compares by the second element (a), which works
    # as a tie-breaker (choosing the pair with the smaller first number).
    pairs_with_distance = [
        (b - a, a, b)
        for a, b in zip(s, s[1:])
    ]

    # Find the minimum tuple based on the distance (first element)
    min_tuple = min(pairs_with_distance)

    # Extract and return the pair (a, b)
    return (min_tuple[1], min_tuple[2])