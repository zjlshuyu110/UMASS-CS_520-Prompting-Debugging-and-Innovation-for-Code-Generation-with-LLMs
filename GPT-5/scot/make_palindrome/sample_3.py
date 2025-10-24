from typing import *

def make_palindrome(string: str) -> str:
    s = string
    n = len(s)
    if n <= 1 or s == s[::-1]:
        return s

    # Track the longest palindrome that ends at n-1
    best_len = 1  # at least the last char
    # Consider all centers (odd and even), expand, and keep those ending at n-1
    for center in range(n):
        # Odd-length palindromes: (center, center)
        l, r = center, center
        while l >= 0 and r < n and s[l] == s[r]:
            if r == n - 1:
                best_len = max(best_len, r - l + 1)
            l -= 1
            r += 1
        # Even-length palindromes: (center, center+1)
        l, r = center, center + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r == n - 1:
                best_len = max(best_len, r - l + 1)
            l -= 1
            r += 1

    i = n - best_len  # start of the longest palindromic suffix
    return s + s[:i][::-1]
