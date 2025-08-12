# main.py
# -*- coding: utf-8 -*-

import utils_ans as utils

# 1) 两圆面积之和
def sum_two_circles_area(r1, r2):
    return utils.add(utils.circle_area(r1), utils.circle_area(r2))

# 2) 矩形与圆面积差（矩形面积 - 圆面积）
def rectangle_circle_area_diff(w, h, r):
    return utils.sub(utils.rectangle_area(w, h), utils.circle_area(r))

# 3) 圆柱体体积（底面半径 r，高 h）
def cylinder_volume(r, h):
    return utils.mul(utils.circle_area(r), h)

# 4) 圆扇形面积（半径 r，圆心角（度）deg）
def sector_area(r, deg):
    return utils.mul(utils.circle_area(r), utils.truediv(deg, 360))

# 5) 等差数列求和（n 项，首项 a1，末项 an）
def arithmetic_sum(n, a1, an):
    return utils.truediv(utils.mul(utils.add(a1, an), n), 2)

# 6) 平均速度（两段路程与时间）
def average_speed(dist1, time1, dist2, time2):
    return utils.truediv(utils.add(dist1, dist2), utils.add(time1, time2))

# 7) 圆环面积（外半径 R，内半径 r）
def annulus_area(R, r):
    return utils.sub(utils.circle_area(R), utils.circle_area(r))

# 8) 将角度（度）转换为弧度
def degrees_to_radians(deg):
    return utils.deg2rad(deg)

# 9) 角度转弧度后求弧长（半径 r，角度 deg）
def arc_length_by_degree(r, deg):
    return utils.mul(r, utils.deg2rad(deg))

# 10) 公式组合：((a+b)^2 - (a-b)^2) / (a*b)
def complex_formula(a, b):
    s1 = utils.add(a, b)
    s2 = utils.sub(a, b)
    num = utils.sub(utils.power(s1, 2), utils.power(s2, 2))
    den = utils.mul(a, b)
    return utils.truediv(num, den)
