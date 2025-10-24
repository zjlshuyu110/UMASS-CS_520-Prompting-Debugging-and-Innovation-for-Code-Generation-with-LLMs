
def common(l1: list, l2: list):
    # sample 代码到这里
    """Return sorted list of unique elements present in both lists."""
    return sorted(set(l1).intersection(l2))



print("Testing common...")
tests = [
    ([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121], [1, 5, 653]),
    ([5, 3, 2, 8], [3, 2], [2, 3]),
    ([4, 3, 2, 8], [3, 2, 4], [2, 3, 4]),
    ([4, 3, 2, 8], [], []),
]

passed = 0
for i, (l1, l2, expected) in enumerate(tests, 1):
    result = common(l1, l2)
    is_pass = result == expected
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: {result} (expected {expected}) {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ this sample all pass!")
else:
    print("✗ SOME FAIL")