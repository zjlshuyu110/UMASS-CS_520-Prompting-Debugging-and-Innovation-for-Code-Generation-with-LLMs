import pytest
from tests.util import get_func

gcd = lambda: get_func("greatest_common_divisor", "greatest_common_divisor")

@pytest.mark.parametrize("a, b, expected", [
    (3, 7, 1),
    (10, 15, 5),
    (49, 14, 7),
    (144, 60, 12),
])
def test_greatest_common_divisor(a, b, expected):
    assert gcd()(a, b) == expected
