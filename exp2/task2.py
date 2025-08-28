"""
exp2/task2：复杂 if 嵌套（不使用循环与数据结构）。可结合输入输出与类型判断。
"""
from typing import Optional


def parse_age(raw: str) -> Optional[int]:
    """原始输入是字符串：纯数字串转为年龄（int），空或非数字返回 None。"""
    raise NotImplementedError


def classify_user(age_raw: str, member_raw: str) -> str:
    """
    基于两个输入字符串进行分类：
    - age_raw: 年龄字符串，见 parse_age 规则
    - member_raw: 'y'/'yes' 表示会员，否则视为非会员

    
    - age 无效 => 返回 'invalid'
    - age < 18 => 'minor'
    - 否则 成年：会员 => 'adult-member'，非会员 => 'adult-nonmember'
    """
    raise NotImplementedError


def compare_numbers(a_raw: str, b_raw: str) -> str:
    """比较两个数字字符串：任一无效返回 'invalid'；否则返回 '>'、'<' 或 '='。"""
    raise NotImplementedError


def choose_operation(op: str, x: float, y: float) -> Optional[float]:
    #op:"+" return x+y
    #op:"-" return x-y
    #op:"*" return x*y
    #op:"/" return x/y
    """
    根据 op 执行 + - * / 四则运算；非法 op 返回 None；除数为 0 时返回 None。
    """
    if op=="+":
        return x+y
    elif op =='-':
        return x-y
    elif op=='*':
        return x*y
    elif op=='/':
        return x/y
