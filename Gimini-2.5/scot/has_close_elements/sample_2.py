
from typing import List
from itertools import combinations

# --- Shared Validation Logic ---
def _validate_input(numbers: List[float]):
    """Raises ValueError if the list of numbers is empty."""
    if not numbers:
        raise ValueError("Input list 'numbers' must not be empty.")
    
    # --- Implementation 2: Brute Force (itertools.combinations) - O(N^2) ---
# Cleaner implementation using Python's standard library for pair generation.
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks for close elements using itertools.combinations and the 'any' function.
    Time Complexity: O(N^2)
    """
    _validate_input(numbers)
    
    # Generate all unique pairs (a, b) from the list
    all_pairs = combinations(numbers, 2)
    
    # Use 'any' to check if any pair satisfies the closeness condition
    is_close = any(abs(a - b) < threshold for a, b in all_pairs)
    
    return is_close