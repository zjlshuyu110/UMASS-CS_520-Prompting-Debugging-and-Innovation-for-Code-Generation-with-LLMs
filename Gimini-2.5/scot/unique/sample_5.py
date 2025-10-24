import collections
# --- Implementation 5: Using List Comprehension over Set (Style Variation) ---
# A concise, single-line expression combining the de-duplication and sorting logic.
def unique(l: list) -> list:
    """
    Returns a new list containing sorted unique elements using a concise list comprehension
    over a set conversion, combined with the sorted() function.
    """
    # The set conversion handles uniqueness, and sorted() handles the ordering.
    return [x for x in sorted(list(set(l)))]