"""
task2 答案：元组基础操作。
"""
from typing import Any, Iterable, Sequence, Tuple


def make_tuple(a: Any, b: Any, c: Any) -> Tuple[Any, Any, Any]:
	return (a, b, c)


def tuple_length(items: Sequence[Any]) -> int:
	return len(items)


def get_first_last(items: Sequence[Any]) -> Tuple[Any, Any]:
	return items[0], items[-1]


def slice_middle(items: Sequence[Any], start: int, end: int, step: int | None = None) -> Tuple[Any, ...]:
	return tuple(items[start:end] if step is None else items[start:end:step])


def concatenate_tuples(a: Iterable[Any], b: Iterable[Any]) -> Tuple[Any, ...]:
	return tuple(a) + tuple(b)


def repeat_tuple(items: Iterable[Any], times: int) -> Tuple[Any, ...]:
	return tuple(items) * times


def to_tuple(items: Iterable[Any]) -> Tuple[Any, ...]:
	return tuple(items)


def count_value(items: Iterable[Any], value: Any) -> int:
	return tuple(items).count(value)


def find_index(items: Sequence[Any], value: Any, start: int = 0, end: int | None = None) -> int:
	stop = len(items) if end is None else end
	return items.index(value, start, stop)


def swap_first_last(items: Sequence[Any]) -> Tuple[Any, ...]:
	# 长度>=2
	return (items[-1],) + tuple(items[1:-1]) + (items[0],)

