from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Using itertools.combinations to generate all pairs elegantly.
    Time: O(n²), Space: O(1)
    """
    from itertools import combinations
    
    min_distance = float('inf')
    closest_pair = None
    
    for num1, num2 in combinations(numbers, 2):
        distance = abs(num1 - num2)
        if distance < min_distance:
            min_distance = distance
            closest_pair = (min(num1, num2), max(num1, num2))
    
    return closest_pair