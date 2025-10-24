def greatest_common_divisor(a: int, b: int) -> int:
    """
    Compute GCD using Euclidean algorithm with explicit swapping
    to ensure a >= b at each step.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Non-negative GCD of a and b
    """
    a, b = abs(a), abs(b)
    
    # Ensure a >= b
    if a < b:
        a, b = b, a
    
    while b > 0:
        remainder = a % b
        a = b
        b = remainder
    
    return a