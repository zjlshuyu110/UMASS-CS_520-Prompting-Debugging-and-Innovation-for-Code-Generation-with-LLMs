from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers[:]
    return [x for i, x in enumerate(numbers) for x in ([x, delimeter] if i < len(numbers) - 1 else [x])]
