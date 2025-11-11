from typing import *

def make_palindrome(string: str) -> str:
    def is_pal(s: str) -> bool:
        return s == s[::-1]

    n = len(string)
    # Find the earliest i such that string[i:] is a palindrome.
    for i in range(n + 1):
        if is_pal(string[i:]):
            # Append reverse of the prefix string[:i]
            return string + string[:i][::-1]
    return string  # unreachable, but keeps type checkers happy
