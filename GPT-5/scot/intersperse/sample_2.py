from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers[:]
    result = [x for pair in zip(numbers, [delimeter] * len(numbers)) for x in pair][:-1]
    return result
