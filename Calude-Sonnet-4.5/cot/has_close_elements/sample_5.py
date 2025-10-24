from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Elegant approach using zip to pair adjacent elements."""
    sorted_numbers = sorted(numbers)
    
    for num1, num2 in zip(sorted_numbers, sorted_numbers[1:]):
        if abs(num2 - num1) < threshold:
            return True
    
    return False
