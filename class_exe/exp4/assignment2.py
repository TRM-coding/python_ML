# assignment.py
# -*- coding: utf-8 -*-

"""
说明：
- 按每题 TODO 完成；除特别说明外，返回题述要求的结果。
- 允许使用：input/print、算术运算、divmod、abs、所有复合赋值、比较与身份比较（is / is not）。
"""

# 1) 链式比较与算术关系（输入）
def chained_compare_stats():
    # TODO:
    # 1) 从一行读取三个整数 a b c（空格分隔）
    # 2) 计算并返回一个二元组 (cond1, cond2)：
    #    cond1: a < b <= a * b
    #    cond2: c ** 2 >= a + b
    return ?


# 2) 复合赋值序列（输入）
def update_with_compound():
    # TODO:
    # 1) 从一行读取两个整数 a b（空格分隔）
    # 2) 按顺序对 a 执行：
    #    a **= 2
    #    a //= b
    #    a += b
    #    a %= (b * 2)
    # 3) 返回更新后的 a
    return ?


# 3) 整除与还原校验（输入）
def div_identity_check():
    # TODO:
    # 1) 读取两个整数 n d（空格分隔，保证 d != 0）
    # 2) 计算 q = n // d 与 r = n % d
    # 3) 返回 (q, r, q * d + r == n)
    return ?


# 4) 幂与乘积一致性（输入）
def square_vs_mul():
    # TODO:
    # 1) 读取一个整数 x
    # 2) 返回一个布尔值，判断 x ** 2 是否等于 x * x
    return ?


# # 5) 等值 vs 同一对象（仅用元组，不用列表）
# def identity_equality_tuples():
#     # TODO:
#     # 1) 内部创建 t1 = (1, 2)，t2 = (1, 2)，t3 = t1
#     # 2) 返回三元组：
#     #    (t1 == t2, t1 is t2, t1 is t3)
#     return ?


# 6) 位移往返（参数）
def shift_roundtrip(x: int, n: int):
    # TODO:
    # 1) 复制一份 y = x
    # 2) 对 y 执行左移复合赋值 y <<= n
    # 3) 再对 y 右移复合赋值 y >>= n
    # 4) 返回 (y, y == x)
    return ?


# 7) int 与 float 的等值与同一对象（输入）
def int_float_identity_equal():
    # TODO:
    # 1) 从一行读取 i 和 f（空格分隔），i 按 int 读，f 按 float 读
    # 2) 返回 (i == f, i is f)
    return ?


# 8) 无分支,不使用库函数求两数最大/最小（参数）
def max_min_arith(a: int, b: int):
    # TODO:
    # 1) 使用算术与 abs()（不使用比较与条件），返回 (max_val, min_val)
    #    提示：max = (a + b + abs(a - b)) // 2
    #          min = (a + b - abs(a - b)) // 2
    return ?


# 9) 复合赋值链（参数）
def compound_chain(a: int, b: int, c: int):
    # TODO:
    # 1) 按顺序进行以下操作（均为原地复合赋值）：
    #    a += b
    #    b *= c
    #    c //= (a % 3 + 1)   # 注意括号
    # 2) 返回三元组 (a, b, c)
    return ?


# 10) 三数有序性检查（输入）
def sorted_three_check():
    # TODO:
    # 1) 输入三个整数 a b c（空格分隔）
    # 2) 返回三元组：(a <= b <= c, a < b, b < c)
    return ?
