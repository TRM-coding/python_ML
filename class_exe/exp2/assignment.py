# assignment.py
# -*- coding: utf-8 -*-

"""
要求：
- 按照每个函数中的 TODO 实现功能
- 返回读取到/处理后的结果（print 题通常返回 None）
"""

# ---------- 输入类练习 ----------

def read_string_no_prompt():
    # TODO:
    # 1) 不带任何参数调用 input()
    # 2) 将读取到的原始字符串返回
    return ?


def read_string_with_prompt():
    # TODO:
    # 1) 使用 input("请输入姓名: ") 读取一行字符串
    # 2) 返回读取到的字符串
    return ?


def read_int_with_prompt():
    # TODO:
    # 1) 使用 input("请输入整数: ") 读取字符串
    # 2) 将其转换为 int 后返回
    return ?


def read_float_with_prompt():
    # TODO:
    # 1) 使用 input("请输入小数: ") 读取字符串
    # 2) 将其转换为 float 后返回
    return ?


def read_two_ints_space_separated():
    # TODO:
    # 1) 使用 input("请输入两个整数(以空格分隔): ") 读取一行，如 "3 5"
    # 2) 拆分得到两个数字，转换为 int
    # 3) 以 (a, b) 的元组形式返回
    return ?


def read_three_lines_int_float_str():
    # TODO:
    # 1) 连续读取三行：
    #    第1行：整数
    #    第2行：小数
    #    第3行：字符串（原样返回，不 strip）
    # 2) 分别转换后返回 (i, f, s)
    return ?


# ---------- 输出类练习 ----------

def print_default(a, b):
    # TODO:
    # 1) 使用 print(a, b)（默认 sep=' ', end='\n'）
    # 2) 函数返回 None
    return ?





def print_with_end_no_newline(text):
    # TODO:
    # 1) 打印 text，设置 end=""（不换行）
    # 2) 函数返回 None
    return ?



def print_multiple_calls(a, b, c):
    # TODO:
    # 1) 依次调用三次 print：
    #    第一次打印 a，末尾不换行（end=","）
    #    第二次打印 b，末尾不换行（end=","）
    #    第三次打印 c（使用默认 end）
    # 2) 函数返回 None
    return ?
