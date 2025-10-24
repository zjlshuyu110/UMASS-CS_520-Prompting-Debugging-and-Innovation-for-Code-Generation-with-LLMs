from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    s = sorted(numbers)
    # Find index i minimizing s[i+1] - s[i]
    i = min(range(len(s) - 1), key=lambda k: s[k + 1] - s[k])
    return (s[i], s[i + 1])
