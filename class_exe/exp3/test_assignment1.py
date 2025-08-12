# test_assignment.py
# -*- coding: utf-8 -*-

import assignment1 as assignment

# import assignment1_ans as assignment

def test_add():
    assert assignment.add(7, 3) == 10
    assert assignment.add(-2, 5) == 3


def test_subtract():
    assert assignment.subtract(7, 3) == 4
    assert assignment.subtract(3, 7) == -4


def test_multiply():
    assert assignment.multiply(7, 3) == 21
    assert assignment.multiply(-2, 4) == -8


def test_true_divide():
    assert assignment.true_divide(7, 3) == 7 / 3
    assert isinstance(assignment.true_divide(7, 3), float)


def test_floor_divide():
    assert assignment.floor_divide(7, 3) == 2
    assert assignment.floor_divide(-7, 3) == -3  # 向下取整


def test_modulo():
    assert assignment.modulo(7, 3) == 1
    assert assignment.modulo(-7, 3) == 2  # Python: 余数符号与被除数相同


def test_power():
    assert assignment.power(7, 3) == 343
    assert assignment.power(2, 4) == 16


def test_negate():
    assert assignment.negate(7) == -7
    assert assignment.negate(-3) == 3


def test_positive():
    assert assignment.positive(7) == 7
    assert assignment.positive(-3) == -3


def test_absolute():
    assert assignment.absolute(-7) == 7
    assert assignment.absolute(7) == 7


def test_divmod_pair():
    assert assignment.divmod_pair(7, 3) == (2, 1)
    assert assignment.divmod_pair(-7, 3) == (-3, 2)
