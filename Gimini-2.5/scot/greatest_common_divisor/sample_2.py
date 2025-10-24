# --- Implementation 2: Recursive Euclidean Algorithm (Modulo) ---
def greatest_common_divisor(a: int, b: int) -> int:
    """Computes GCD using the recursive Euclidean algorithm (modulo-based)."""
    u, v = abs(a), abs(b)
    
    # Base case: if v is 0, then u is the GCD.
    if v == 0:
        return u
    
    # Recursive step: GCD(u, v) = GCD(v, u % v)
    return greatest_common_divisor(v, u % v)