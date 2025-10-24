def greatest_common_divisor(a: int, b: int) -> int:
    """
    Compute GCD using subtraction-based algorithm.
    Less efficient for large numbers but conceptually simple.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Non-negative GCD of a and b
    """
    a, b = abs(a), abs(b)
    
    # Handle zero cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Repeatedly subtract smaller from larger
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a