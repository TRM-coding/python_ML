# test_assignment.py
# -*- coding: utf-8 -*-

import assignment
# import assignment_ans as assignment


def test_int_to_float():
    assert assignment.int_to_float(5) == 5.0
    assert isinstance(assignment.int_to_float(5), float)


def test_float_to_int():
    assert assignment.float_to_int(3.9) == 3
    assert isinstance(assignment.float_to_int(3.9), int)


def test_str_to_int():
    assert assignment.str_to_int("42") == 42
    assert isinstance(assignment.str_to_int("42"), int)


def test_str_to_float():
    assert assignment.str_to_float("3.14") == 3.14
    assert isinstance(assignment.str_to_float("3.14"), float)


def test_int_to_str():
    assert assignment.int_to_str(99) == "99"
    assert isinstance(assignment.int_to_str(99), str)


def test_float_to_str():
    assert assignment.float_to_str(2.5) == "2.5"
    assert isinstance(assignment.float_to_str(2.5), str)


def test_bool_to_int():
    assert assignment.bool_to_int(True) == 1
    assert assignment.bool_to_int(False) == 0
    assert isinstance(assignment.bool_to_int(True), int)


def test_bool_to_float():
    assert assignment.bool_to_float(True) == 1.0
    assert assignment.bool_to_float(False) == 0.0
    assert isinstance(assignment.bool_to_float(False), float)


def test_int_to_bool():
    assert assignment.int_to_bool(3) is True
    assert assignment.int_to_bool(0) is False
    assert isinstance(assignment.int_to_bool(1), bool)


def test_str_to_bool():
    assert assignment.str_to_bool("") is False
    assert assignment.str_to_bool("abc") is True
    assert isinstance(assignment.str_to_bool("abc"), bool)


def test_mixed_to_str():
    assert assignment.mixed_to_str(3, 4.5) == "3 4.5"
    assert assignment.mixed_to_str(True, 10) == "True 10"
