from typing import List
from itertools import combinations

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check with explicit early exit optimization."""
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Single element cannot have close pairs
    if len(numbers) == 1:
        return False
    
    # Check all distinct pairs
    for idx, num1 in enumerate(numbers):
        for num2 in numbers[idx + 1:]:
            distance = abs(num1 - num2)
            if distance < threshold:
                return True  # Early exit on first match
    
    return False