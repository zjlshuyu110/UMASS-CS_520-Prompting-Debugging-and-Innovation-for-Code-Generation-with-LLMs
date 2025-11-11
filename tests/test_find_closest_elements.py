import pytest
from tests.util import get_func

fn = lambda: get_func("find_closest_elements", "find_closest_elements")

@pytest.mark.parametrize("nums, expected", [
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], (3.9, 4.0)),
    ([1.0, 2.0, 5.9, 4.0, 5.0],       (5.0, 5.9)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.2],  (2.0, 2.2)),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0],  (2.0, 2.0)),
    ([1.1, 2.2, 3.1, 4.1, 5.1],       (2.2, 3.1)),
])
def test_find_closest_elements(nums, expected):
    assert fn()(nums) == expected
