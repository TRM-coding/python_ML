# main.py
# -*- coding: utf-8 -*-

"""
目标：练习模块导入与调用。
参考答案版
"""

# 从 utils 模块导入需要用到的函数/常量
from utils import add, mul, circle_area, greet, PI


def compute_sum(a, b):
    """调用 utils 中的加法函数，返回 a+b 的结果"""
    return add(a, b)


def compute_product(a, b):
    """调用 utils 中的乘法函数，返回 a*b 的结果"""
    return mul(a, b)


def circle_area_from_main(r):
    """调用 utils 中的 circle_area，返回圆面积"""
    return circle_area(r)


def hello(name):
    """调用 utils 中的 greet，返回问候字符串"""
    return greet(name)


def constants_pi():
    """返回 utils 中定义的圆周率常量 PI"""
    return PI
