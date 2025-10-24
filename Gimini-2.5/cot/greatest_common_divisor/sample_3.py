import math

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers a and b 
    using the iterative Euclidean algorithm after ensuring |a| >= |b|.
    """
    # 1. Handle negative inputs and sort for optimization
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a  # Ensure a >= b for the loop
    
    # 2. Euclidean algorithm (a is the dividend, b is the divisor)
    while b:
        a, b = b, a % b
        
    return a