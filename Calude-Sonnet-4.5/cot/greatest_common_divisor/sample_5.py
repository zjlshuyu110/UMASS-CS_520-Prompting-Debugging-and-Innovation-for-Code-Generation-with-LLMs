def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor with explicit zero handling."""
    a, b = abs(a), abs(b)
    
    # Handle zero cases explicitly
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Standard Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a