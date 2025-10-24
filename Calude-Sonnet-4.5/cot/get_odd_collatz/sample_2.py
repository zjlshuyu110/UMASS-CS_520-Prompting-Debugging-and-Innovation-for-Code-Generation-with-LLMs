def get_odd_collatz(n):
    """Collect odd numbers in a list, then deduplicate and sort."""
    odd_numbers = []
    
    while n != 1:
        if n % 2 == 1:
            odd_numbers.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    odd_numbers.append(1)
    return sorted(set(odd_numbers))