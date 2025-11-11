import pytest
from tests.util import get_func

fn = lambda: get_func("has_close_elements", "has_close_elements")

# 1) threshold <= 0 触发早返回
@pytest.mark.parametrize("nums, thresh, expected", [
    ([1.0, 2.0], 0.0, False),
    ([1.0, 2.0], -1.0, False),
])
def test_threshold_nonpositive(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 2) len(numbers) < 2 触发早返回
@pytest.mark.parametrize("nums, thresh, expected", [
    ([], 1.0, False),
    ([1.23], 0.5, False),
])
def test_len_lt_2(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 3) 排序后相邻才可比较（无序输入 -> 排序后相邻）
@pytest.mark.parametrize("nums, thresh, expected", [
    ([3.0, 1.01, 2.0, 1.0], 0.02, True),  # 1.00 与 1.01 排序后相邻且差0.01<0.02
    ([10.0, 8.0, 3.0, 0.0], 1.0, False),  # 相邻差均≥1
])
def test_unsorted_adjacency(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 4) NaN 处理：遇到 NaN 会重置 prev；不跨 NaN 比较
@pytest.mark.parametrize("nums, thresh, expected", [
    ([1.0, float('nan')], 0.5, False),                 # 只有一个有效数 + NaN
    ([1.0, float('nan'), 1.1], 0.05, False),           # NaN 使 prev 置空，不比较跨 NaN
    ([1.0, float('nan'), 1.00000001], 1e-7, False),    # NaN 夹在中间 -> 不会命中近邻
    ([1.0, 1.00000001, float('nan')], 1e-7, True),     # 近邻发生在 NaN 之前 -> 命中 True
    ([2.0, 2.0, float('nan')], 0.1, True),             # 等值分支，在遇到 NaN 前已返回 True
])
def test_nan_handling(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 5) 等值路径（含 +inf/+inf、-inf/-inf、+0.0/-0.0）
@pytest.mark.parametrize("nums, thresh, expected", [
    ([0.0, -0.0], 1.0, True),                        # +0.0 == -0.0 -> True
    ([float('inf'), float('inf')], 0.1, True),       # +inf == +inf -> True（不做 inf-inf）
    ([float('-inf'), float('-inf')], 5.0, True),     # -inf == -inf -> True
    ([float('-inf'), float('inf')], 1e9, False),     # -inf 与 +inf 不相等，diff 为 inf，不可能 < threshold
])
def test_equality_paths(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 6) diff < threshold 的边界：等于阈值 False；真小于 True；略大于 True
@pytest.mark.parametrize("nums, thresh, expected", [
    ([0.0, 0.1], 0.1, False),                  # 恰好等于阈值 -> False（严格 <）
    ([0.0, 0.1], 0.1000000001, True),          # 阈值略大 -> True
    ([0.0, 0.1], 0.0999999999, False),         # 阈值略小 -> False（0.1 不小于 0.0999999999）
    ([0.0, 1e-10], 1e-9, True),                # 稳健的“真小于”用例
])
def test_threshold_boundaries(nums, thresh, expected):
    res = fn()(nums, thresh)
    assert res == expected

# 7) 负数与混合符号；以及分离很远但彼此不近
@pytest.mark.parametrize("nums, thresh, expected", [
    ([-3.5, -3.4], 0.11, True),     # 差 0.1 < 0.11
    ([-3.5, -3.4], 0.1, False),     # 差 0.1 == 0.1 -> False
    ([-2.0, 100.0], 1.0, False),    # 相距甚远
    ([-1.0, 0.0, 1.0], 0.9, False), # 最近是 0 与 ±1 差1.0，不满足 <0.9
])
def test_negative_and_far_apart(nums, thresh, expected):
    assert fn()(nums, thresh) == expected

# 8) 通过 NaN 片段后的近邻检测（确保 prev reset 后仍可在后段命中）
@pytest.mark.parametrize("nums, thresh, expected", [
    ([5.0, float('nan'), 7.0, 7.0], 0.2, True),     # 后段等值命中
    ([5.0, float('nan'), 7.0, 7.3], 0.2, False),    # 后段差 0.3 >= 0.2
])
def test_split_by_nan_then_detect(nums, thresh, expected):
    assert fn()(nums, thresh) == expected
