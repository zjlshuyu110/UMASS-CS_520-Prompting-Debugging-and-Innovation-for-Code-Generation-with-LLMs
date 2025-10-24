def get_odd_collatz(n):
    """
    Returns a sorted list of all unique odd numbers in the Collatz sequence of n.
    Collects into a list, then converts to set for uniqueness, and finally sorts.
    """
    current = n
    sequence = []
    
    while True:
        sequence.append(current)
        
        if current == 1:
            break
            
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
            
    # Filter for odd numbers, convert to set for uniqueness, and then sort
    odd_numbers = sorted(list({x for x in sequence if x % 2 != 0}))
    
    return odd_numbers