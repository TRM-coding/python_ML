"""
exp3/task1 答案：综合练习（无循环）。
"""
from typing import Any, Iterable, Mapping, Sequence, Tuple, Optional


def normalize_score(raw: str) -> Optional[int]:
    if raw is None:
        return None
    raw = raw.strip()
    if not raw.isdigit():
        return None
    val = int(raw)
    if 0 <= val <= 100:
        return val
    return None


def summary_tuple(name: str, age_raw: str, score_raw: str) -> Tuple[str, str]:
    # age：非负整数则返回原始数字字符串，否则 invalid
    def _parse_age(x: str) -> Optional[int]:
        if x is None:
            return None
        x = x.strip()
        if not x.isdigit():
            return None
        val = int(x)
        return val if val >= 0 else None

    age_val = _parse_age(age_raw)
    score_val = normalize_score(score_raw)
    age_text = str(age_val) if age_val is not None else "invalid"
    score_text = str(score_val) if score_val is not None else "invalid"
    return age_text, score_text


def pick_container(kind: str, a: Any, b: Any) -> Any:
    k = (kind or "").lower()
    if k == "list":
        return [a, b]
    elif k == "tuple":
        return (a, b)
    elif k == "set":
        return {a, b}
    else:
        return {"a": a, "b": b}


def merge_mapping(a: Mapping[str, Any], b: Mapping[str, Any], prefer: str = "b") -> Mapping[str, Any]:
    if prefer == "a":
        return {**dict(b), **dict(a)}
    else:
        return {**dict(a), **dict(b)}


def slice_and_reverse(seq: Sequence[Any], start: int, end: int) -> Sequence[Any]:
    part = seq[start:end]
    # 尽量保持同类型返回
    if isinstance(part, list):
        return part[::-1]
    if isinstance(part, tuple):
        return part[::-1]
    # 回退为列表
    return list(part)[::-1]
