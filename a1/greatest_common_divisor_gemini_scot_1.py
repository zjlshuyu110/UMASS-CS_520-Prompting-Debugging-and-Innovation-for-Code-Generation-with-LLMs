# --- Implementation 1: Iterative Euclidean Algorithm (Modulo) ---
# This is the most efficient and standard approach for calculating GCD.
def greatest_common_divisor(a: int, b: int) -> int:
    """Computes GCD using the standard iterative Euclidean algorithm (modulo-based)."""
    # 1. Take absolute values, as GCD is conventionally non-negative.
    u, v = abs(a), abs(b)

    # 2. Handle special case GCD(x, 0) = |x|.
    if u == 0:
        return v
    if v == 0:
        return u
    
    # 3. Iteratively apply the Euclidean division lemma.
    # GCD(u, v) = GCD(v, u % v)
    while v:
        u, v = v, u % v
    
    return u