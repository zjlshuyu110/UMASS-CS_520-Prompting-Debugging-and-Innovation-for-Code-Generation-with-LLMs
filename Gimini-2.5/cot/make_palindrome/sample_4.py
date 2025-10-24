def make_palindrome(string: str) -> str:
    """
    Finds the shortest palindrome that begins with the supplied string
    using a while loop to locate the split point 'i'.
    """
    n = len(string)
    if n == 0:
        return ""

    # 'i' is the length of the prefix (and thus the index where the suffix starts).
    # We are looking for the smallest 'i' such that string[i:] is a palindrome.
    i = 0
    while i < n:
        suffix = string[i:]
        if suffix == suffix[::-1]:
            break  # Found the longest palindromic suffix string[i:]
        i += 1

    # The prefix to reverse is string[:i].
    # If string is a palindrome, i=0, prefix[:0] is "", result is string + "".
    # If string is 'cat', i=2 ('t' is palindrome), prefix[:2] is 'ca', result is 'cat' + 'ac'.
    prefix_to_reverse = string[:i]
    return string + prefix_to_reverse[::-1]