"""task4 测试：集合基础操作。支持 --impl 切换实现。"""
import pytest
from conftest import import_task


@pytest.fixture(scope="module")
def impl(request):
	which = request.config.getoption("--impl")
	return import_task("task4", which)


def test_make_and_len(impl):
	s = impl.make_set(1, 2, 2, 3)
	assert s == {1, 2, 3}
	assert impl.set_length([1, 1, 2]) == 2


def test_add_and_remove(impl):
	assert impl.add_value({1, 2}, 3) == {1, 2, 3}
	assert impl.remove_value({1, 2, 3}, 2) == {1, 3}


def test_operations(impl):
	a, b = {1, 2, 3}, {3, 4}
	assert impl.union(a, b) == {1, 2, 3, 4}
	assert impl.intersection(a, b) == {3}
	assert impl.difference(a, b) == {1, 2}
	assert impl.symmetric_difference(a, b) == {1, 2, 4}


def test_subset_superset(impl):
	a, b = {1, 2}, {1, 2, 3}
	assert impl.is_subset(a, b) is True
	assert impl.is_superset(b, a) is True


def test_to_frozenset(impl):
	fs = impl.to_frozenset([1, 2, 2])
	assert isinstance(fs, frozenset)
	assert fs == frozenset({1, 2})

