def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str: # sample code here
    s = string
    n = len(s)
    if n <= 1 or s == s[::-1]:
        return s

    base = 911382323
    mod  = 1_000_000_007

    # Precompute powers
    powb = [1] * (n + 1)
    for i in range(1, n + 1):
        powb[i] = (powb[i - 1] * base) % mod

    # Prefix hash of s
    pref = [0] * (n + 1)
    for i, ch in enumerate(s, 1):
        pref[i] = (pref[i - 1] * base + ord(ch)) % mod

    # Prefix hash of reversed s
    rs = s[::-1]
    rpref = [0] * (n + 1)
    for i, ch in enumerate(rs, 1):
        rpref[i] = (rpref[i - 1] * base + ord(ch)) % mod

    def hash_sub(pref_arr, l, r):
        """hash of s[l:r] using prefix array for that string"""
        return (pref_arr[r] - pref_arr[l] * powb[r - l]) % mod

    # Find earliest i where s[i:] == reverse(s[i:])
    # reverse(s[i:]) is exactly rs[:n - i]
    for i in range(n + 1):
        h1 = hash_sub(pref, i, n)         # s[i:n]
        h2 = hash_sub(rpref, 0, n - i)    # rs[0:n-i] == reverse(s[i:n])
        if h1 == h2:
            return s + s[:i][::-1]

    return s

print("Testing make_palindrome...")
tests = [
    ('', ''),
    ('x', 'x'),
    ('xyz', 'xyzyx'),
    ('xyx', 'xyx'),
    ('jerry', 'jerryrrej'),
]

passed = 0
for i, (input_str, expected) in enumerate(tests, 1):
    result = make_palindrome(input_str)
    is_pass = result == expected
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: '{result}' (expected '{expected}') {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ PASS！")
else:
    print("✗ FAIL")