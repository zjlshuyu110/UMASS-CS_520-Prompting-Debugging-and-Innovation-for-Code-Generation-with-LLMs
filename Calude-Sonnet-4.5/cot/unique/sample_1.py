# Implementation 1: Classic set + sorted approach
def unique(l: list):
    """
    Convert to set to remove duplicates, then return sorted list.
    Most straightforward and Pythonic approach.
    """
    return sorted(set(l))