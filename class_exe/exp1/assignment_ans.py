# assignment.py
# -*- coding: utf-8 -*-

"""
练习主题：Python 基本类型的显式类型转换
涵盖：int, float, str, bool
要求：完成 TODO 中的步骤，使用 Python 内置的类型转换函数
"""

def int_to_float(x: int):
    # 将整数 x 转换为 float 类型并返回
    return float(x)


def float_to_int(x: float):
    # 将浮点数 x 转换为 int 类型并返回
    return int(x)


def str_to_int(s: str):
    # 将字符串 s 转换为 int 类型并返回
    return int(s)


def str_to_float(s: str):
    # 将字符串 s 转换为 float 类型并返回
    return float(s)


def int_to_str(x: int):
    # 将整数 x 转换为 str 类型并返回
    return str(x)


def float_to_str(x: float):
    # 将浮点数 x 转换为 str 类型并返回
    return str(x)


def bool_to_int(flag: bool):
    # 将布尔值 flag 转换为 int 类型并返回
    return int(flag)


def bool_to_float(flag: bool):
    # 将布尔值 flag 转换为 float 类型并返回
    return float(flag)


def int_to_bool(x: int):
    # 将整数 x 转换为 bool 类型并返回
    return bool(x)


def str_to_bool(s: str):
    # 将字符串 s 转换为 bool 类型并返回
    return bool(s)


def mixed_to_str(a, b):
    """
    - 将 a 和 b 都转换为字符串
    - 用空格拼接成一个字符串并返回
    例：a=3, b=4.5 -> "3 4.5"
    """
    return str(a) + " " + str(b)
