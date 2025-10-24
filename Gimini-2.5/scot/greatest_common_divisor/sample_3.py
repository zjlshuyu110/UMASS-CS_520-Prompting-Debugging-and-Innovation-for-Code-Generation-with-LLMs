# --- Implementation 3: Subtraction-Based Euclidean Algorithm ---
# Slower than the modulo version, but demonstrates the core principle of the algorithm.
def greatest_common_divisor(a: int, b: int) -> int:
    """Computes GCD using the iterative subtraction method."""
    u, v = abs(a), abs(b)
    
    # Handle special case GCD(x, 0) = |x|
    if u == 0: return v
    if v == 0: return u

    # Iteratively reduce the larger number by the smaller number until they are equal.
    # GCD(u, v) = GCD(u - v, v) if u > v
    while u != v:
        if u > v:
            u = u - v
        else:
            v = v - u
    
    return u