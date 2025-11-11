import pytest
from tests.util import get_func

gcd = lambda: get_func("greatest_common_divisor", "greatest_common_divisor")

# 1) 多步余数序列（Euclid 链较长：斐波那契相邻，互素）
@pytest.mark.parametrize("a, b, expected", [
    (4181, 2584, 1),
    (832040, 514229, 1),
])
def test_long_euclid_chain(a, b, expected):
    assert gcd()(a, b) == expected

# 2) 素数幂 vs 合数（公因子小，如 2 或 3）
@pytest.mark.parametrize("a, b, expected", [
    (3**7, 2*3**4*5, 3**4),
    (2**8, 3*2**3*7, 2**3),
])
def test_prime_power_vs_composite(a, b, expected):
    assert gcd()(a, b) == expected

# 3) 极度不平衡的量级（tiny vs huge）
@pytest.mark.parametrize("a, b, expected", [
    (1, 10**12, 1),
    (10**12, 1, 1),
    (2, 10**12, 2),
])
def test_unbalanced_magnitudes(a, b, expected):
    assert gcd()(a, b) == expected

# 4) 带符号的对称性再确认（新数值）
@pytest.mark.parametrize("a, b, expected", [
    (-270, 192, 6),
    (192, -270, 6),
])
def test_signed_symmetry_again(a, b, expected):
    assert gcd()(a, b) == expected
