from typing import List, Tuple

# Implementation 5: Compact brute force with early initialization
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Compact version with different initialization strategy.
    Time: O(n²), Space: O(1)
    """
    n = len(numbers)
    best_i, best_j = 0, 1
    min_dist = abs(numbers[1] - numbers[0])
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(numbers[i] - numbers[j])
            if dist < min_dist:
                min_dist = dist
                best_i, best_j = i, j
    
    return (min(numbers[best_i], numbers[best_j]), max(numbers[best_i], numbers[best_j]))