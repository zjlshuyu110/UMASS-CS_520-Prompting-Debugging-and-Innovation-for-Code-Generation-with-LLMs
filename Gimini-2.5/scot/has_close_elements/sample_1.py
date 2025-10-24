from typing import List
from itertools import combinations

# --- Shared Validation Logic ---
def _validate_input(numbers: List[float]):
    """Raises ValueError if the list of numbers is empty."""
    if not numbers:
        raise ValueError("Input list 'numbers' must not be empty.")

# --- Implementation 1: Brute Force (Nested Loops) - O(N^2) ---
# Simple and direct implementation using nested indices.
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks for close elements using nested loops to compare every unique pair.
    Time Complexity: O(N^2)
    """
    _validate_input(numbers)
    n = len(numbers)
    
    for i in range(n):
        # Start inner loop from i + 1 to avoid comparing an element with itself 
        # and to avoid checking the same pair twice.
        for j in range(i + 1, n):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False