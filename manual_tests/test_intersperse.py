from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    # sample code here
    if len(numbers) <= 1:
        return numbers[:]
    result = [x for pair in zip(numbers, [delimeter] * len(numbers)) for x in pair][:-1]
    return result
    pass

print("Testing intersperse...")
tests = [
    ([], 7, []),
    ([5, 6, 3, 2], 8, [5, 8, 6, 8, 3, 8, 2]),
    ([2, 2, 2], 2, [2, 2, 2, 2, 2]),
]

passed = 0
for i, (nums, delim, expected) in enumerate(tests, 1):
    result = intersperse(nums, delim)
    is_pass = result == expected
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: {result} (expected {expected}) {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ PASS！")
else:
    print("✗ FAIL")