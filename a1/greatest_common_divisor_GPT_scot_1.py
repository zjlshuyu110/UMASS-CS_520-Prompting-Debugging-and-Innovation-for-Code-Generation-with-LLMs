def greatest_common_divisor(a: int, b: int) -> int:
    """Compute GCD using the iterative Euclidean algorithm."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a
