from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    s = sorted(numbers)
    best_i = 0
    best_diff = s[1] - s[0]
    for i, (a, b) in enumerate(zip(s, s[1:])):
        d = b - a
        if d < best_diff:
            best_diff = d
            best_i = i
    return (s[best_i], s[best_i + 1])
