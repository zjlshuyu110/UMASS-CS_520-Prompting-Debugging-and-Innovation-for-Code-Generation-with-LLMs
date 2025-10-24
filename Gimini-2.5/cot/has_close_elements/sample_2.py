from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Uses sorting (O(N log N)) to check only adjacent elements."""
    if len(numbers) < 2:
        return False
    
    sorted_numbers = sorted(numbers)

    # Check differences between adjacent elements
    for i in range(len(sorted_numbers) - 1):
        if (sorted_numbers[i+1] - sorted_numbers[i]) < threshold:
            return True
            
    return False