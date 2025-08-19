"""
task3 答案：字典基础操作。
"""
from typing import Any, Dict, Iterable, Mapping, Tuple


def make_dict(a_key: Any, a_val: Any, b_key: Any, b_val: Any) -> Dict[Any, Any]:
	return {a_key: a_val, b_key: b_val}


def dict_length(d: Mapping[Any, Any]) -> int:
	return len(d)


def get_with_default(d: Mapping[Any, Any], key: Any, default: Any) -> Any:
	return d.get(key, default)


def set_key(d: Mapping[Any, Any], key: Any, value: Any) -> Dict[Any, Any]:
	newd = dict(d)
	newd[key] = value
	return newd


def merge_dicts(a: Mapping[Any, Any], b: Mapping[Any, Any]) -> Dict[Any, Any]:
	return {**dict(a), **dict(b)}


def pop_key(d: Mapping[Any, Any], key: Any) -> Tuple[Dict[Any, Any], Any]:
	newd = dict(d)
	val = newd.pop(key)
	return newd, val


def keys_values(d: Mapping[Any, Any]) -> Tuple[Tuple[Any, ...], Tuple[Any, ...]]:
	return tuple(d.keys()), tuple(d.values())


def invert_simple(d: Mapping[Any, Any]) -> Dict[Any, Any]:
	# 不使用循环：利用 keys 与 values 的对应顺序，通过 zip 解包
	k = tuple(d.keys())
	v = tuple(d.values())
	return dict(zip(v, k))


def update_with(d: Mapping[Any, Any], updates: Mapping[Any, Any]) -> Dict[Any, Any]:
	return {**dict(d), **dict(updates)}

