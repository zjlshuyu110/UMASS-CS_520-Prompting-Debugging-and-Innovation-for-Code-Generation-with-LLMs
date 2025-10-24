def greatest_common_divisor(a: int, b: int) -> int:
    """
    Compute GCD using binary GCD algorithm (Stein's algorithm).
    Efficient as it uses bitwise operations instead of division.
    
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
    
    # Count common factors of 2
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1
    
    # Remove remaining factors of 2 from a
    while (a & 1) == 0:
        a >>= 1
    
    # From here on, a is always odd
    while b != 0:
        # Remove factors of 2 from b
        while (b & 1) == 0:
            b >>= 1
        
        # Now both a and b are odd; swap if necessary so a <= b
        if a > b:
            a, b = b, a
        
        # b = b - a (both odd, so result is even)
        b = b - a
    
    # Restore common factors of 2
    return a << shift