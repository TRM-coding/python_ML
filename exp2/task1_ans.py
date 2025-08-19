"""
exp2/task1 答案：基本 if 语句。
"""
from typing import Any, Optional


def is_adult(age: int) -> bool:
    return True if age >= 18 else False


def grade_from_score(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def classify_number(x: float) -> str:
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"


def valid_percent(p: float) -> bool:
    return True if 0 <= p <= 100 else False


def safe_div(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def truthy_text(val: Any) -> str:
    return "YES" if bool(val) else "NO"
