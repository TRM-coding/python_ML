"""
列表（list）基础练习。

规则：保持简单，不使用 if 语句和循环语句。优先使用列表的切片、拼接、重复（*）、
以及常见的内置方法来完成题目。

实现这些函数以通过测试。不要修改函数签名。
"""

from typing import Any, Iterable, List, Sequence, Tuple



def make_list(a: Any, b: Any, c: Any) -> List[Any]:
	"""由三个值组成并返回一个列表。"""
	raise NotImplementedError


def list_length(items: Sequence[Any]) -> int:
	"""返回列表的长度。"""
	raise NotImplementedError


def get_first_last(items: Sequence[Any]) -> Tuple[Any, Any]:
	"""返回 (第一个元素, 最后一个元素) 的二元组。

	注意：测试会保证传入的序列非空。
	"""
	raise NotImplementedError


def slice_middle(items: Sequence[Any], start: int, end: int, step: int | None = None) -> List[Any]:
	"""返回一个切片结果的列表。

	当 step 为 None 时，等价于 items[start:end]；否则等价于 items[start:end:step]。
	"""
	raise NotImplementedError


def concatenate_lists(a: Iterable[Any], b: Iterable[Any]) -> List[Any]:
	"""将两个可迭代对象转为列表后拼接并返回新列表。"""
	raise NotImplementedError


def repeat_list(items: Iterable[Any], times: int) -> List[Any]:
	"""使用 * 运算符将序列重复 times 次后返回列表。"""
	raise NotImplementedError


def copy_list_slice(items: Iterable[Any]) -> List[Any]:
	"""使用切片返回一个浅拷贝。"""
	raise NotImplementedError


def copy_list_list(items: Iterable[Any]) -> List[Any]:
	"""使用 list() 返回一个浅拷贝。"""
	raise NotImplementedError


def replace_slice(items: Iterable[Any], start: int, end: int, replacement: Iterable[Any]) -> List[Any]:
	"""用 replacement 替换切片 items[start:end]，返回新列表（不修改入参）。"""
	raise NotImplementedError


def insert_at(items: Iterable[Any], index: int, value: Any) -> List[Any]:
	"""在给定索引处插入一个元素并返回新列表。"""
	raise NotImplementedError


def remove_value(items: Iterable[Any], value: Any) -> List[Any]:
	"""删除第一次出现的 value 并返回新列表。"""
	raise NotImplementedError


def pop_at(items: Iterable[Any], index: int = -1) -> Tuple[List[Any], Any]:
	"""弹出给定索引处的值并返回 (新列表, 被弹出的值)。"""
	raise NotImplementedError


def count_value(items: Iterable[Any], value: Any) -> int:
	"""返回 value 在列表中的出现次数。"""
	raise NotImplementedError


def find_index(items: Sequence[Any], value: Any, start: int = 0, end: int | None = None) -> int:
	"""返回 value 在区间 [start, end) 内第一次出现的索引。end 为 None 时表示到末尾。"""
	raise NotImplementedError


def reverse_list(items: Iterable[Any]) -> List[Any]:
	"""使用切片返回一个倒序的新列表。"""
	raise NotImplementedError


def sort_list(items: Iterable[Any], reverse: bool = False) -> List[Any]:
	"""返回排序后的新列表，可通过 reverse 指定倒序。"""
	raise NotImplementedError

