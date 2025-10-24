def greatest_common_divisor(a: int, b: int) -> int:
    """
    Compute GCD using recursive Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Non-negative GCD of a and b
    """
    a, b = abs(a), abs(b)
    
    if b == 0:
        return a
    
    return greatest_common_divisor(b, a % b)