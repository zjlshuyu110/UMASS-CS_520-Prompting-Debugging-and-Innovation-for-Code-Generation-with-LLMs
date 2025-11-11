import pytest
from tests.util import get_func

fn = lambda: get_func("has_close_elements", "has_close_elements")

# 1) 全 NaN -> False
@pytest.mark.parametrize("nums, thresh, expected", [
    ([float('nan')], 1.0, False),
    ([float('nan'), float('nan')], 1.0, False),
])
def test_all_nans(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 2) 含无穷大：只有相等的无穷大才 True；无穷与有限差为 inf 不会 < threshold
@pytest.mark.parametrize("nums, thresh, expected", [
    ([float('inf'), float('inf'), 1e9], 0.5, True),          # inf==inf -> True
    ([float('-inf'), -1e9, float('inf')], 1e308, False),     # -inf 与 +inf 不可触发 < threshold
])
def test_infinity_cases(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 3) 巨大阈值轻松命中（任意有限相邻差 < threshold）
@pytest.mark.parametrize("nums, thresh, expected", [
    ([0.0, 1000.0, 3000.0], 5000.0, True),  # 相邻差 1000 < 5000
])
def test_huge_threshold(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 4) 极小差距（亚正常值）
@pytest.mark.parametrize("nums, thresh, expected", [
    ([0.0, 1e-300], 1e-299, True),  # 1e-300 < 1e-299
    ([0.0, 1e-300], 1e-310, False), # 1e-300 不小于 1e-310
])
def test_subnormal_gaps(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 5) 重复块在排序后相邻才触发
@pytest.mark.parametrize("nums, thresh, expected", [
    ([3.0, 1.0, 2.0, 2.0], 0.1, True),   # 2.0 与 2.0 排序后相邻 -> 等值 True
    ([5.0, 1.0, 3.0, 2.0], 0.5, False),  # 无任意相邻差 < 0.5
])
def test_duplicate_blocks_and_no_hit(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 6) 多个 NaN 片段，确保 prev 多次 reset，但近邻对在 NaN 之前相邻出现
@pytest.mark.parametrize("nums, thresh, expected", [
    ([float('nan'), 1.0, 1.0000001, float('nan')], 1e-6, True),  # 1.0 与 1.0000001 在 NaN 之前且相邻 -> True
    ([float('nan'), -5.0, float('nan'), 10.0], 1.0, False),      # 无近邻
])
def test_multiple_nan_segments(nums, thresh, expected):
    assert fn()(nums, thresh) == expected
