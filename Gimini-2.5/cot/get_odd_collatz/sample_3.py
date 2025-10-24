def _collatz_generator(n):
    """Generates the Collatz sequence for n."""
    current = n
    yield current
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        yield current

def get_odd_collatz(n):
    """
    Returns a sorted list of all unique odd numbers in the Collatz sequence of n.
    Uses a generator for sequence creation.
    """
    # Use a set comprehension on the generator output, filtering for odd numbers
    odd_numbers = {x for x in _collatz_generator(n) if x % 2 != 0}
    
    # Return sorted list
    return sorted(list(odd_numbers))