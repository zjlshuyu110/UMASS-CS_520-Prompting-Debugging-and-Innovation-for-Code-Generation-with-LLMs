from typing import List
import itertools

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers[:]
    # Build pairs like [(1, 4), (2, 4), (3,)]
    it = itertools.chain.from_iterable(
        (n, delimeter) for n in numbers[:-1]
    )
    return list(itertools.chain(it, [numbers[-1]]))
