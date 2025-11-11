import pytest
from tests.util import get_func

gcd = lambda: get_func("greatest_common_divisor", "greatest_common_divisor")

# 1) 包含 1 的情形（gcd(a,1)=1），含负数
@pytest.mark.parametrize("a, b, expected", [
    (1, 999, 1),
    (999, 1, 1),
    (-1, 12345, 1),
    (12345, -1, 1),
])
def test_with_one(a, b, expected):
    assert gcd()(a, b) == expected

# 2) 幂次对（2^k, 2^m）
@pytest.mark.parametrize("a, b, expected", [
    (2**10, 2**5, 2**5),
    (2**6, 2**9, 2**6),
])
def test_power_of_two_pairs(a, b, expected):
    assert gcd()(a, b) == expected

# 3) 连续整数 (n, n+1) -> 1（与 iter1 不同的数据点）
@pytest.mark.parametrize("n", [2, 50, 9999])
def test_consecutive_integers(n):
    assert gcd()(n, n+1) == 1
    assert gcd()(n+1, n) == 1

# 4) 负正混合但绝对值相等，如 (-k, k) -> k（与 iter1 不同的数据点）
@pytest.mark.parametrize("k", [7, 64, 512])
def test_neg_pos_equal_abs(k):
    assert gcd()(-k, k) == k
    assert gcd()(k, -k) == k
