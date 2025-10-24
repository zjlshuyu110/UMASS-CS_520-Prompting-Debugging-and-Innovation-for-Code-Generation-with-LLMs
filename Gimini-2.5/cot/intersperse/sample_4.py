from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Models the problem as a list 'join' operation."""
    
    if len(numbers) < 2:
        return list(numbers)
        
    # Create a list where the delimiter is inserted between every element.
    # e.g., [1, 2, 3] -> [1, 4, 2, 4, 3]
    
    # Start with the first element
    result = [numbers[0]]
    
    # Extend the list with [delimiter, next_element] repeatedly
    for num in numbers[1:]:
        result.extend([delimeter, num])
        
    return result