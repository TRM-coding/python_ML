# test_main.py
# -*- coding: utf-8 -*-

import importlib
import types

def test_import_and_calls():
    # 动态导入，确保按要求从 main 走到 utils
    main = importlib.import_module("main")
    # main = importlib.import_module("main_ans")

    # 和 utils 分别取值，避免学生在 main 里硬编码
    utils = importlib.import_module("utils")

    # 1) 加法
    assert main.compute_sum(3, 5) == utils.add(3, 5)
    assert main.compute_sum(-2, 1.5) == utils.add(-2, 1.5)

    # 2) 乘法
    assert main.compute_product(4, 6) == utils.mul(4, 6)
    assert main.compute_product(2.5, 2) == utils.mul(2.5, 2)

    # 3) 圆面积
    assert abs(main.circle_area_from_main(2.0) - utils.circle_area(2.0)) < 1e-9

    # 4) 问候
    assert main.hello("Alice") == utils.greet("Alice")

    # 5) 常量 PI
    assert main.constants_pi() == utils.PI
    assert isinstance(main.constants_pi(), float)


def test_import_style_flexibility():
    """
    不强制导入风格；只要 main 能调用 utils 的接口并通过测试即可。
    这里仅检查 main 模块存在所需可调用对象。
    """
    import main
    # import main_ans as main
    for name in ("compute_sum", "compute_product", "circle_area_from_main", "hello", "constants_pi"):
        assert hasattr(main, name)
        assert callable(getattr(main, name))
