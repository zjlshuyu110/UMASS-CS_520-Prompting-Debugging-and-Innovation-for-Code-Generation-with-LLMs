def greatest_common_divisor(a: int, b: int) -> int:
    """Computes GCD using iterative Euclidean, ensuring a >= b initially."""
    u, v = abs(a), abs(b)

    # Handle special case GCD(x, 0) = |x|
    if u == 0: return v
    if v == 0: return u

    # Ensure u >= v for cleaner logic inside the loop (optional but common optimization)
    if u < v:
        u, v = v, u

    # The loop continues until the remainder (v) is zero.
    while v > 0:
        remainder = u % v
        u = v
        v = remainder
        
    return u