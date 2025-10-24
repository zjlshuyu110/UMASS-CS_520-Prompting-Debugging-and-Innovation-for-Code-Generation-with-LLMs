from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check using itertools.combinations to generate all pairs."""
    for num1, num2 in combinations(numbers, 2):
        if abs(num1 - num2) < threshold:
            return True
    
    return False