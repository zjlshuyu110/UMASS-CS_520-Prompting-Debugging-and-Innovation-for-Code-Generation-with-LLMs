def get_odd_collatz(n):
    """
    Returns a sorted list of all unique odd numbers in the Collatz sequence of n.
    Uses a different loop structure.
    """
    current = n
    odd_numbers = set()

    # The starting number n is always part of the sequence.
    if current % 2 != 0:
        odd_numbers.add(current)

    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            # Current must be odd and > 1.
            current = 3 * current + 1
            # Add the *new* current if it's odd.
            # NOTE: The rule 3n+1 makes the *next* term even, so we don't check after this step.
            
        # Re-check and add only the odd numbers we land on after a transition.
        # This is slightly tricky, let's stick to the previous loop logic.
        
        # Simpler approach for this style: check *before* transition and handle n=1.
        pass # Reverting to a simpler structure that avoids double-checking for oddness.

    current = n
    odd_numbers = set()
    
    # Handle the starting number n (must be captured)
    if current % 2 != 0:
        odd_numbers.add(current)
    
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        
        # Check and collect the new number if it's odd
        if current % 2 != 0:
            odd_numbers.add(current)
            
    return sorted(list(odd_numbers))