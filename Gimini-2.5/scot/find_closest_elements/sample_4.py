from typing import List, Tuple, Optional
# Implementation 4: Early Exit/Zero Distance Priority
# Explicitly prioritizes finding a zero distance and bails out immediately.
# ----------------------------------------------------------------------
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Optimized for lists likely to contain duplicates (distance 0.0),
    prioritizing early exit logic.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    s = sorted(numbers)
    min_distance = float('inf')
    closest_pair = (s[0], s[1])

    # Pre-check for the most common minimum: distance 0.0
    for i in range(1, len(s)):
        a, b = s[i-1], s[i]
        current_distance = b - a

        if current_distance == 0.0:
            # Found the absolute minimum distance, no need to continue
            return (a, b)

        if current_distance < min_distance:
            min_distance = current_distance
            closest_pair = (a, b)

    return closest_pair