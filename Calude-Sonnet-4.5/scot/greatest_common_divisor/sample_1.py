def greatest_common_divisor(a: int, b: int) -> int:
    """
    Compute GCD using iterative Euclidean algorithm.
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Non-negative GCD of a and b
    """
    a, b = abs(a), abs(b)
    
    while b != 0:
        a, b = b, a % b
    
    return a