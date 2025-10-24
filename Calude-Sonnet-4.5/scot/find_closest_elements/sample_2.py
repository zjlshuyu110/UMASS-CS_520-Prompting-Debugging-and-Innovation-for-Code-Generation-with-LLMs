from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the two closest elements in a list of floats.
    
    Implementation 2: Brute force approach.
    Compares all possible pairs to find minimum distance.
    Less efficient O(n²) but doesn't require sorting.
    
    Args:
        numbers: List of float values (at least 2 elements)
    
    Returns:
        Tuple of (smaller, larger) closest elements
    """
    min_distance = float('inf')
    closest_pair = None
    
    # Compare all pairs
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < min_distance:
                min_distance = distance
                # Store in sorted order
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
    
    return closest_pair