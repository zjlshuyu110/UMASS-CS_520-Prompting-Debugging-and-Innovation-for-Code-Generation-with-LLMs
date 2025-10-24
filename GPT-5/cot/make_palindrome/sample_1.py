from typing import *

def make_palindrome(string: str) -> str:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    n = len(string)
    for i in range(n):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return string  # only reached when string is empty
