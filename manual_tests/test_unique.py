def unique(l: list):
    #sample code here
    seen = set()
    unique_items = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(unique_items)
    pass

print("Testing unique...")
tests = [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [0, 2, 3, 5, 9, 123]),
]

passed = 0
for i, (input_list, expected) in enumerate(tests, 1):
    result = unique(input_list)
    is_pass = result == expected
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: {result} (expected {expected}) {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ PASS！")
else:
    print("✗ SOME FAIL")