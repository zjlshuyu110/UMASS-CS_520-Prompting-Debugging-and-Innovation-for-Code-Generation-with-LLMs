from typing import *

def make_palindrome(string: str) -> str:
    n = len(string)

    def pal_suffix_start(i: int) -> bool:
        # True iff string[i:] is palindrome
        # Compare mirrored pairs inside the suffix
        m = (n - i) // 2
        return all(string[i + k] == string[n - 1 - k] for k in range(m))

    i = next((idx for idx in range(n) if pal_suffix_start(idx)), n)
    # If i == n, string is empty; appending reversed prefix is a no-op
    return string + string[:i][::-1]
