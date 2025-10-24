from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Implementation using list comprehension and index-based min."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # Calculate all adjacent differences: [s[1]-s[0], s[2]-s[1], ...]
    # This involves O(N) space complexity for the differences list.
    differences = [sorted_numbers[i+1] - sorted_numbers[i] for i in range(n - 1)]
    
    # Find the index of the minimum difference
    # Note: min() on floats is safe for this purpose.
    min_diff_index = differences.index(min(differences))
    
    # The closest pair is at the found index and the index immediately following
    a = sorted_numbers[min_diff_index]
    b = sorted_numbers[min_diff_index + 1]
    
    return (a, b)