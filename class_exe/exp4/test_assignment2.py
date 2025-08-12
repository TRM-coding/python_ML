# test_assignment.py
# -*- coding: utf-8 -*-

import builtins
import assignment2 as assignment
# import assignment2_ans as assignment


class InputMock:
    def __init__(self, replies):
        self._replies = list(replies)
        self.calls = []
    def __call__(self, prompt=""):
        self.calls.append(prompt)
        assert self._replies, "没有更多的模拟输入"
        return self._replies.pop(0)


def test_chained_compare_stats(monkeypatch):
    # a=3, b=4 -> 3<4<=12 True
    # c=5 -> 25>=7 True
    im = InputMock(["3 4 5"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.chained_compare_stats() == (True, True)


def test_update_with_compound(monkeypatch):
    # a=10, b=3 -> a**=2=100 -> //=3=33 -> +=3=36 -> %=(6)=0
    im = InputMock(["10 3"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.update_with_compound() == 0


def test_div_identity_check(monkeypatch):
    im = InputMock(["7 3"])
    monkeypatch.setattr(builtins, "input", im)
    q, r, ok = assignment.div_identity_check()
    assert (q, r) == (2, 1)
    assert ok is True

    im = InputMock(["-7 3"])
    monkeypatch.setattr(builtins, "input", im)
    q, r, ok = assignment.div_identity_check()
    assert (q, r) == (-3, 2)
    assert ok is True


def test_square_vs_mul(monkeypatch):
    im = InputMock(["-11"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.square_vs_mul() is True


# def test_identity_equality_tuples():
#     eq, same12, same13 = assignment.identity_equality_tuples()
#     assert eq is True        # (1,2) == (1,2)
#     assert same12 is False   # 不同对象
#     assert same13 is True    # 同一对象引用


def test_shift_roundtrip():
    y, ok = assignment.shift_roundtrip(7, 5)
    assert ok is True
    assert isinstance(y, int)


def test_int_float_identity_equal(monkeypatch):
    im = InputMock(["3 3.0"])
    monkeypatch.setattr(builtins, "input", im)
    eq, same = assignment.int_float_identity_equal()
    assert eq is True
    assert same is False  # 不同类型对象，身份必不同


def test_max_min_arith():
    mx, mn = assignment.max_min_arith(10, -2)
    assert (mx, mn) == (10, -2)
    mx, mn = assignment.max_min_arith(-5, -9)
    assert (mx, mn) == (-5, -9)


def test_compound_chain():
    # a=5,b=3,c=8 -> a=8; b=24; c//= (8%3+1)=3 -> 2
    assert assignment.compound_chain(5, 3, 8) == (8, 24, 2)


def test_sorted_three_check(monkeypatch):
    im = InputMock(["1 2 2"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.sorted_three_check() == (True, True, False)

    im = InputMock(["3 2 1"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.sorted_three_check() == (False, False, False)
