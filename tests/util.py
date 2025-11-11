# tests/util.py
import importlib
import os
from typing import Callable

# 允许取值（文件名里的家族与提示法关键字）
FAMILIES = {"GPT", "Claude", "gemini"}      # 注意大小写与你文件一致
TECHS    = {"cot", "scot"}                  # 你目前两种
DEFAULT_INDEX = "1"                         # 默认为 1；有 _2.py 时可切换

def _env(name: str, default: str | None = None) -> str:
    v = os.environ.get(name)
    if v is None:
        if default is None:
            raise RuntimeError(f"Please set environment variable: {name}")
        return default
    return v

def get_func(problem_name: str, func_name: str) -> Callable:
    """
    根据环境变量拼出模块名并返回函数对象。
    环境变量：
      FAMILY   ∈ {GPT, Claude, gemini}
      TECH     ∈ {cot, scot}
      INDEX    ∈ {"1","2",...}  (可选，默认 "1")
    组合模块：a1.<problem>_<FAMILY>_<TECH>_<INDEX>
    例如：
      FAMILY=GPT TECH=cot INDEX=1 problem=common
      -> a1.common_GPT_cot_1
    """
    family = _env("FAMILY")
    tech   = _env("TECH")
    index  = _env("INDEX", DEFAULT_INDEX)

    if family not in FAMILIES:
        raise RuntimeError(f"FAMILY={family!r} not in {sorted(FAMILIES)}")
    if tech not in TECHS:
        raise RuntimeError(f"TECH={tech!r} not in {sorted(TECHS)}")
    if not index.isdigit():
        raise RuntimeError("INDEX must be a number string like '1' or '2'")

    module_name = f"a1.{problem_name}_{family}_{tech}_{index}"
    try:
        mod = importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            f"Module {module_name!r} not found. "
            f"Check that file '{problem_name}_{family}_{tech}_{index}.py' exists in a1/."
        ) from e

    try:
        func = getattr(mod, func_name)
    except AttributeError as e:
        raise AttributeError(
            f"Function {func_name!r} not found in module {module_name!r}. "
            "Make sure the function name matches the problem (e.g., common(), "
            "greatest_common_divisor(), make_palindrome(), etc.)."
        ) from e

    return func
