from typing import List, Tuple
import math

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    s = sorted(numbers)
    best_diff = math.inf
    best_pair = (s[0], s[1])  # list length >= 2 guaranteed
    for i in range(len(s) - 1):
        a, b = s[i], s[i + 1]
        d = b - a  # non-negative since s is sorted
        if d < best_diff:
            best_diff = d
            best_pair = (a, b)
    return best_pair
