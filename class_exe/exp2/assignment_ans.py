# assignment_ans.py
# -*- coding: utf-8 -*-

"""
练习主题：标准输入输出（答案版）
覆盖：
- input：无提示、带提示，读取 str/int/float，多值拆分
- print：sep、end
"""

# ---------- 输入类练习 ----------

def read_string_no_prompt():
    # 不带任何参数调用 input()，返回原始字符串
    return input()


def read_string_with_prompt():
    # 使用指定提示读取字符串并返回
    return input("请输入姓名: ")


def read_int_with_prompt():
    # 使用指定提示读取字符串并转换为 int 返回
    return int(input("请输入整数: "))


def read_float_with_prompt():
    # 使用指定提示读取字符串并转换为 float 返回
    return float(input("请输入小数: "))


def read_two_ints_space_separated():
    # 读取一行，如 "3 5"，拆分并转为两个 int，以元组返回
    a_str, b_str = input("请输入两个整数(以空格分隔): ").split()
    return int(a_str), int(b_str)


def read_three_lines_int_float_str():
    # 连续读取三行：整数、小数、字符串（原样返回）
    i = int(input())
    f = float(input())
    s = input()
    return i, f, s


# ---------- 输出类练习 ----------

def print_default(a, b):
    # 使用默认参数打印（sep=' '，end='\n'）
    print(a, b)
    return None



def print_with_end_no_newline(text):
    # 打印后不换行
    print(text, end="")
    return None


def print_multiple_calls(a, b, c):
    # 依次打印 a、b（不换行，用逗号作结尾），最后打印 c（默认换行）
    print(a, end=",")
    print(b, end=",")
    print(c)
    return None
