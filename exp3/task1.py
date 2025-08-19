"""
exp3/task1：综合练习（覆盖讲义内容与基本输入/输出；无循环）。

说明：不允许使用 for/while 等循环结构；可使用条件表达式、切片、解包等。
"""
from typing import Any, Iterable, Mapping, Sequence, Tuple, Optional


def normalize_score(raw: str) -> Optional[int]:
    """将原始字符串标准化为 0..100 的整数分数；非法返回 None。"""
    raise NotImplementedError


def summary_tuple(name: str, age_raw: str, score_raw: str) -> Tuple[str, str]:
    """
    生成简单的文本汇总（不涉及循环）：
    - age: 使用 normalize_score 的解析逻辑但不限制 0..100（只要是非负整数即可）；否则 "invalid"
    - score: 使用 normalize_score 的解析逻辑；否则 "invalid"
    返回 (age_text, score_text)
    """
    raise NotImplementedError


def pick_container(kind: str, a: Any, b: Any) -> Any:
    """
    根据 kind 选择容器：
    - 'list' -> 返回 [a, b]
    - 'tuple' -> 返回 (a, b)
    - 'set' -> 返回 {a, b}
    - 其他 -> 返回 {"a": a, "b": b}
    不使用循环。
    """
    raise NotImplementedError


def merge_mapping(a: Mapping[str, Any], b: Mapping[str, Any], prefer: str = "b") -> Mapping[str, Any]:
    """
    合并两个映射：prefer='a' 则 a 覆盖 b，同理 'b' 则 b 覆盖 a；返回新映射。
    """
    raise NotImplementedError


def slice_and_reverse(seq: Sequence[Any], start: int, end: int) -> Sequence[Any]:
    """返回切片 seq[start:end] 的倒序（同类型）。不使用循环。"""
    raise NotImplementedError
