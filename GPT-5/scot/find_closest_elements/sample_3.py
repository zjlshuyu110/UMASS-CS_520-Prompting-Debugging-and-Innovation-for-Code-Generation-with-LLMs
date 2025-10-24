from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    s = sorted(numbers)
    # Build (diff, a, b) so min chooses smallest diff; then unpack (a, b)
    diff_a_b = ((s[i + 1] - s[i], s[i], s[i + 1]) for i in range(len(s) - 1))
    _, a, b = min(diff_a_b, key=lambda t: t[0])
    return (a, b)
