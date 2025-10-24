from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Uses a list comprehension and generator for conditional prepending."""
    if not numbers:
        return []
        
    # Create a list of lists/tuples where each element is [delimiter, number] 
    # except for the first, which is just [number].
    # Then flatten this structure.
    return [
        item 
        for i, num in enumerate(numbers) 
        for item in ([delimeter, num] if i > 0 else [num])
    ]