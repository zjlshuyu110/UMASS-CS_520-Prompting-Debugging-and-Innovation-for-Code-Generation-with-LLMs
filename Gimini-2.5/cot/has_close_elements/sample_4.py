from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Uses sorting and list comprehension to find the minimum adjacent difference (O(N log N))."""
    if len(numbers) < 2:
        return False
    
    sorted_numbers = sorted(numbers)
    
    # Calculate the differences between all adjacent pairs
    adjacent_differences = [
        sorted_numbers[i+1] - sorted_numbers[i]
        for i in range(len(sorted_numbers) - 1)
    ]
    
    # Check if the smallest difference found is less than the threshold
    return min(adjacent_differences) < threshold