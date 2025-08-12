# test_main.py
# -*- coding: utf-8 -*-

import utils
# import utils_ans as utils
import main
# import main_ans as main

def approx_eq(a, b, eps=1e-6):
    return abs(a - b) < eps

def test_sum_two_circles_area():
    assert approx_eq(main.sum_two_circles_area(1, 2),
                     utils.circle_area(1) + utils.circle_area(2))

def test_rectangle_circle_area_diff():
    assert approx_eq(main.rectangle_circle_area_diff(3, 4, 2),
                     utils.rectangle_area(3, 4) - utils.circle_area(2))

def test_cylinder_volume():
    assert approx_eq(main.cylinder_volume(2, 5),
                     utils.circle_area(2) * 5)

def test_sector_area():
    assert approx_eq(main.sector_area(3, 90),
                     utils.circle_area(3) * (90 / 360))

def test_arithmetic_sum():
    assert approx_eq(main.arithmetic_sum(5, 2, 10),
                     (2 + 10) * 5 / 2)

def test_average_speed():
    assert approx_eq(main.average_speed(100, 2, 150, 3),
                     (100 + 150) / (2 + 3))

def test_annulus_area():
    assert approx_eq(main.annulus_area(5, 3),
                     utils.circle_area(5) - utils.circle_area(3))

def test_degrees_to_radians():
    assert approx_eq(main.degrees_to_radians(180),
                     utils.deg2rad(180))

def test_arc_length_by_degree():
    assert approx_eq(main.arc_length_by_degree(5, 180),
                     5 * utils.deg2rad(180))

def test_complex_formula():
    a, b = 5, 3
    assert approx_eq(main.complex_formula(a, b),
                     ((a+b)**2 - (a-b)**2) / (a*b))
