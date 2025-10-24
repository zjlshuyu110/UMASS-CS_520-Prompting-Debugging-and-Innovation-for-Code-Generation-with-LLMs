def get_odd_collatz(n):
    """
    Uses an inner generator function to produce the Collatz sequence, 
    then filters for odd unique numbers.
    """
    if n <= 0:
        return []

    def collatz_sequence_generator(start_n):
        current = start_n
        yield current
        while current != 1:
            if current % 2 == 0:
                current //= 2
            else:
                current = 3 * current + 1
            yield current

    # Collect unique odd numbers from the generated sequence
    # The set handles uniqueness, and the filtering handles odd numbers.
    odd_numbers = {x for x in collatz_sequence_generator(n) if x % 2 != 0}
    
    return sorted(list(odd_numbers))