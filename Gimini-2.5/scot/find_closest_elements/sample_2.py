from typing import List, Tuple, Optional
# Implementation 2: Zip/Pairwise Iteration
# Uses Python's zip feature to create consecutive pairs without manual indexing.
# ----------------------------------------------------------------------
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Finds the pair of closest elements using zip iteration over consecutive pairs.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    sorted_numbers = sorted(numbers)

    min_distance = float('inf')
    closest_pair = (0.0, 0.0) # Placeholder, will be updated in the first iteration

    # Iterate over (a, b) pairs directly
    # Note: zip(s, s[1:]) generates [(s[0], s[1]), (s[1], s[2]), ...]
    for a, b in zip(sorted_numbers, sorted_numbers[1:]):
        current_distance = b - a

        if current_distance < min_distance:
            min_distance = current_distance
            closest_pair = (a, b)
            if min_distance == 0.0:
                break # Optimization

    return closest_pair