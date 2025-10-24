from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the two closest elements in a list of floats.
    
    Implementation 3: Enumerate approach.
    Sorts and uses enumerate to track differences, then finds minimum.
    
    Args:
        numbers: List of float values (at least 2 elements)
    
    Returns:
        Tuple of (smaller, larger) closest elements
    """
    # Sort the list
    sorted_numbers = sorted(numbers)
    
    # Calculate all consecutive differences with their indices
    differences = [
        (abs(sorted_numbers[i + 1] - sorted_numbers[i]), i)
        for i in range(len(sorted_numbers) - 1)
    ]
    
    # Find index with minimum difference
    min_diff, min_idx = min(differences, key=lambda x: x[0])
    
    # Return the pair at that index
    return (sorted_numbers[min_idx], sorted_numbers[min_idx + 1])

