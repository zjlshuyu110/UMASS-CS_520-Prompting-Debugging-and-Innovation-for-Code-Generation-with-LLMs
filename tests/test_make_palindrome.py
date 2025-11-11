import pytest
from tests.util import get_func

fn = lambda: get_func("make_palindrome", "make_palindrome")

@pytest.mark.parametrize("s, expected", [
    ("", ""),
    ("x", "x"),
    ("xyz", "xyzyx"),
    ("xyx", "xyx"),
    ("jerry", "jerryrrej"),
])
def test_make_palindrome(s, expected):
    assert fn()(s) == expected
