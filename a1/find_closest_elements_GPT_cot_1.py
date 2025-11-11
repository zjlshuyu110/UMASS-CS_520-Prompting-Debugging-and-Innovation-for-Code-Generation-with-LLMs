from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    s = sorted(numbers)
    best = (s[0], s[1])
    best_diff = s[1] - s[0]
    for i in range(1, len(s) - 1):
        a, b = s[i], s[i + 1]
        d = b - a
        if d < best_diff:
            best_diff = d
            best = (a, b)
    return best
