"""exp2/task2 测试：复杂 if 嵌套（无循环）。"""
import pytest
from conftest import import_task


@pytest.fixture(scope="module")
def impl(request):
    return import_task("task2", request.config.getoption("--impl"))


def test_parse_age(impl):
    assert impl.parse_age("18") == 18
    assert impl.parse_age("") is None
    assert impl.parse_age("abc") is None


def test_classify_user(impl):
    assert impl.classify_user("17", "y") == "minor"
    assert impl.classify_user("18", "y") == "adult-member"
    assert impl.classify_user("20", "no") == "adult-nonmember"
    assert impl.classify_user("", "y") == "invalid"


def test_compare_numbers(impl):
    assert impl.compare_numbers("1", "2") == "<"
    assert impl.compare_numbers("2", "2") == "="
    assert impl.compare_numbers("3", "2") == ">"
    assert impl.compare_numbers("a", "2") == "invalid"


def test_choose_operation(impl):
    assert impl.choose_operation("+", 1, 2) == 3
    assert impl.choose_operation("-", 1, 2) == -1
    assert impl.choose_operation("*", 3, 2) == 6
    assert impl.choose_operation("/", 3, 2) == 1.5
    assert impl.choose_operation("/", 3, 0) is None
    assert impl.choose_operation("?", 1, 2) is None
