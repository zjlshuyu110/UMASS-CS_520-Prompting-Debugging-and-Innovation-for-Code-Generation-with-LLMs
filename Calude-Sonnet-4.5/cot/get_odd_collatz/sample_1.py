def get_odd_collatz(n):
    """Collect odd numbers using a set, then sort."""
    odd_numbers = set()
    
    while n != 1:
        if n % 2 == 1:
            odd_numbers.add(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    
    odd_numbers.add(1)  # 1 is always the final odd number
    return sorted(odd_numbers)