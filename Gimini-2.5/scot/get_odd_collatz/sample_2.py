def get_odd_collatz(n):
    """
    Recursive implementation with a helper function to build the sequence.
    Returns the sorted list of unique odd numbers.
    """
    if n <= 0:
        return []

    def collatz_recursive(current, odd_numbers):
        if current == 1:
            odd_numbers.add(1)
            return
        
        if current % 2 != 0:
            odd_numbers.add(current)
            collatz_recursive(3 * current + 1, odd_numbers)
        else:
            collatz_recursive(current // 2, odd_numbers)
            
    result_set = set()
    collatz_recursive(n, result_set)
    return sorted(list(result_set))