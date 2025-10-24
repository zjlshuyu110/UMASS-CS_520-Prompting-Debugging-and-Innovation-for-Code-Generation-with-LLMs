from typing import List, Tuple
from itertools import pairwise # Requires Python 3.10+

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Implementation using itertools.pairwise (Python 3.10+)."""
    sorted_numbers = sorted(numbers)
    
    # pairwise(iterable) returns (s[0], s[1]), (s[1], s[2]), ...
    # This is equivalent to the zip approach but more concise.
    
    # Find the pair that minimizes the difference (p[1] - p[0])
    # The 'min' function with a key does the single O(N) pass.
    closest_pair = min(pairwise(sorted_numbers), key=lambda p: p[1] - p[0])
    
    return closest_pair