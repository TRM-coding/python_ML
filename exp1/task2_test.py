"""task2 测试：元组基础操作。支持 --impl 切换实现。"""
import pytest
from conftest import import_task


@pytest.fixture(scope="module")
def impl(request):
	which = request.config.getoption("--impl")
	return import_task("task2", which)


def test_make_tuple(impl):
	assert impl.make_tuple(1, 2, 3) == (1, 2, 3)
	assert impl.make_tuple("a", None, True) == ("a", None, True)


def test_tuple_length(impl):
	assert impl.tuple_length(()) == 0
	assert impl.tuple_length((1, 2)) == 2


def test_get_first_last(impl):
	assert impl.get_first_last((1,)) == (1, 1)
	assert impl.get_first_last((1, 2, 3)) == (1, 3)


@pytest.mark.parametrize(
	"items,start,end,step,expected",
	[
		((0, 1, 2, 3, 4, 5), 1, 5, None, (1, 2, 3, 4)),
		((0, 1, 2, 3, 4, 5), 0, 6, 2, (0, 2, 4)),
		((0, 1, 2, 3, 4, 5), 5, 1, -2, (5, 3)),
	],
)
def test_slice_middle(impl, items, start, end, step, expected):
	assert impl.slice_middle(items, start, end, step) == expected


def test_concatenate_tuples(impl):
	assert impl.concatenate_tuples((1, 2), (3, 4)) == (1, 2, 3, 4)
	assert impl.concatenate_tuples([], []) == ()


def test_repeat_tuple(impl):
	assert impl.repeat_tuple((1, 2), 3) == (1, 2, 1, 2, 1, 2)
	assert impl.repeat_tuple([], 5) == ()


def test_to_tuple_and_count(impl):
	items = [1, 2, 2, 3, 2]
	t = impl.to_tuple(items)
	assert isinstance(t, tuple)
	assert impl.count_value(items, 2) == 3


def test_find_index(impl):
	items = ("a", "b", "c", "b", "a")
	assert impl.find_index(items, "b") == 1
	assert impl.find_index(items, "b", 2) == 3
	assert impl.find_index(items, "a", 1, 5) == 4


def test_swap_first_last(impl):
	assert impl.swap_first_last((1, 2)) == (2, 1)
	assert impl.swap_first_last((1, 2, 3, 4)) == (4, 2, 3, 1)

