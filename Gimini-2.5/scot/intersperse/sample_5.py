from typing import List, Callable

# Helper for the examples below
DELIMITER = 99

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts the delimeter by iterating and accumulating with list extension.
    This is very similar to V1 but emphasizes the sequential extension step.
    """
    result = []
    
    # Iterate through all elements. The delimiter is only added 
    # if we know there is an element *after* the current one.
    for i, number in enumerate(numbers):
        result.append(number)
        
        # Check if the current element is NOT the last one
        if i < len(numbers) - 1:
            result.append(delimeter)
            
    return result