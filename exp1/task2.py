"""
元组（tuple）基础练习。

规则：不使用 if 语句和循环，优先使用切片、拼接、重复（*）以及内置方法。
实现这些函数以通过测试。
"""
from typing import Any, Iterable, Sequence, Tuple


def make_tuple(a: Any, b: Any, c: Any) -> Tuple[Any, Any, Any]:
	"""由三个值组成并返回一个元组。"""
	raise NotImplementedError


def tuple_length(items: Sequence[Any]) -> int:
	"""返回序列的长度。"""
	raise NotImplementedError


def get_first_last(items: Sequence[Any]) -> Tuple[Any, Any]:
	"""返回 (第一个元素, 最后一个元素)。测试会保证非空。"""
	raise NotImplementedError


def slice_middle(items: Sequence[Any], start: int, end: int, step: int | None = None) -> Tuple[Any, ...]:
	"""返回切片结果的元组。step 为 None 时等价于 items[start:end]。"""
	raise NotImplementedError


def concatenate_tuples(a: Iterable[Any], b: Iterable[Any]) -> Tuple[Any, ...]:
	"""将两个可迭代对象转为元组后拼接并返回新元组。"""
	raise NotImplementedError


def repeat_tuple(items: Iterable[Any], times: int) -> Tuple[Any, ...]:
	"""使用 * 运算符将序列重复 times 次后返回元组。"""
	raise NotImplementedError


def to_tuple(items: Iterable[Any]) -> Tuple[Any, ...]:
	"""将可迭代对象转换为元组。"""
	raise NotImplementedError


def count_value(items: Iterable[Any], value: Any) -> int:
	"""统计 value 在序列中的出现次数。"""
	raise NotImplementedError


def find_index(items: Sequence[Any], value: Any, start: int = 0, end: int | None = None) -> int:
	"""返回 value 在区间 [start, end) 内第一次出现的索引。end 为 None 表示到末尾。"""
	raise NotImplementedError


def swap_first_last(items: Sequence[Any]) -> Tuple[Any, ...]:
	"""交换首尾元素并返回新元组。测试会保证长度 >= 2。"""
	raise NotImplementedError

