"""task1 测试：列表基础操作。

使用 pytest 参数 --impl=student|ans 来切换被测实现。
"""
import pytest
from conftest import import_task


@pytest.fixture(scope="module")
def impl(request):
	which = request.config.getoption("--impl")
	mod = import_task("task1", which)
	return mod


def test_make_list(impl):
	assert impl.make_list(1, 2, 3) == [1, 2, 3]
	assert impl.make_list("a", None, True) == ["a", None, True]


def test_list_length(impl):
	assert impl.list_length([]) == 0
	assert impl.list_length([1, 2, 3]) == 3


def test_get_first_last(impl):
	assert impl.get_first_last([1]) == (1, 1)
	assert impl.get_first_last([1, 2, 3, 4]) == (1, 4)


@pytest.mark.parametrize(
	"items,start,end,step,expected",
	[
		([0, 1, 2, 3, 4, 5], 1, 5, None, [1, 2, 3, 4]),
		([0, 1, 2, 3, 4, 5], 0, 6, 2, [0, 2, 4]),
		([0, 1, 2, 3, 4, 5], 5, 1, -2, [5, 3]),
	],
)
def test_slice_middle(impl, items, start, end, step, expected):
	assert impl.slice_middle(items, start, end, step) == expected


def test_concatenate_lists(impl):
	assert impl.concatenate_lists([1, 2], (3, 4)) == [1, 2, 3, 4]
	assert impl.concatenate_lists([], []) == []


def test_repeat_list(impl):
	assert impl.repeat_list([1, 2], 3) == [1, 2, 1, 2, 1, 2]
	assert impl.repeat_list([], 5) == []


def test_copy(impl):
	src = [1, [2], 3]
	a = impl.copy_list_slice(src)
	b = impl.copy_list_list(src)
	assert a == src and b == src and a is not src and b is not src


def test_replace_slice(impl):
	assert impl.replace_slice([1, 2, 3, 4], 1, 3, [9, 9]) == [1, 9, 9, 4]
	assert impl.replace_slice([1, 2, 3, 4], 0, 0, [7]) == [7, 1, 2, 3, 4]


def test_insert_at(impl):
	assert impl.insert_at([1, 2, 3], 1, 99) == [1, 99, 2, 3]
	assert impl.insert_at([1, 2, 3], 0, 0) == [0, 1, 2, 3]


def test_remove_value(impl):
	assert impl.remove_value([1, 2, 2, 3], 2) == [1, 2, 3]


def test_pop_at(impl):
	new_list, v = impl.pop_at([10, 20, 30], 1)
	assert (new_list, v) == ([10, 30], 20)
	new_list2, v2 = impl.pop_at([10, 20, 30])
	assert (new_list2, v2) == ([10, 20], 30)


def test_count_value(impl):
	assert impl.count_value([1, 2, 2, 3, 2], 2) == 3
	assert impl.count_value([], 5) == 0


def test_find_index(impl):
	items = ["a", "b", "c", "b", "a"]
	assert impl.find_index(items, "b") == 1
	assert impl.find_index(items, "b", 2) == 3
	assert impl.find_index(items, "a", 1, 5) == 4


def test_reverse_list(impl):
	assert impl.reverse_list([1, 2, 3]) == [3, 2, 1]


def test_sort_list(impl):
	assert impl.sort_list([3, 1, 2]) == [1, 2, 3]
	assert impl.sort_list([3, 1, 2], reverse=True) == [3, 2, 1]

