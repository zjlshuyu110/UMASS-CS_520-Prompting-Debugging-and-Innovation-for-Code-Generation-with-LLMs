import pytest
from tests.util import get_func

fn = lambda: get_func("intersperse", "intersperse")

@pytest.mark.parametrize("nums, delim, expected", [
    ([], 7, []),
    ([5, 6, 3, 2], 8, [5, 8, 6, 8, 3, 8, 2]),
    ([2, 2, 2], 2, [2, 2, 2, 2, 2]),
])
def test_intersperse(nums, delim, expected):
    assert fn()(nums, delim) == expected
