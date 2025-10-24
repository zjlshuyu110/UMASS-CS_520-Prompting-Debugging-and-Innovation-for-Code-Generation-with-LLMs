from typing import List, Callable

# Helper for the examples below
DELIMITER = 99

# Implementation 2: Iterating by Index (While Loop)
# Uses a while loop and explicit index manipulation.
# ----------------------------------------------------------------------
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts the delimeter using a while loop and checking the index
    to decide whether to append the delimeter.
    """
    result = []
    i = 0
    list_len = len(numbers)
    
    while i < list_len:
        # Append the current element
        result.append(numbers[i])
        
        # If it's not the last element, append the delimeter
        if i < list_len - 1:
            result.append(delimeter)
            
        i += 1
        
    return result