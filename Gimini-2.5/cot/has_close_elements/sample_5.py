from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Uses sorting and the zip function for iterating over adjacent pairs (O(N log N))."""
    if len(numbers) < 2:
        return False
        
    sorted_numbers = sorted(numbers)
    
    # zip(L, L[1:]) pairs up (L[0], L[1]), (L[1], L[2]), etc.
    for a, b in zip(sorted_numbers, sorted_numbers[1:]):
        # b will always be >= a since the list is sorted
        if (b - a) < threshold:
            return True
            
    return False