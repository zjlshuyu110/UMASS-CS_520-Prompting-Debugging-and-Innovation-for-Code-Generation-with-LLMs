import pytest
from tests.util import get_func

fn = lambda: get_func("has_close_elements", "has_close_elements")

@pytest.mark.parametrize("nums, thresh, expected", [
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3,  True),
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05, False),
    ([1.0, 2.0, 5.9, 4.0, 5.0],      0.95, True),
    ([1.0, 2.0, 5.9, 4.0, 5.0],      0.8,  False),
    ([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1,  True),
    ([1.1, 2.2, 3.1, 4.1, 5.1],      1.0,  True),
    ([1.1, 2.2, 3.1, 4.1, 5.1],      0.5,  False),
])
def test_has_close_elements(nums, thresh, expected):
    assert fn()(nums, thresh) == expected
