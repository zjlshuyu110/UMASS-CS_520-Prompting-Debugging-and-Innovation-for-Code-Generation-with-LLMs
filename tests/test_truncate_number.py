import pytest
from tests.util import get_func

fn = lambda: get_func("truncate_number", "truncate_number")

@pytest.mark.parametrize("x, expected", [
    (3.5,   0.5),
    (1.33,  0.33),
    (123.456, 0.456),
])
def test_truncate_number(x, expected):
    # 浮点数用容差比较
    assert abs(fn()(x) - expected) < 1e-6
