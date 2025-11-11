import pytest
from tests.util import get_func

fn = lambda: get_func("unique", "unique")

@pytest.mark.parametrize("arr, expected", [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [0, 2, 3, 5, 9, 123]),
])
def test_unique(arr, expected):
    assert fn()(arr) == expected
