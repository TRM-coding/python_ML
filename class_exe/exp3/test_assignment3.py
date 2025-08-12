# test_assignment.py
# -*- coding: utf-8 -*-

import assignment3 as assignment
# import assignment3_ans as assignment


def test_is_equal():
    assert assignment.is_equal(7, 3) is False
    assert assignment.is_equal(5, 5) is True


def test_is_not_equal():
    assert assignment.is_not_equal(7, 3) is True
    assert assignment.is_not_equal(5, 5) is False


def test_is_greater():
    assert assignment.is_greater(7, 3) is True
    assert assignment.is_greater(3, 7) is False


def test_is_less():
    assert assignment.is_less(7, 3) is False
    assert assignment.is_less(3, 7) is True


def test_is_greater_equal():
    assert assignment.is_greater_equal(7, 3) is True
    assert assignment.is_greater_equal(3, 3) is True
    assert assignment.is_greater_equal(2, 3) is False


def test_is_less_equal():
    assert assignment.is_less_equal(7, 3) is False
    assert assignment.is_less_equal(3, 3) is True
    assert assignment.is_less_equal(2, 3) is True


def test_is_same_object():
    a = [1, 2]
    b = a
    c = [1, 2]
    assert assignment.is_same_object(a, b) is True
    assert assignment.is_same_object(a, c) is False


def test_is_not_same_object():
    a = [1, 2]
    b = a
    c = [1, 2]
    assert assignment.is_not_same_object(a, b) is False
    assert assignment.is_not_same_object(a, c) is True
