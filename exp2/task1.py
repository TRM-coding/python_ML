"""
exp2/task1：基本 if 语句练习（不使用循环与复杂数据结构）。

要求：只使用基本类型（数值、字符串、布尔、None）与 if/elif/else、and/or/not、
链式比较、三元表达式等语法。
"""
from typing import Any, Optional


def is_adult(age: int) -> bool:
    """返回是否成年：>=18 为 True。"""
    raise NotImplementedError


def grade_from_score(score: int) -> str:
    """根据分数返回等级 A/B/C/D/F，边界同讲义示例。"""
    raise NotImplementedError


def classify_number(x: float) -> str:
    """返回 'positive'/'negative'/'zero'。"""
    raise NotImplementedError


def valid_percent(p: float) -> bool:
    """是否在 [0,100] 区间（含边界）。"""
    raise NotImplementedError


def safe_div(a: float, b: float) -> Optional[float]:
    """b 为 0 时返回 None，否则返回 a/b。"""
    raise NotImplementedError


def truthy_text(val: Any) -> str:
    """val 为真返回 'YES' 否则 'NO'（使用条件表达式）。"""
    raise NotImplementedError
