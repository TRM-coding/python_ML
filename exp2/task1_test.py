"""exp2/task1 测试：基本 if 语句。支持 --impl 切换实现。"""
import pytest
from conftest import import_task


@pytest.fixture(scope="module")
def impl(request):
    return import_task("task1", request.config.getoption("--impl"))


def test_is_adult(impl):
    assert impl.is_adult(18) is True
    assert impl.is_adult(17) is False


def test_grade_from_score(impl):
    assert impl.grade_from_score(95) == "A"
    assert impl.grade_from_score(83) == "B"
    assert impl.grade_from_score(72) == "C"
    assert impl.grade_from_score(60) == "D"
    assert impl.grade_from_score(10) == "F"


def test_classify_number(impl):
    assert impl.classify_number(1) == "positive"
    assert impl.classify_number(-0.1) == "negative"
    assert impl.classify_number(0.0) == "zero"


def test_valid_percent(impl):
    for p in (0, 50, 100):
        assert impl.valid_percent(p) is True
    for p in (-1, 101):
        assert impl.valid_percent(p) is False


def test_safe_div(impl):
    assert impl.safe_div(10, 2) == 5
    assert impl.safe_div(1, 0) is None


def test_truthy_text(impl):
    assert impl.truthy_text("hello") == "YES"
    assert impl.truthy_text(0) == "NO"
