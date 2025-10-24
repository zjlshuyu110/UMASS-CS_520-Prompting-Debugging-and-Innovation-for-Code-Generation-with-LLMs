from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    s = sorted(numbers)
    pairs = list(zip(s, s[1:]))  # consecutive pairs
    # Choose the pair with minimal difference
    a, b = min(pairs, key=lambda p: p[1] - p[0])
    return (a, b)
