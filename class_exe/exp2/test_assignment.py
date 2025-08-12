# test_assignment.py
# -*- coding: utf-8 -*-

import builtins
import assignment
# import assignment_ans as assignment


# ----------- 工具：模拟 input 与检测 prompt -----------

class InputMock:
    """按顺序返回预置的输入；若设置了 expected_prompts，则逐一校验传入的 prompt。"""
    def __init__(self, replies, expected_prompts=None):
        self._replies = list(replies)
        self._expected_prompts = list(expected_prompts) if expected_prompts else None
        self.calls = []

    def __call__(self, prompt=""):
        self.calls.append(prompt)
        if self._expected_prompts is not None:
            idx = len(self.calls) - 1
            assert idx < len(self._expected_prompts), "input 调用次数超出预期"
            assert prompt == self._expected_prompts[idx], f"期望的 prompt: {self._expected_prompts[idx]!r}, 实际: {prompt!r}"
        assert self._replies, "没有更多的模拟输入可用"
        return self._replies.pop(0)


# ---------------- 输入类测试 ----------------

def test_read_string_no_prompt(monkeypatch):
    im = InputMock(["hello"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.read_string_no_prompt() == "hello"
    assert im.calls == [""]


def test_read_string_with_prompt(monkeypatch):
    im = InputMock(["Alice"], expected_prompts=["请输入姓名: "])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.read_string_with_prompt() == "Alice"


def test_read_int_with_prompt(monkeypatch):
    im = InputMock(["123"], expected_prompts=["请输入整数: "])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.read_int_with_prompt() == 123


def test_read_float_with_prompt(monkeypatch):
    im = InputMock(["3.14"], expected_prompts=["请输入小数: "])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.read_float_with_prompt() == 3.14


def test_read_two_ints_space_separated(monkeypatch):
    im = InputMock(["7 8"], expected_prompts=["请输入两个整数(以空格分隔): "])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.read_two_ints_space_separated() == (7, 8)


def test_read_three_lines_int_float_str(monkeypatch):
    im = InputMock(["10", "2.5", "Raw String"])
    monkeypatch.setattr(builtins, "input", im)
    assert assignment.read_three_lines_int_float_str() == (10, 2.5, "Raw String")


# ---------------- 输出类测试 ----------------

def test_print_default(capsys):
    assignment.print_default("A", "B")
    captured = capsys.readouterr()
    assert captured.out == "A B\n"




def test_print_with_end_no_newline(capsys):
    assignment.print_with_end_no_newline("X")
    captured = capsys.readouterr()
    assert captured.out == "X"





def test_print_multiple_calls(capsys):
    assignment.print_multiple_calls("A", "B", "C")
    captured = capsys.readouterr()
    assert captured.out == "A,B,C\n"
