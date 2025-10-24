from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the two closest elements in a list of floats.
    
    Implementation 4: Functional style with zip.
    Uses zip to pair consecutive elements after sorting.
    
    Args:
        numbers: List of float values (at least 2 elements)
    
    Returns:
        Tuple of (smaller, larger) closest elements
    """
    # Sort the list
    sorted_numbers = sorted(numbers)
    
    # Zip consecutive pairs and find minimum by distance
    consecutive_pairs = zip(sorted_numbers[:-1], sorted_numbers[1:])
    
    # Find pair with minimum distance
    closest_pair = min(consecutive_pairs, key=lambda pair: abs(pair[1] - pair[0]))
    
    return closest_pair