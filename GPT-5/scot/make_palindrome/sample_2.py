from typing import *

def make_palindrome(string: str) -> str:
    n = len(string)

    def suffix_is_pal(start: int) -> bool:
        l, r = start, n - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

    for i in range(n + 1):
        if suffix_is_pal(i):
            return string + string[:i][::-1]
    return string
