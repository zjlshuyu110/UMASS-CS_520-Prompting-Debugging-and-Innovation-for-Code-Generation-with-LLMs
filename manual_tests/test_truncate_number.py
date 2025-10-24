def truncate_number(number: float) -> float:
    # sample code here
    s = f"{number:.15f}"
    if "." not in s:
        return 0.0
    int_part, dec_part = s.split(".")
    return float("0." + dec_part.rstrip("0")) if dec_part.strip("0") else 0.0   
    pass

print("Testing truncate_number...")
tests = [
    (3.5, 0.5),
    (1.33, 0.33),
    (123.456, 0.456),
]

passed = 0
for i, (num, expected) in enumerate(tests, 1):
    result = truncate_number(num)
    # 浮点数比较用误差
    is_pass = abs(result - expected) < 1e-6
    status = "✓ PASS" if is_pass else "✗ FAIL"
    print(f"Test {i}: {result:.6f} (expected {expected:.6f}) {status}")
    if is_pass:
        passed += 1

print(f"\nresult: {passed}/{len(tests)} pass")
if passed == len(tests):
    print("✓ PASS！")
else:
    print("✗ FAIL")