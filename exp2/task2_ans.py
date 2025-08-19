"""
exp2/task2 答案：复杂 if 嵌套（无循环）。
"""
from typing import Optional


def parse_age(raw: str) -> Optional[int]:
    if raw is None or raw == "":
        return None
    if raw.isdigit():
        return int(raw)
    return None


def classify_user(age_raw: str, member_raw: str) -> str:
    age = parse_age(age_raw)
    if age is None:
        return "invalid"
    if age < 18:
        return "minor"
    # 成年
    m = member_raw.strip().lower() if member_raw is not None else ""
    if m == "y" or m == "yes":
        return "adult-member"
    else:
        return "adult-nonmember"


def compare_numbers(a_raw: str, b_raw: str) -> str:
    if a_raw is None or b_raw is None:
        return "invalid"
    a_raw = a_raw.strip()
    b_raw = b_raw.strip()
    if a_raw == "" or b_raw == "":
        return "invalid"
    # 简单解析为浮点（不使用异常处理的循环等）
    try:
        a = float(a_raw)
        b = float(b_raw)
    except Exception:
        return "invalid"
    if a > b:
        return ">"
    elif a < b:
        return "<"
    else:
        return "="


def choose_operation(op: str, x: float, y: float) -> Optional[float]:
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y == 0:
            return None
        return x / y
    else:
        return None
