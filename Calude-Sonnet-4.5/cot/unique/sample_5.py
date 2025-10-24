# Implementation 5: One-liner using sorted with set
def unique(l: list):
    """
    Compact one-liner: convert to set inline within sorted().
    Functionally identical to Implementation 1 but more condensed.
    """
    return sorted(list(set(l)))