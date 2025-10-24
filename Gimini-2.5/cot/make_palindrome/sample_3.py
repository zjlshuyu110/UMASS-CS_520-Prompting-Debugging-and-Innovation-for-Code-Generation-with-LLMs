def _is_palindrome_ptr(s: str) -> bool:
    """Helper using two pointers for palindrome check."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def make_palindrome(string: str) -> str:
    """
    Finds the shortest palindrome that begins with the supplied string
    using a two-pointer helper for the palindrome check.
    """
    n = len(string)
    if n == 0:
        return ""

    # Find the index 'i' where the suffix string[i:] is the longest palindrome.
    # We iterate 'i' from 0 (full string suffix) up to n-1 (single char suffix).
    for i in range(n):
        suffix = string[i:]
        if _is_palindrome_ptr(suffix):
            # The non-palindromic prefix is string[:i].
            prefix_to_reverse = string[:i]
            return string + prefix_to_reverse[::-1]

    # Should be unreachable.
    return string