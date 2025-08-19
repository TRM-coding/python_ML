"""task3 测试：字典基础操作。支持 --impl 切换实现。"""
import pytest
from conftest import import_task


@pytest.fixture(scope="module")
def impl(request):
	which = request.config.getoption("--impl")
	return import_task("task3", which)


def test_make_and_len(impl):
	d = impl.make_dict("a", 1, "b", 2)
	assert d == {"a": 1, "b": 2}
	assert impl.dict_length(d) == 2


def test_get_with_default(impl):
	d = {"a": 1}
	assert impl.get_with_default(d, "a", 9) == 1
	assert impl.get_with_default(d, "x", 9) == 9


def test_set_key(impl):
	d = {"a": 1}
	d2 = impl.set_key(d, "b", 2)
	assert d2 == {"a": 1, "b": 2} and d == {"a": 1}


def test_merge_dicts(impl):
	a = {"a": 1, "x": 0}
	b = {"b": 2, "x": 9}
	assert impl.merge_dicts(a, b) == {"a": 1, "x": 9, "b": 2}


def test_pop_key(impl):
	newd, v = impl.pop_key({"a": 1, "b": 2}, "a")
	assert (newd, v) == ({"b": 2}, 1)


def test_keys_values(impl):
	d = {"a": 1, "b": 2}
	k, v = impl.keys_values(d)
	assert k == ("a", "b") and v == (1, 2)


def test_invert_simple(impl):
	d = {"a": 1, "b": 2}
	assert impl.invert_simple(d) == {1: "a", 2: "b"}


def test_update_with(impl):
	d = {"a": 1}
	u = {"b": 2, "a": 9}
	assert impl.update_with(d, u) == {"a": 9, "b": 2}

