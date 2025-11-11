from typing import List, Tuple
import math

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Selects and returns the two closest numbers from a list, 
    in order (smaller number first, larger number second).
    """
    # 1. Sort the list (O(N log N))
    sorted_numbers = sorted(numbers)
    
    # Initialize minimum difference and the closest pair
    min_diff = math.inf
    closest_pair: Tuple[float, float] = (0.0, 0.0) # Will be overwritten
    
    # 2. Iterate through adjacent pairs (O(N))
    # We only need to iterate up to the second-to-last element
    for i in range(len(sorted_numbers) - 1):
        a = sorted_numbers[i]
        b = sorted_numbers[i+1]
        
        # Since the list is sorted, b >= a, so difference is b - a
        current_diff = b - a
        
        # 3. Update if a new minimum difference is found
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = (a, b)
            
    # 4. Return the pair
    return closest_pair

