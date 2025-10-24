import math

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers a and b 
    using the standard iterative Euclidean algorithm.
    """
    # 1. Handle negative inputs: GCD is always non-negative, gcd(a, b) = gcd(|a|, |b|)
    a = abs(a)
    b = abs(b)
    
    # 2. Euclidean algorithm
    # gcd(a, b) = gcd(b, a % b)
    while b:
        # Standard tuple unpacking swap in Python: (a, b) = (b, a % b)
        a, b = b, a % b
    
    # When b is 0, a holds the GCD. This handles (0, 0) -> 0.
    return a