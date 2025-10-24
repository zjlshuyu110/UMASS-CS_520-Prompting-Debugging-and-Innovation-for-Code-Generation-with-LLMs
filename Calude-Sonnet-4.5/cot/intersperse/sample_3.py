from typing import List

# Implementation 3: Using zip to pair elements with delimiters
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Zip numbers with delimiters, then flatten."""
    if len(numbers) <= 1:
        return numbers[:]
    
    delimiters = [delimeter] * (len(numbers) - 1)
    result = []
    for num, delim in zip(numbers, delimiters):
        result.extend([num, delim])
    result.append(numbers[-1])
    return result