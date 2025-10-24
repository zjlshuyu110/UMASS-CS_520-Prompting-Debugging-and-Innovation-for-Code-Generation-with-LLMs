def get_odd_collatz(n):
    """
    Iterative implementation using a single `while` loop and conditional assignment.
    """
    if n <= 0:
        return []
        
    odd_numbers = set()
    current = n
    
    while current != 1:
        is_odd = current % 2 != 0
        if is_odd:
            odd_numbers.add(current)
            current = 3 * current + 1
        else:
            current //= 2
            
    odd_numbers.add(1) # Add the terminating 1
    
    return sorted(list(odd_numbers))