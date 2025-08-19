"""
exp3/task1：综合练习（覆盖讲义内容与基本输入/输出；无循环）。

要求与范围：
- 不允许使用 for/while 等循环结构；可使用条件表达式、切片、解包、内置函数等。
- 题目覆盖 lec3_and_lec4.md 的基础内容与简单的输入/输出规范化思路。
- 重点在“没有循环时如何用内置特性完成小任务”。

每个函数下方都提供了更详细的说明与示例（并不是严格的 doctest，仅用于说明预期行为）。
"""
from typing import Any, Iterable, Mapping, Sequence, Tuple, Optional


def normalize_score(raw: str) -> Optional[int]:
    """
    将原始“分数字符串”标准化为 0..100 的整数；非法输入返回 None。

    规则：
    - 先去除首尾空白（例如 " 99 \n" -> "99"）。
    - 仅接受“纯数字字符串”（正整数或零），即 `str.isdigit()` 为 True。
    - 转为 int 后仅当 0 <= 分数 <= 100 时返回该整数，否则返回 None。

    示例：
    - normalize_score("0") -> 0
    - normalize_score(" 99 ") -> 99
    - normalize_score("101") -> None  （超出范围）
    - normalize_score("-1") -> None   （不是纯数字字符串）
    - normalize_score("ab9") -> None  （包含非数字字符）
    - normalize_score("009") -> 9     （前导 0 视为合法，int("009") == 9）
    """
    raise NotImplementedError


def summary_tuple(name: str, age_raw: str, score_raw: str) -> Tuple[str, str]:
    """
    生成简单的文本汇总，返回 (age_text, score_text)。

    规则：
    - age_text：按“非负整数”来解析 `age_raw`（与 normalize_score 类似，但不设上限）。
        - 先去空白；必须是纯数字字符串；int 值必须 >= 0 才合法；合法则返回该数字的字符串形式。
        - 否则返回 "invalid"。
    - score_text：使用 normalize_score 的逻辑解析 `score_raw`，合法则返回数字的字符串形式，否则 "invalid"。

    示例：
    - summary_tuple("Tom", "20", "88") -> ("20", "88")
    - summary_tuple("Tom", "-1", "88") -> ("invalid", "88")
    - summary_tuple("Tom", "20", "101") -> ("20", "invalid")
    """
    raise NotImplementedError


def pick_container(kind: str, a: Any, b: Any) -> Any:
    """
    根据 `kind` 选择并返回一个包含 a 与 b 的容器（不使用循环）。

    大小写不敏感：
    - kind == 'list'  -> 返回 [a, b]
    - kind == 'tuple' -> 返回 (a, b)
    - kind == 'set'   -> 返回 {a, b}
    - 其他值          -> 返回 {"a": a, "b": b}

    示例：
    - pick_container('list', 1, 2) -> [1, 2]
    - pick_container('tuple', 1, 2) -> (1, 2)
    - pick_container('set', 1, 2) -> {1, 2}
    - pick_container('dict', 1, 2) -> {"a": 1, "b": 2}
    """
    raise NotImplementedError


def merge_mapping(a: Mapping[str, Any], b: Mapping[str, Any], prefer: str = "b") -> Mapping[str, Any]:
    """
    合并两个映射并返回新映射，不修改入参。

    - 当 prefer='a'：以 a 为优先，表示“a 覆盖 b”，即重复键取 a 的值。
    - 当 prefer='b'：以 b 为优先，表示“b 覆盖 a”，即重复键取 b 的值（默认）。

    等价示意：
    - prefer='a' -> {**b, **a}
    - prefer='b' -> {**a, **b}

    示例：
    a = {"x": 1, "k": 0}, b = {"x": 9, "y": 2}
    - merge_mapping(a, b, prefer='b') -> {"x": 9, "k": 0, "y": 2}
    - merge_mapping(a, b, prefer='a') -> {"x": 1, "k": 0, "y": 2}
    """
    raise NotImplementedError


def slice_and_reverse(seq: Sequence[Any], start: int, end: int) -> Sequence[Any]:
    """
    返回切片 `seq[start:end]` 的倒序，尽量保持与切片结果相同的类型（不使用循环）。

    说明：
    - 当 seq 为 list 或 tuple 时，返回同类型的倒序切片。
    - 其他序列类型无法保证原类型，回退为 list。

    示例：
    - slice_and_reverse([0,1,2,3,4], 1, 4) -> [3,2,1]
    - slice_and_reverse((0,1,2,3,4), 1, 4) -> (3,2,1)
    """
    raise NotImplementedError
