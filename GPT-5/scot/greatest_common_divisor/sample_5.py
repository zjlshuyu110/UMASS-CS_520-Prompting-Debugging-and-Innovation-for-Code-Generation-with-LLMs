def greatest_common_divisor(a: int, b: int) -> int:
    """Compute GCD with full edge-case handling."""
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a
