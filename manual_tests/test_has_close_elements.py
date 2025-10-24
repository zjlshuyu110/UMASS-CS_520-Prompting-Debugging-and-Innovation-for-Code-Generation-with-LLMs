from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # 👇 sample code here
    n = len(numbers)
    if n < 2 or threshold <= 0:
        return False

    for i in range(n):
        xi = numbers[i]
        for j in range(i + 1, n):
            if abs(xi - numbers[j]) < threshold:
                return True
    return False
   
    pass

# 官方测试用例
print("Testing has_close_elements...")
tests = [
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3, True),
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05, False),
    ([1.0, 2.0, 5.9, 4.0, 5.0], 0.95, True),
    ([1.0, 2.0, 5.9, 4.0, 5.0], 0.8, False),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1, True),
    ([1.1, 2.2, 3.1, 4.1, 5.1], 1.0, True),
    ([1.1, 2.2, 3.1, 4.1, 5.1], 0.5, False),
]

passed = 0
for i, (nums, thresh, expected) in enumerate(tests, 1):
    result = has_close_elements(nums, thresh)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    print(f"Test {i}: {result} (expected {expected}) {status}")
    if result == expected:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ PASS！")
else:
    print("✗ FAIL")