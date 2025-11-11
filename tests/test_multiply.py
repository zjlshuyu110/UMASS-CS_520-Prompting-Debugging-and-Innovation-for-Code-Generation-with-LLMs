import pytest
from tests.util import get_func

fn = lambda: get_func("multiply", "multiply")

@pytest.mark.parametrize("a, b, expected", [
    (148, 412, 16),
    (19, 28, 72),
    (2020, 1851, 0),
    (14, -15, 20),
    (76, 67, 42),
    (17, 27, 49),
    (0, 1, 0),
    (0, 0, 0),
])
def test_multiply(a, b, expected):
    assert fn()(a, b) == expected
