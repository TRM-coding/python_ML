"""exp3/task1 测试：综合练习（覆盖讲义范围；无循环）。"""
import pytest
from conftest import import_task


@pytest.fixture(scope="module")
def impl(request):
    return import_task("task1", request.config.getoption("--impl"))


def test_normalize_score(impl):
    assert impl.normalize_score("0") == 0
    assert impl.normalize_score("100") == 100
    assert impl.normalize_score(" 99 ") == 99
    assert impl.normalize_score("101") is None
    assert impl.normalize_score("-1") is None
    assert impl.normalize_score("abc") is None


def test_summary_tuple(impl):
    age_text, score_text = impl.summary_tuple("Tom", "20", "88")
    assert age_text == "20" and score_text == "88"
    age_text2, score_text2 = impl.summary_tuple("Tom", "-1", "88")
    assert age_text2 == "invalid" and score_text2 == "88"
    age_text3, score_text3 = impl.summary_tuple("Tom", "20", "101")
    assert age_text3 == "20" and score_text3 == "invalid"


def test_pick_container(impl):
    assert impl.pick_container("list", 1, 2) == [1, 2]
    assert impl.pick_container("tuple", 1, 2) == (1, 2)
    assert impl.pick_container("set", 1, 2) == {1, 2}
    assert impl.pick_container("dict", 1, 2) == {"a": 1, "b": 2}


def test_merge_mapping(impl):
    a = {"x": 1, "k": 0}
    b = {"x": 9, "y": 2}
    assert impl.merge_mapping(a, b, prefer="b") == {"x": 9, "k": 0, "y": 2}
    assert impl.merge_mapping(a, b, prefer="a") == {"x": 1, "k": 0, "y": 2}


def test_slice_and_reverse(impl):
    assert impl.slice_and_reverse([0, 1, 2, 3, 4], 1, 4) == [3, 2, 1]
    assert impl.slice_and_reverse((0, 1, 2, 3, 4), 1, 4) == (3, 2, 1)
