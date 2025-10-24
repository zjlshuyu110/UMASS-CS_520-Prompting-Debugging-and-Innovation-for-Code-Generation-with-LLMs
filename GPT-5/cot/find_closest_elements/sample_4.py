from typing import List, Tuple
import bisect

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    sorted_list: List[float] = []
    best_pair: Tuple[float, float] | None = None
    best_diff = float("inf")

    for x in numbers:
        i = bisect.bisect_left(sorted_list, x)
        # Check left neighbor
        if i > 0:
            a = sorted_list[i - 1]
            d = x - a
            if d < best_diff:
                best_diff = d
                best_pair = (a, x)
        # Check right neighbor
        if i < len(sorted_list):
            b = sorted_list[i]
            d = b - x
            if d < best_diff:
                best_diff = d
                best_pair = (x, b)
        # Insert x
        sorted_list.insert(i, x)

    # At least two numbers exist, so best_pair must be set
    return best_pair  # type: ignore[return-value]
