from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find the two closest elements in a list of floats.
    
    Implementation 5: One-pass with running minimum.
    Sorts once, then tracks minimum in a single pass with clear variable names.
    
    Args:
        numbers: List of float values (at least 2 elements)
    
    Returns:
        Tuple of (smaller, larger) closest elements
    """
    # Sort the list to ensure adjacent elements are candidates
    sorted_numbers = sorted(numbers)
    
    # Initialize tracking variables
    best_distance = float('inf')
    best_left = None
    best_right = None
    
    # Single pass through consecutive pairs
    for i in range(len(sorted_numbers) - 1):
        left = sorted_numbers[i]
        right = sorted_numbers[i + 1]
        current_distance = right - left  # No abs() needed since sorted
        
        if current_distance < best_distance:
            best_distance = current_distance
            best_left = left
            best_right = right
    
    return (best_left, best_right)