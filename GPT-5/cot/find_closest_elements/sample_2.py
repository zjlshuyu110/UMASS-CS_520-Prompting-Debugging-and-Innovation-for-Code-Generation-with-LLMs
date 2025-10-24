from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    seen = set()
    for x in numbers:
        if x in seen:
            return (x, x)
        seen.add(x)
    s = sorted(numbers)
    best_pair = (s[0], s[1])
    best_diff = s[1] - s[0]
    for a, b in zip(s, s[1:]):
        d = b - a
        if d < best_diff:
            best_diff = d
            best_pair = (a, b)
    return best_pair
