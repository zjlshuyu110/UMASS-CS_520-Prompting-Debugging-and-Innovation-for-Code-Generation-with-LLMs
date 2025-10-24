from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Generate all pairs and use min() with a key function.
    Time: O(n²), Space: O(n²) for storing all pairs
    """
    from itertools import combinations
    
    # Generate all pairs in sorted order
    all_pairs = [(min(a, b), max(a, b)) for a, b in combinations(numbers, 2)]
    
    # Find the pair with minimum distance
    closest_pair = min(all_pairs, key=lambda pair: pair[1] - pair[0])
    
    return closest_pair