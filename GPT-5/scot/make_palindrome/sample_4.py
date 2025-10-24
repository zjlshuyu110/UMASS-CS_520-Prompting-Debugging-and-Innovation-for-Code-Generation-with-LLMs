from typing import *

def make_palindrome(string: str) -> str:
    s = string
    n = len(s)
    if n <= 1 or s == s[::-1]:
        return s

    # dp[l][r] = True if s[l:r+1] is palindrome
    dp = [[False] * n for _ in range(n)]
    best_len = 1  # suffix palindrome length
    # length 1
    for i in range(n):
        dp[i][i] = True
    # length 2+
    for length in range(2, n + 1):
        for l in range(0, n - length + 1):
            r = l + length - 1
            if s[l] == s[r]:
                if length == 2 or dp[l + 1][r - 1]:
                    dp[l][r] = True
                    if r == n - 1:
                        best_len = max(best_len, length)

    i = n - best_len
    return s + s[:i][::-1]
