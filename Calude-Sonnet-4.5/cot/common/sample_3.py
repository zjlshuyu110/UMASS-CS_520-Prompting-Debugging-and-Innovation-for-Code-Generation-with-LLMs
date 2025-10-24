# Implementation 3: Using intersection() method
def common(l1: list, l2: list):
    """Return sorted list of unique elements present in both lists."""
    return sorted(set(l1).intersection(set(l2)))