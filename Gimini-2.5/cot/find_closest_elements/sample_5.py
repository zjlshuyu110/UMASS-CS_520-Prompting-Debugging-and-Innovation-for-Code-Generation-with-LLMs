from typing import List, Tuple
import math

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Implementation using a brute-force O(N^2) comparison of all pairs."""
    n = len(numbers)
    min_diff = math.inf
    closest_pair: Tuple[float, float] = (0.0, 0.0) 
    
    # Iterate through all unique pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            a = numbers[i]
            b = numbers[j]
            
            # Use abs() because the list is not sorted
            current_diff = abs(a - b)
            
            # If the current difference is strictly smaller, update
            if current_diff < min_diff:
                min_diff = current_diff
                # Store the pair in (smaller, larger) order
                closest_pair = (min(a, b), max(a, b))
                
            # Handle the case where the difference is equal to the minimum
            # This is important for duplicates in the unsorted list (diff = 0)
            elif current_diff == min_diff:
                # If the difference is zero (duplicates), we must return (x, x)
                if current_diff == 0:
                    return (a, a)
                    
    return closest_pair