
from typing import List
from itertools import combinations

# --- Shared Validation Logic ---
def _validate_input(numbers: List[float]):
    """Raises ValueError if the list of numbers is empty."""
    if not numbers:
        raise ValueError("Input list 'numbers' must not be empty.")

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    A functional approach using sorting, list slicing, and zip to compare adjacent elements.
    Time Complexity: O(N log N) due to sorting.
    """
    _validate_input(numbers)
    
    # Sort the list
    sorted_numbers = sorted(numbers)
    
    # Use zip to create pairs of adjacent elements: (n[0], n[1]), (n[1], n[2]), etc.
    # We only need to check if ANY adjacent difference is less than the threshold.
    is_close = any(
        (b - a) < threshold 
        for a, b in zip(sorted_numbers[:-1], sorted_numbers[1:])
    )
    
    return is_close