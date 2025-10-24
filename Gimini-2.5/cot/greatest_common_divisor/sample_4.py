import math

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers a and b 
    using the subtractive Euclidean algorithm.
    """
    # 1. Handle negative inputs
    a = abs(a)
    b = abs(b)

    # 2. Handle base cases (0, 0) -> 0, (a, 0) -> a, (0, b) -> b
    if a == 0:
        return b
    if b == 0:
        return a
        
    # 3. Subtractive algorithm: keep subtracting the smaller from the larger
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    # When a == b, this value is the GCD
    return a