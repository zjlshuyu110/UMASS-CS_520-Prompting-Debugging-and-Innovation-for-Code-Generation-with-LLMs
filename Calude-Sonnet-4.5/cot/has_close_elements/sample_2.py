from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check all pairs using nested loops."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    
    return False