"""
字典（map/dict）基础练习。

规则：不使用 if 语句和循环，优先使用字典字面量、解包、get、keys/values/items、
copy、update、pop、setdefault 等基础方法与操作。
实现这些函数以通过测试。
"""
from typing import Any, Dict, Iterable, Mapping, Tuple


def make_dict(a_key: Any, a_val: Any, b_key: Any, b_val: Any) -> Dict[Any, Any]:
	"""根据两个键值对构造并返回字典。"""
	raise NotImplementedError


def dict_length(d: Mapping[Any, Any]) -> int:
	"""返回字典的键数量。"""
	raise NotImplementedError


def get_with_default(d: Mapping[Any, Any], key: Any, default: Any) -> Any:
	"""等价于 d.get(key, default)。"""
	raise NotImplementedError


def set_key(d: Mapping[Any, Any], key: Any, value: Any) -> Dict[Any, Any]:
	"""返回一个新字典，等于 d 的浅拷贝，并设置/覆盖 key 的值。"""
	raise NotImplementedError


def merge_dicts(a: Mapping[Any, Any], b: Mapping[Any, Any]) -> Dict[Any, Any]:
	"""返回合并后的新字典，b 中键覆盖 a。"""
	raise NotImplementedError


def pop_key(d: Mapping[Any, Any], key: Any) -> Tuple[Dict[Any, Any], Any]:
	"""弹出指定键并返回 (新字典, 被弹出的值)。假设 key 一定存在。"""
	raise NotImplementedError


def keys_values(d: Mapping[Any, Any]) -> Tuple[Tuple[Any, ...], Tuple[Any, ...]]:
	"""返回 (keys_tuple, values_tuple)。顺序遵循迭代顺序。"""
	raise NotImplementedError


def invert_simple(d: Mapping[Any, Any]) -> Dict[Any, Any]:
	"""键值互换（假设值唯一且可作键）。不使用循环，使用 items 的解包技巧。"""
	raise NotImplementedError


def update_with(d: Mapping[Any, Any], updates: Mapping[Any, Any]) -> Dict[Any, Any]:
	"""返回应用 updates 后的新字典。"""
	raise NotImplementedError

