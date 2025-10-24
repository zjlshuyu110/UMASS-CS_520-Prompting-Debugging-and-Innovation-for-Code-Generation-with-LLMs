from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Implementation using zip for adjacent iteration."""
    sorted_numbers = sorted(numbers)
    
    # Use zip to create pairs: (s[0], s[1]), (s[1], s[2]), ...
    # This is a concise way to iterate over adjacent elements.
    adjacent_pairs = zip(sorted_numbers, sorted_numbers[1:])
    
    # Use the 'min' function with a key to find the pair with the smallest difference
    # key=lambda p: p[1] - p[0] computes the difference for each pair (smaller, larger)
    closest_pair = min(adjacent_pairs, key=lambda p: p[1] - p[0])
    
    return closest_pair