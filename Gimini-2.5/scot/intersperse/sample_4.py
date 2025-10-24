from typing import List, Callable

# Helper for the examples below
DELIMITER = 99

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts the delimeter using recursion.
    """
    # Base case 1: Empty list
    if not numbers:
        return []
        
    # Base case 2: Single element list
    if len(numbers) == 1:
        return [numbers[0]]

    # Recursive step: Take the first element, add the delimiter, 
    # and combine with the result of calling the function on the rest of the list.
    return [numbers[0], delimeter] + intersperse(numbers[1:], delimeter)