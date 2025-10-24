from typing import List, Tuple, Optional


# Implementation 1: Classic Indexed Iteration
# Uses a standard for loop with range and explicit indexing.
# ----------------------------------------------------------------------
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Finds the pair of closest elements using classic indexed iteration
    after sorting the list.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    # Step 2: Sort the list (O(N log N))
    sorted_numbers = sorted(numbers)

    # Step 3: Initialize
    min_distance = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])

    # Step 4 & 5: Iterate and Update (O(N))
    for i in range(1, len(sorted_numbers)):
        a = sorted_numbers[i - 1]
        b = sorted_numbers[i]
        current_distance = b - a # Since the list is sorted, abs() is not needed

        if current_distance < min_distance:
            min_distance = current_distance
            closest_pair = (a, b)
            # Early exit optimization for perfect matches
            if min_distance == 0.0:
                break

    # Step 6: Return
    return closest_pair