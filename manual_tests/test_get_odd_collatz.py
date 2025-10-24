def get_odd_collatz(n):
    # sample code here
    def collatz_gen(x):
        while True:
            yield x
            if x == 1:
                break
            x = 3 * x + 1 if x % 2 else x // 2

    return sorted({num for num in collatz_gen(n) if num % 2})
    pass

print("Testing get_odd_collatz...")
tests = [
    (14, [1, 5, 7, 11, 13, 17]),
    (5, [1, 5]),
    (12, [1, 3, 5]),
    (1, [1]),
]

passed = 0
for i, (n, expected) in enumerate(tests, 1):
    result = get_odd_collatz(n)
    is_pass = result == expected
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: get_odd_collatz({n}) = {result} (expected {expected}) {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ this sample all pass!")
else:
    print("✗ SOME FAIL")