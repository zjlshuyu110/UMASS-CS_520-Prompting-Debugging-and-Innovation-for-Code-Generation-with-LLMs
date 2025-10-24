from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    n = len(numbers)
    if n <= 1:
        return numbers[:]
    result = [delimeter] * (2 * n - 1)
    result[::2] = numbers
    return result
