"""
集合（set）基础练习。

规则：不使用 if 语句和循环，优先使用字面量、集合方法（add/discard/remove/pop）、
集合运算（| & - ^）、issubset/issuperset、len 等。
实现这些函数以通过测试。
"""
from typing import Any, Iterable, FrozenSet, Set, Tuple


def make_set(*values: Any) -> Set[Any]:
	"""根据任意数量的位置参数创建并返回集合。"""
	raise NotImplementedError


def set_length(s: Iterable[Any]) -> int:
	"""返回集合中元素个数（先转为 set）。"""
	raise NotImplementedError


def add_value(s: Iterable[Any], value: Any) -> Set[Any]:
	"""返回新集合（不修改入参），包含原集合所有元素以及新的 value。"""
	raise NotImplementedError


def remove_value(s: Iterable[Any], value: Any) -> Set[Any]:
	"""返回新集合，移除一个元素（假设一定存在）。"""
	raise NotImplementedError


def union(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	"""并集。"""
	raise NotImplementedError


def intersection(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	"""交集。"""
	raise NotImplementedError


def difference(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	"""差集 a - b。"""
	raise NotImplementedError


def symmetric_difference(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	"""对称差集。"""
	raise NotImplementedError


def is_subset(a: Iterable[Any], b: Iterable[Any]) -> bool:
	"""a 是否是 b 的子集。"""
	raise NotImplementedError


def is_superset(a: Iterable[Any], b: Iterable[Any]) -> bool:
	"""a 是否是 b 的父集。"""
	raise NotImplementedError


def to_frozenset(values: Iterable[Any]) -> FrozenSet[Any]:
	"""转换为不可变集合。"""
	raise NotImplementedError

