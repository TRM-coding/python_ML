"""
task4 答案：集合基础操作。
"""
from typing import Any, Iterable, FrozenSet, Set


def make_set(*values: Any) -> Set[Any]:
	return set(values)


def set_length(s: Iterable[Any]) -> int:
	return len(set(s))


def add_value(s: Iterable[Any], value: Any) -> Set[Any]:
	return set(s) | {value}


def remove_value(s: Iterable[Any], value: Any) -> Set[Any]:
	new_s = set(s)
	new_s.remove(value)  # 假设一定存在
	return new_s


def union(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) | set(b)


def intersection(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) & set(b)


def difference(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) - set(b)


def symmetric_difference(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) ^ set(b)


def is_subset(a: Iterable[Any], b: Iterable[Any]) -> bool:
	return set(a).issubset(set(b))


def is_superset(a: Iterable[Any], b: Iterable[Any]) -> bool:
	return set(a).issuperset(set(b))


def to_frozenset(values: Iterable[Any]) -> FrozenSet[Any]:
	return frozenset(values)

"""
task4 答案：集合基础操作。
"""
from typing import Any, Iterable, FrozenSet, Set, Tuple


def make_set(*values: Any) -> Set[Any]:
	return set(values)


def set_length(s: Iterable[Any]) -> int:
	return len(set(s))


def add_value(s: Iterable[Any], value: Any) -> Set[Any]:
	new = set(s)
	new |= {value}
	return new


def remove_value(s: Iterable[Any], value: Any) -> Set[Any]:
	new = set(s)
	# 假设一定存在
	new.remove(value)
	return new


def union(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) | set(b)


def intersection(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) & set(b)


def difference(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) - set(b)


def symmetric_difference(a: Iterable[Any], b: Iterable[Any]) -> Set[Any]:
	return set(a) ^ set(b)


def is_subset(a: Iterable[Any], b: Iterable[Any]) -> bool:
	return set(a).issubset(set(b))


def is_superset(a: Iterable[Any], b: Iterable[Any]) -> bool:
	return set(a).issuperset(set(b))


def to_frozenset(values: Iterable[Any]) -> FrozenSet[Any]:
	return frozenset(values)

