# utils.py
# -*- coding: utf-8 -*-

PI = 3.14159

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def truediv(a, b):
    return a / b  # 浮点除法

def floordiv(a, b):
    return a // b

def mod(a, b):
    return a % b

def power(a, b):
    return a ** b

def circle_area(r):
    return PI * r * r

def circle_circumference(r):
    return 2 * PI * r

def rectangle_area(w, h):
    return w * h

def deg2rad(deg):
    return deg * PI / 180
