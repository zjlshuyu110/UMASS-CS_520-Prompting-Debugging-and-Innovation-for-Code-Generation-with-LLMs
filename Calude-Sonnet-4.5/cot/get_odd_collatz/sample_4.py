def get_odd_collatz(n):
    """Generate full sequence, filter odds."""
    sequence = []
    current = n
    
    while current != 1:
        sequence.append(current)
        current = current // 2 if current % 2 == 0 else 3 * current + 1
    
    sequence.append(1)
    return sorted({num for num in sequence if num % 2 == 1})