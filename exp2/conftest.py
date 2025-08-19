"""
pytest 配置：提供 --impl 选项以选择导入学生版（默认）或答案版实现。
"""
from __future__ import annotations

from pathlib import Path
from types import ModuleType
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


def _load(module_name: str, file_path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(module_name, str(file_path))
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)  # type: ignore[attr-defined]
    return mod


def import_task(task: str, impl: str = "student") -> ModuleType:
    base = Path(__file__).parent
    name = f"{task}_ans.py" if impl == "ans" else f"{task}.py"
    return _load(f"exp2.{task}.{impl}", base / name)


__all__ = ["import_task"]
