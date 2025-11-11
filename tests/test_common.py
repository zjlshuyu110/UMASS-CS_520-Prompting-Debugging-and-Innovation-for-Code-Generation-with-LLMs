import pytest
from tests.util import get_func

common = lambda: get_func("common", "common")

@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121], [1, 5, 653]),
    ([5, 3, 2, 8], [3, 2], [2, 3]),
    ([4, 3, 2, 8], [3, 2, 4], [2, 3, 4]),
    ([4, 3, 2, 8], [], []),
])
def test_common(l1, l2, expected):
    assert common()(l1, l2) == expected
