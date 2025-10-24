def greatest_common_divisor(a: int, b: int) -> int:
    """Iterative Euclidean algorithm. Returns non-negative GCD; 0 only if a==b==0."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a
