from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of the input list 'numbers'.
    """
    if len(numbers) < 2:
        return list(numbers)  # Return a new list, unchanged.

    result = []
    
    # Process the first element separately (no delimiter before it)
    result.append(numbers[0])
    
    # Process the remaining elements, prepending the delimiter
    for x in numbers[1:]:
        result.append(delimeter)
        result.append(x)
        
    return result