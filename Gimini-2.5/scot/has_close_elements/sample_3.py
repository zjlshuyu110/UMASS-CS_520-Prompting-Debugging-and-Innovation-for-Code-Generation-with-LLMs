from typing import List
from itertools import combinations

# --- Shared Validation Logic ---
def _validate_input(numbers: List[float]):
    """Raises ValueError if the list of numbers is empty."""
    if not numbers:
        raise ValueError("Input list 'numbers' must not be empty.")
    
    
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks for close elements by sorting the list and only comparing adjacent numbers.
    Time Complexity: O(N log N) due to sorting.
    """
    _validate_input(numbers)
    
    # 1. Sort the list (O(N log N))
    sorted_numbers = sorted(numbers)
    
    # 2. Iterate and compare adjacent elements (O(N))
    # We stop at len - 1 because we check i and i + 1
    for i in range(len(sorted_numbers) - 1):
        # Since it is sorted, sorted_numbers[i+1] >= sorted_numbers[i]
        difference = sorted_numbers[i+1] - sorted_numbers[i]
        
        if difference < threshold:
            return True
            
    return False