# assignment.py
# -*- coding: utf-8 -*-

"""
综合提升：输入/输出 + 算术/赋值 + 比较（含 is / is not）
答案版
"""

# 1) 链式比较与算术关系（输入）
def chained_compare_stats():
    a_str, b_str, c_str = input().split()
    a, b, c = int(a_str), int(b_str), int(c_str)
    cond1 = a < b <= a * b
    cond2 = c ** 2 >= a + b
    return (cond1, cond2)


# 2) 复合赋值序列（输入）
def update_with_compound():
    a_str, b_str = input().split()
    a, b = int(a_str), int(b_str)
    a **= 2
    a //= b
    a += b
    a %= (b * 2)
    return a


# 3) 地板除与还原校验（输入）
def div_identity_check():
    n_str, d_str = input().split()
    n, d = int(n_str), int(d_str)
    q = n // d
    r = n % d
    return (q, r, q * d + r == n)


# 4) 幂与乘积一致性（输入）
def square_vs_mul():
    x = int(input())
    return x ** 2 == x * x


# # 5) 等值 vs 同一对象（仅用元组，不用列表）
# def identity_equality_tuples():
#     t1 = (1, 2)
#     t2 = (1, 2)
#     t3 = t1
#     return (t1 == t2, t1 is t2, t1 is t3)


# 6) 位移往返（参数）
def shift_roundtrip(x: int, n: int):
    y = x
    y <<= n
    y >>= n
    return (y, y == x)


# 7) int 与 float 的等值与同一对象（输入）
def int_float_identity_equal():
    i_str, f_str = input().split()
    i, f = int(i_str), float(f_str)
    return (i == f, i is f)


# 8) 无分支求两数最大/最小（参数）
def max_min_arith(a: int, b: int):
    mx = (a + b + abs(a - b)) // 2
    mn = (a + b - abs(a - b)) // 2
    return (mx, mn)


# 9) 复合赋值链（参数）
def compound_chain(a: int, b: int, c: int):
    a += b
    b *= c
    c //= (a % 3 + 1)
    return (a, b, c)


# 10) 三数有序性检查（输入）
def sorted_three_check():
    a_str, b_str, c_str = input().split()
    a, b, c = int(a_str), int(b_str), int(c_str)
    return (a <= b <= c, a < b, b < c)
