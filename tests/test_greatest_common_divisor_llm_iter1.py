import pytest
from tests.util import get_func

gcd = lambda: get_func("greatest_common_divisor", "greatest_common_divisor")

# 1) (0, n) 和 (n, 0) 分支（含负数）
@pytest.mark.parametrize("a, b, expected", [
    (0, 7, 7),
    (7, 0, 7),
    (0, -7, 7),
    (-7, 0, 7),
])
def test_zero_branches(a, b, expected):
    assert gcd()(a, b) == expected

# 2) (0, 0) -> 0 （按实现/文档）
def test_both_zero():
    assert gcd()(0, 0) == 0

# 3) 相等数字（含负数相等）
@pytest.mark.parametrize("a, b, expected", [
    (12, 12, 12),
    (-12, -12, 12),  # 绝对值处理后返回非负
])
def test_equal_numbers(a, b, expected):
    assert gcd()(a, b) == expected

# 4) 互素（多次 while 迭代）
@pytest.mark.parametrize("a, b, expected", [
    (55, 34, 1),
    (101, 64, 1),
])
def test_coprime_pairs(a, b, expected):
    assert gcd()(a, b) == expected

# 5) 整除快速路径（余数为 0）
@pytest.mark.parametrize("a, b, expected", [
    (100, 25, 25),
    (81, 9, 9),
    (72, 36, 36),
])
def test_divisibility_quick_exit(a, b, expected):
    assert gcd()(a, b) == expected

# 6) 对称性：gcd(a, b) == gcd(b, a)
@pytest.mark.parametrize("a, b, expected", [
    (27, 15, 3),
    (15, 27, 3),   # 交换参数
    (-24, 18, 6),
    (18, -24, 6),  # 交换且含负数
])
def test_symmetry(a, b, expected):
    assert gcd()(a, b) == expected

# 7) 较大的数值（多轮迭代，但确定且快速）
@pytest.mark.parametrize("a, b, expected", [
    (987654, 123456, 6),  # 987654 % 123456 = 6 -> gcd(123456, 6) = 6
    (12345678, 876543, 3),
])
def test_large_values(a, b, expected):
    assert gcd()(a, b) == expected
