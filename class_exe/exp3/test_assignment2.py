# test_assignment.py
# -*- coding: utf-8 -*-

import assignment2 as assignment
# import assignment2_ans as assignment


def test_assign_value():
    assert assignment.assign_value() == 5


def test_add_and_assign():
    assert assignment.add_and_assign(7, 3) == 10


def test_subtract_and_assign():
    assert assignment.subtract_and_assign(7, 3) == 4


def test_multiply_and_assign():
    assert assignment.multiply_and_assign(7, 3) == 21


def test_divide_and_assign():
    out = assignment.divide_and_assign(7, 3)
    assert isinstance(out, float)
    assert abs(out - (7 / 3)) < 1e-9


def test_floor_divide_and_assign():
    assert assignment.floor_divide_and_assign(7, 3) == 2
    assert assignment.floor_divide_and_assign(-7, 3) == -3


def test_modulo_and_assign():
    assert assignment.modulo_and_assign(7, 3) == 1
    assert assignment.modulo_and_assign(-7, 3) == 2


def test_power_and_assign():
    assert assignment.power_and_assign(7, 3) == 343
    assert assignment.power_and_assign(2, 4) == 16


def test_bitwise_and_assign():
    assert assignment.bitwise_and_assign(7, 3) == (7 & 3)


def test_bitwise_or_assign():
    assert assignment.bitwise_or_assign(7, 3) == (7 | 3)


def test_bitwise_xor_assign():
    assert assignment.bitwise_xor_assign(7, 3) == (7 ^ 3)


def test_left_shift_and_assign():
    assert assignment.left_shift_and_assign(7, 1) == (7 << 1)


def test_right_shift_and_assign():
    assert assignment.right_shift_and_assign(7, 1) == (7 >> 1)
