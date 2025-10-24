def get_odd_collatz(n):
    """
    Returns a sorted list of all unique odd numbers in the Collatz sequence of n.
    Uses a recursive helper function.
    """
    odd_numbers = set()

    def collatz_recurse(current):
        if current % 2 != 0:
            odd_numbers.add(current)
        
        if current == 1:
            return
        
        if current % 2 == 0:
            collatz_recurse(current // 2)
        else:
            # 3n+1 is always even, which is fine for the next step.
            collatz_recurse(3 * current + 1)

    collatz_recurse(n)
    return sorted(list(odd_numbers))