# test_assignment.py
# -*- coding: utf-8 -*-

import builtins
import assignment1 as assignment
# import assignment1_ans as assignment

class InputMock:
    def __init__(self, replies):
        self._replies = list(replies)
        self.calls = []
    def __call__(self, prompt=""):
        self.calls.append(prompt)
        assert self._replies, "没有更多的模拟输入"
        return self._replies.pop(0)

# ---------------- 测试 ----------------

def test_sum_two_ints(monkeypatch):
    im = InputMock(["3 5"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.sum_two_ints() == 8

def test_area_of_rectangle(monkeypatch):
    im = InputMock(["3.5 2.0"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.area_of_rectangle() == 7.0

def test_circle_circumference(monkeypatch):
    im = InputMock(["2.0"])
    monkeypatch.setattr(builtins, "input", im)
    assert abs(assignment.circle_circumference() - (2 * 3.14159 * 2.0)) < 1e-6

def test_average_of_three(monkeypatch):
    im = InputMock(["3 4 5"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.average_of_three() == 4.0

def test_fahrenheit_to_celsius(monkeypatch):
    im = InputMock(["212"])
    monkeypatch.setattr(builtins, "input", im)
    assert abs(assignment.fahrenheit_to_celsius() - 100.0) < 1e-6

def test_simple_interest(monkeypatch):
    im = InputMock(["1000 5 2"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.simple_interest() == 100.0

def test_greet_user(monkeypatch, capsys):
    im = InputMock(["Alice"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.greet_user() is None
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"

def test_divmod_example(monkeypatch):
    im = InputMock(["7 3"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.divmod_example() == (2, 1)

def test_power_of_number(monkeypatch):
    im = InputMock(["2 4"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.power_of_number() == 16

def test_format_print_example(monkeypatch, capsys):
    im = InputMock(["foo bar"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.format_print_example() is None
    captured = capsys.readouterr()
    assert captured.out == "foo - bar\n"
