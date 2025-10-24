import math

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers a and b 
    using a concise iterative Euclidean algorithm implementation.
    """
    # Use temporary variables for mutable state
    x, y = abs(a), abs(b)
    
    # Euclidean algorithm: while the remainder y is non-zero
    while y:
        x, y = y, x % y
        
    # x holds the final GCD
    return x