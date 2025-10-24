# Implementation 3: Using dict.fromkeys() to preserve uniqueness
def unique(l: list):
    """
    dict.fromkeys() removes duplicates while preserving first occurrence order.
    Then sort the keys.
    """
    return sorted(dict.fromkeys(l).keys())