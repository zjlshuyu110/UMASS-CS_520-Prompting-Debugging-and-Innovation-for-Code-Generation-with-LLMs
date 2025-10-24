from typing import List, Tuple, Optional
# Implementation 5: Iteration using `next` and a Generator (More advanced iteration style)
# Uses a generator to calculate distances and then finds the minimum in a single line.
# ----------------------------------------------------------------------
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Uses a single pass generator combined with min() and the zip function.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    s = sorted(numbers)

    # Generator expression to iterate over (distance, a, b) tuples
    pairs_generator = (
        (b - a, a, b)
        for a, b in zip(s, s[1:])
    )

    # The min() function consumes the generator, finding the minimum distance
    # and implicitly handling ties by choosing the first element encountered.
    min_distance, element_a, element_b = min(pairs_generator)

    return (element_a, element_b)