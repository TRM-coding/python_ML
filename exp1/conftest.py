"""
pytest 配置：提供 --impl 选项以选择导入学生版（默认）或答案版实现。

使用方式：
- pytest                 # 默认测试学生实现（task*.py）
- pytest --impl=ans      # 测试答案实现（task*_ans.py）
"""
from __future__ import annotations

from pathlib import Path
from types import ModuleType
from typing import Iterable

import importlib.util
import sys


def pytest_addoption(parser):
    parser.addoption(
        "--impl",
        action="store",
        default="student",
        choices=["student", "ans"],
        help="选择被测试的实现：student 或 ans",
    )


def load_module_from_path(module_name: str, file_path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)  # type: ignore[assignment]
    return module


def resolve_module_path(base_dir: Path, task: str, impl: str) -> Path:
    """返回模块文件路径。impl 为 'ans' 则选 *_ans.py，否则选 *.py。"""
    if impl == "ans":
        name = f"{task}_ans.py"
    else:
        name = f"{task}.py"
    return base_dir / name


def import_task(task: str, impl: str = "student") -> ModuleType:
    base_dir = Path(__file__).parent
    path = resolve_module_path(base_dir, task, impl)
    return load_module_from_path(f"exp1.{task}.{impl}", path)


__all__ = ["import_task"]
