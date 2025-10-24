def multiply(a, b):
    # sample code here
    return (abs(a) % 10) * (abs(b) % 10)
    pass

print("Testing multiply...")
tests = [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (76, 67, 42),
    (17, 27, 49),
    (0, 1, 0),
    (0, 0, 0),
]

passed = 0
for i, (a, b, expected) in enumerate(tests, 1):
    result = multiply(a, b)
    is_pass = result == expected
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: multiply({a}, {b}) = {result} (expected {expected}) {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ this sample all pass!")
else:
    print("✗ SOME FAIL")