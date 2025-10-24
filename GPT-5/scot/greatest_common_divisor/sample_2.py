def greatest_common_divisor(a: int, b: int) -> int:
    """Compute GCD using recursion."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
