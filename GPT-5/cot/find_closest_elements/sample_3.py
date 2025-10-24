from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    s = sorted(numbers)
    pairs = list(zip(s, s[1:]))
    # Distance between adjacent sorted elements is just b - a
    return min(pairs, key=lambda p: p[1] - p[0])
