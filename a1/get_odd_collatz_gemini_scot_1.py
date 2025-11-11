def get_odd_collatz(n):
    """
    Generates the Collatz sequence for n and returns the sorted list of 
    unique odd numbers in that sequence, including 1.
    """
    if n <= 0:
        return [] # Handle non-positive input gracefully
        
    odd_numbers = set()
    current = n
    
    while current != 1:
        if current % 2 != 0:
            odd_numbers.add(current)
            # Apply 3n + 1 rule for the next step
            current = 3 * current + 1
        else:
            # Apply n/2 rule
            current //= 2
            
    odd_numbers.add(1) # Add the terminating 1
    
    return sorted(list(odd_numbers))