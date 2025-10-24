# Implementation 4: Filter with lambda and set membership
def common(l1: list, l2: list):
    """Return sorted list of unique elements present in both lists."""
    set2 = set(l2)
    return sorted(set(filter(lambda x: x in set2, l1)))