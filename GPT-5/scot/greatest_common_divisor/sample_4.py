def greatest_common_divisor(a: int, b: int) -> int:
    """Compute GCD iteratively with tuple swapping."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
