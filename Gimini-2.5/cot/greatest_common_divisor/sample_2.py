import math
import sys

# Increase recursion limit for safety in recursive solutions, though not strictly needed here
# sys.setrecursionlimit(2000) 

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers a and b 
    using the recursive Euclidean algorithm.
    """
    # 1. Handle negative inputs
    a = abs(a)
    b = abs(b)

    # 2. Base case: gcd(a, 0) = a
    if b == 0:
        return a
    
    # 3. Recursive step: gcd(a, b) = gcd(b, a % b)
    return greatest_common_divisor(b, a % b)