from typing import *

def make_palindrome(string: str) -> str:
    def is_pal(s: str) -> bool:
        return s == s[::-1]

    def first_pal_suffix(i: int) -> int:
        # Return the smallest i such that string[i:] is a palindrome
        if i >= len(string) or is_pal(string[i:]):
            return i
        return first_pal_suffix(i + 1)

    i = first_pal_suffix(0)
    return string + string[:i][::-1]
