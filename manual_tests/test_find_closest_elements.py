from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sample code here
    s = sorted(numbers)
    pairs = list(zip(s, s[1:]))  # consecutive pairs
    # Choose the pair with minimal difference
    a, b = min(pairs, key=lambda p: p[1] - p[0])
    return (a, b)
   
    
    pass


print("Testing find_closest_elements...")
tests = [
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], (3.9, 4.0)),
    ([1.0, 2.0, 5.9, 4.0, 5.0], (5.0, 5.9)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], (2.0, 2.2)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], (2.0, 2.0)),
    ([1.1, 2.2, 3.1, 4.1, 5.1], (2.2, 3.1)),
]

passed = 0
for i, (nums, expected) in enumerate(tests, 1):
    result = find_closest_elements(nums)
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