import pytest
from tests.util import get_func

fn = lambda: get_func("get_odd_collatz", "get_odd_collatz")

@pytest.mark.parametrize("n, expected", [
    (14, [1, 5, 7, 11, 13, 17]),
    (5,  [1, 5]),
    (12, [1, 3, 5]),
    (1,  [1]),
])
def test_get_odd_collatz(n, expected):
    assert fn()(n) == expected
