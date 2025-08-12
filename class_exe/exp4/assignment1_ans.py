# assignment.py
# -*- coding: utf-8 -*-

"""
参考答案
"""

def sum_two_ints():
    a_str, b_str = input().split()
    a, b = int(a_str), int(b_str)
    return a + b


def area_of_rectangle():
    w_str, h_str = input().split()
    w, h = float(w_str), float(h_str)
    return w * h


def circle_circumference():
    r = float(input())
    PI = 3.14159
    return 2 * PI * r


def average_of_three():
    a, b, c = map(int, input().split())
    return (a + b + c) / 3


def fahrenheit_to_celsius():
    f = float(input())
    return (f - 32) * 5 / 9


def simple_interest():
    principal_str, rate_str, years_str = input().split()
    principal = float(principal_str)
    rate = float(rate_str)
    years = float(years_str)
    return principal * (rate / 100) * years


def greet_user():
    name = input()
    print(f"Hello, {name}!")
    return None


def divmod_example():
    a, b = map(int, input().split())
    return divmod(a, b)


def power_of_number():
    base, exp = map(int, input().split())
    return base ** exp


def format_print_example():
    s1, s2 = input().split()
    print(s1, s2, sep=" - ")
    return None
