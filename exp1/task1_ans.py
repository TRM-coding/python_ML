"""
task1 答案：列表基础操作，不使用 if 与循环。
"""
from typing import Any, Iterable, List, Sequence, Tuple


def make_list(a: Any, b: Any, c: Any) -> List[Any]:
	return [a, b, c]


def list_length(items: Sequence[Any]) -> int:
	return len(items)


def get_first_last(items: Sequence[Any]) -> Tuple[Any, Any]:
	return items[0], items[-1]


def slice_middle(items: Sequence[Any], start: int, end: int, step: int | None = None) -> List[Any]:
	return list(items[start:end] if step is None else items[start:end:step])


def concatenate_lists(a: Iterable[Any], b: Iterable[Any]) -> List[Any]:
	return list(a) + list(b)


def repeat_list(items: Iterable[Any], times: int) -> List[Any]:
	return list(items) * times


def copy_list_slice(items: Iterable[Any]) -> List[Any]:
	lst = list(items)
	return lst[:]


def copy_list_list(items: Iterable[Any]) -> List[Any]:
	return list(items)


def replace_slice(items: Iterable[Any], start: int, end: int, replacement: Iterable[Any]) -> List[Any]:
	lst = list(items)
	lst[start:end] = list(replacement)
	return lst


def insert_at(items: Iterable[Any], index: int, value: Any) -> List[Any]:
	lst = list(items)
	lst[index:index] = [value]
	return lst


def remove_value(items: Iterable[Any], value: Any) -> List[Any]:
	lst = list(items)
	# 使用切片和拼接模拟 remove 的效果（避免循环）
	i = lst.index(value)
	return lst[:i] + lst[i + 1 :]


def pop_at(items: Iterable[Any], index: int = -1) -> Tuple[List[Any], Any]:
	lst = list(items)
	# 支持负索引
	idx = index if index >= 0 else len(lst) + index
	popped = lst[idx]
	new_list = lst[:idx] + lst[idx + 1 :]
	return new_list, popped


def count_value(items: Iterable[Any], value: Any) -> int:
	return list(items).count(value)


def find_index(items: Sequence[Any], value: Any, start: int = 0, end: int | None = None) -> int:
	stop = len(items) if end is None else end
	return items.index(value, start, stop)


def reverse_list(items: Iterable[Any]) -> List[Any]:
	lst = list(items)
	return lst[::-1]


def sort_list(items: Iterable[Any], reverse: bool = False) -> List[Any]:
	return sorted(list(items), reverse=reverse)

