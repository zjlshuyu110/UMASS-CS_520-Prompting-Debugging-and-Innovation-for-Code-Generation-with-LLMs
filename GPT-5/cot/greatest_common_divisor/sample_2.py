def greatest_common_divisor(a: int, b: int) -> int:
    """Recursive Euclidean algorithm with absolute normalization."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a  # also covers a==b==0 -> 0
    return greatest_common_divisor(b, a % b)
