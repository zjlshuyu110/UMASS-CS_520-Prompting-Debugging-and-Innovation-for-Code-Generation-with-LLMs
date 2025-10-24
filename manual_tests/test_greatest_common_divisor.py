def greatest_common_divisor(a: int, b: int) -> int:
    # sample code put here 
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a

    pass

print("Testing greatest_common_divisor...")
tests = [
    (3, 7, 1),
    (10, 15, 5),
    (49, 14, 7),
    (144, 60, 12),
]

passed = 0
for i, (a, b, expected) in enumerate(tests, 1):
    result = greatest_common_divisor(a, b)
    is_pass = result == expected
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: gcd({a}, {b}) = {result} (expected {expected}) {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ PASS！")
else:
    print("✗ FAIL")