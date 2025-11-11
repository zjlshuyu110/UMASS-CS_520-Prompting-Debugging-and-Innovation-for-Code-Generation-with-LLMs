import pytest
from tests.util import get_func

fn = lambda: get_func("has_close_elements", "has_close_elements")

# 1) 长列表：只有一对在排序后相邻且接近
@pytest.mark.parametrize("nums, thresh, expected", [
    ([10.0, 1.0, 7.0, 4.0, 4.001, 100.0, 50.0], 0.01, True),  # 4.0 与 4.001 差 0.001 < 0.01
    ([10.0, 1.0, 7.0, 4.0, 4.02, 100.0, 50.0], 0.01, False),  # 最小相邻差 >= 0.02
])
def test_long_list_single_close_pair(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 2) 含 (-inf, finite, +inf)：只有有限对的相邻差可能命中；严格 '<' 演示
@pytest.mark.parametrize("nums, thresh, expected", [
    ([float('-inf'), -0.2, 0.1, float('inf')], 0.31, True),  # 相邻差 0.3 < 0.31 -> True
    ([float('-inf'), -0.2, 0.1, float('inf')], 0.3, False),  # 等于 0.3（严格 <）-> False
])
def test_inf_with_finite_pairs_strict_threshold(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 3) 精确构造：just-above / equal / just-below 最小相邻差
@pytest.mark.parametrize("nums, thresh, expected", [
    ([0.0, 0.25, 0.5], 0.26, True),   # min gap 0.25 < 0.26
    ([0.0, 0.25, 0.5], 0.25, False),  # 等于阈值 -> False
    ([0.0, 0.25, 0.5], 0.24, False),  # 小于最小相邻差 -> False
])
def test_just_above_below_min_gap(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 4) 远距离混合（应 False）
@pytest.mark.parametrize("nums, thresh, expected", [
    ([-1000.0, -100.0, 0.0, 100.0, 1000.0], 10.0, False),
    ([0.0, 100.0, 200.0, 300.0], 50.0, False),
])
def test_far_apart_mixed_signs(nums, thresh, expected):
    assert fn()(nums, thresh) == expected
