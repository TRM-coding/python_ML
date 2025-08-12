# utils.py
# -*- coding: utf-8 -*-

PI = 3.14159

def add(a: int | float, b: int | float):
    return a + b

def mul(a: int | float, b: int | float):
    return a * b

def circle_area(r: float):
    return PI * r * r

def greet(name: str):
    return f"Hello, {name}!"
