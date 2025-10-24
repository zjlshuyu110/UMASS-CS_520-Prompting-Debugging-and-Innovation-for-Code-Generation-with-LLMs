from typing import List
from itertools import combinations

# --- Shared Validation Logic ---
def _validate_input(numbers: List[float]):
    """Raises ValueError if the list of numbers is empty."""
    if not numbers:
        raise ValueError("Input list 'numbers' must not be empty.")


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    A compact brute force check using nested list comprehension and 'any'.
    Time Complexity: O(N^2)
    """
    _validate_input(numbers)
    
    n = len(numbers)
    
    # Check if any pair satisfies the condition (i < j ensures unique pairs)
    is_close = any(
        abs(numbers[i] - numbers[j]) < threshold
        for i in range(n)
        for j in range(i + 1, n)
    )
    
    return is_close