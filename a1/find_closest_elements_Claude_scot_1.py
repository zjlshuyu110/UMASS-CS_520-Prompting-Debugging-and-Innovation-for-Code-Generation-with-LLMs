from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the two closest elements in a list of floats.
    
    Implementation 1: Classic sort and iterate approach.
    Sorts the list and compares consecutive pairs to find minimum distance.
    
    Args:
        numbers: List of float values (at least 2 elements)
    
    Returns:
        Tuple of (smaller, larger) closest elements
    """
    # Sort the list to ensure consecutive elements are closest candidates
    sorted_numbers = sorted(numbers)
    
    # Initialize with first pair
    min_distance = abs(sorted_numbers[1] - sorted_numbers[0])
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    
    # Check all consecutive pairs
    for i in range(len(sorted_numbers) - 1):
        distance = abs(sorted_numbers[i + 1] - sorted_numbers[i])
        if distance < min_distance:
            min_distance = distance
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair
