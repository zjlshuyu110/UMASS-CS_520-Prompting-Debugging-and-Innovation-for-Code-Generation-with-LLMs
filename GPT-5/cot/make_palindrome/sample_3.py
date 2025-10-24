from typing import *

def make_palindrome(string: str) -> str:
    def is_pal_suffix(start: int) -> bool:
        # Check if string[start:] is a palindrome using two pointers
        l, r = start, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

    n = len(string)
    for i in range(n):
        if is_pal_suffix(i):
            return string + string[:i][::-1]
    return string
