from typing import List, Callable

# Helper for the examples below
DELIMITER = 99

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts the delimeter between every two consecutive elements using 
    a standard for loop and handling the last element outside the loop.
    """
    if not numbers:
        return []

    result = []
    # Loop over all but the last element
    for number in numbers[:-1]:
        result.append(number)
        result.append(delimeter)
    
    # Append the last element, which doesn't need a trailing delimeter
    result.append(numbers[-1])
    
    return result