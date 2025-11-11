from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Brute force approach: compare all pairs and track the minimum distance pair.
    Time: O(n²), Space: O(1)
    """
    min_distance = float('inf')
    closest_pair = (numbers[0], numbers[1])
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < min_distance:
                min_distance = distance
                # Store in order (smaller, larger)
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
    
    return closest_pair