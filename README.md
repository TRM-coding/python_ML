# Python 基础练习（exp1）

本仓库包含 list / tuple / dict(map) / set 的基础练习题、参考答案与 pytest 测试。

- 练习文件：`exp1/task1.py`、`exp1/task2.py`、`exp1/task3.py`、`exp1/task4.py`
- 答案文件：`exp1/task1_ans.py`、`exp1/task2_ans.py`、`exp1/task3_ans.py`、`exp1/task4_ans.py`
- 测试文件：`exp1/task1_test.py`、`exp1/task2_test.py`、`exp1/task3_test.py`、`exp1/task4_test.py`
- pytest 配置：`exp1/conftest.py`（提供 `--impl` 选项用于切换学生实现或答案实现）

## 环境准备

建议使用 Python 3.10+。若未安装 pytest，请先安装：

```bash
python -m pip install -U pytest
```

如果你在 VS Code 的虚拟环境中，请确保已激活对应环境再执行上面的命令。

## 运行测试

本项目的测试支持用命令行参数 `--impl` 选择被测实现：

- `--impl=student`：测试学生实现（默认），对应文件 `task*.py`
- `--impl=ans`：测试参考答案实现，对应文件 `task*_ans.py`

在项目根目录（`/root/Teach_Summer/class2`）下运行：

```bash
# 运行 exp1 下所有测试 - 默认学生实现
python -m pytest -q exp1

# 运行 exp1 下所有测试 - 使用答案实现
python -m pytest -q exp1 --impl=ans

# 只运行 task1 的测试（学生实现）
python -m pytest -q exp1/task1_test.py

# 只运行 task1 的测试（答案实现）
python -m pytest -q exp1/task1_test.py --impl=ans

# 只运行指定用例
python -m pytest -q exp1/task1_test.py::test_make_list --impl=ans
```

若出现 “unrecognized arguments: --impl=ans”，请确认 `exp1/conftest.py` 存在且未被改动；或直接在 issue/消息中告知我修复。

## 练习约束

题目刻意限制了控制流，要求不使用 `if` 与循环，重点练习以下基础操作：

- list：切片、拼接、重复（`*`）、浅拷贝、常用内置方法
- tuple：切片、拼接、重复（`*`）、索引/计数
- dict：字面量、解包合并、`get`/`pop`/`update`/`keys`/`values`/`items`
- set：字面量、集合运算（并/交/差/对称差）、`issubset`/`issuperset` 等

## VS Code 集成（可选）

让测试面板默认跑答案实现，可在工作区设置中加入：

```json
{
  "python.testing.pytestArgs": ["--impl=ans", "exp1"],
  "python.testing.pytestEnabled": true
}
```

也可改为 `student` 以验证练习代码。

## 目录结构

```
exp1/
  conftest.py
  task1.py          # list 练习（函数桩）
  task1_ans.py      # list 参考答案
  task1_test.py     # list 测试
  task2.py          # tuple 练习（函数桩）
  task2_ans.py      # tuple 参考答案
  task2_test.py     # tuple 测试
  task3.py          # dict(map) 练习（函数桩）
  task3_ans.py      # dict(map) 参考答案
  task3_test.py     # dict(map) 测试
  task4.py          # set 练习（函数桩）
  task4_ans.py      # set 参考答案
  task4_test.py     # set 测试
```

## 小贴士

- 测试严格按题目约束编写。若你使用了高阶语法但符合约束，通常也能通过。
- 若你希望新增练习题或更难的变体，告诉我你想练的点，我会补充对应的题与测试。
