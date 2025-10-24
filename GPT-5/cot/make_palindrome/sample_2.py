from typing import *

def make_palindrome(string: str) -> str:
    # Already a palindrome or empty: return unchanged
    if string == string[::-1]:
        return string

    n = len(string)
    i = 0
    while i < n and string[i:] != string[i:][::-1]:
        i += 1

    # Append reverse of the non-palindromic prefix
    return string + string[:i][::-1]
