# Python 常用数据结构

------

## 0. 对比

| 类型       | 字面量          | 可变   | 是否有序                   | 元素可重复                 | 作为字典键           |
| ---------- | --------------- | ------ | -------------------------- | -------------------------- | -------------------- |
| list 列表  | `[ ]`           | 可变   | 有序                       | 可                         | 否                   |
| tuple 元组 | `( )`           | 不可变 | 有序                       | 可                         | 可（若内部全可哈希） |
| dict 字典  | `{k: v}`        | 可变   | 有序（Py3.7+保持插入顺序） | 键不可重复（后者覆盖前者） | —                    |
| set 集合   | `{ }` / `set()` | 可变   | 无序                       | 否（自动去重）             | —                    |

> 空集合请用 `set()`；`{}` 是空字典。

------

## 1) list 列表

### 创建与访问

```python
nums = [1, 2, 3]
xs = list("abc")       # ['a','b','c']
xs[0], xs[-1]           # 索引；-1 为最后一个
xs[1:3]                 # 切片（不含右端）
```

### 常用操作

```python
xs.append(4)            # 尾部追加 
xs.extend([5, 6])       # 连接
xs.insert(1, 99)        # 指定位置插入 
xs.pop()                # 弹尾部并返回 
xs.pop(1)               # 删除索引1 
xs.remove(99)           # 按值删首个匹配 
xs.clear()
```

### 排序与反转

```python
xs = [3,1,2]
xs.sort()               # 就地排序，返回 None
xs.sort(key=abs, reverse=True)
ys = sorted(xs)         # 生成新列表
xs.reverse()            # 就地反转
```

### 列表推导式

```python
squares = [i*i for i in range(5) if i%2==0]
```

### 切片与切片赋值

```python
xs = [0,1,2,3]
xs[1:3] = [10, 11, 12]  # 可改变长度
```

### 复制与乘法

```python
a = [[0]*3]*2           # 错误：两行指向同一子列表
b = [[0 for _ in range(3)] for _ in range(2)]  # 正确
```

`*` 复制的是**引用**。

```python
a = [[0]*3]*2
a[0] is a[1]          # True，同一对象
a[0][0] = 1
print(a)              # [[1, 0, 0], [1, 0, 0]]  两行一起变

row = [0]*3：创建一个新列表，元素是对同一个 int 0 的引用。int 不可变
```

------

## 2) tuple 元组

### 基本

```python
t = (1, 2, 3)
single = (1,)           # 单元素必须带逗号
empty = ()
```

- 不可变，有序。可作为字典键（内部元素必须可哈希）。

### 打包与解包

```python
a, b = 1, 2             # 解包赋值
x = (1, 2)
a, b = x
# 交换
a, b = b, a
```

------

## 3) dict 字典（map）

### 创建

```python
d = {"a":1, "b":2}
d = dict([("a",1), ("b",2)])
d = dict(a=1, b=2)
```

- 键必须可哈希：常见为 `str`、`int`、`tuple(不可变元素)`。

### 访问与更新

```python
d["a"]          # KeyError 若不存在
v = d.get("a", 0)   # 不存在返回默认值

d["c"] = 3          # 新增/更新

d.update({"a":10, "d":4})
d |= {"e":5}        # 3.9+ 合并
```

### 删除

```python
d.pop("a", None)     # 删除并返回键 "a" 对应的值；若不存在则返回 None，不报错
key, val = d.popitem()# 从字典中删除并返回一对键值，默认按后进先出（LIFO），即删除最后插入的那一对。字典为空时抛 KeyError
```

### 遍历

```python
for k in d: ...                    # 键
for k, v in d.items(): ...         # 键值
for v in d.values(): ...
"a" in d        # 仅查键
```

### 有序性

- Python3.7+ 规定保持**插入顺序**（语言保证）.

------

## 4) set 集合（去重）

### 创建与基本操作

```python
s = {1,2,3}
s = set([1,2,2,3])     # {1,2,3}

s.add(4)
s.update([3,5])
s.discard(10)          # 不存在不报错
# s.remove(10)         # 不存在会报错
s.pop()                 # 随机弹出一个元素
```

### 集合运算

```python
a, b = {1,2,3}, {3,4}
a | b      # 并集 {1,2,3,4}
a & b      # 交集 {3}
a - b      # 差集 {1,2}
a <= b     # 子集
```

```python
s = "banana"
#生成字符频次表
cnt = {ch: s.count(ch) for ch in set(s)}
```

### 易错点

- `{}` 是字典，空集合用 `set()`；元素必须可哈希。

------

## 5) 拷贝与共享引用

```python
import copy

# 浅拷贝：顶层复制，内部引用共享
l1 = [[1],[2]]
l2 = l1.copy()         # 或 l1[:] / list(l1)
l2[0].append(99)
# l1[0] 也会受影响

# 深拷贝：递归复制
l3 = copy.deepcopy(l1)
```

> 函数默认参数不要用可变对象：`def f(x, cache=None): cache = cache or {} ...`





------

## 6) 常见模式

### 6.1 去重并保持原顺序

```python
seen = set()
res = []
for x in [1,2,2,3,1]:
    if x not in seen:
        seen.add(x)
        res.append(x)
# res = [1,2,3]
```

### 6.2 计数

```python
from collections import Counter
Counter("banana")      # Counter({'a':3,'n':2,'b':1})
```





# if语句

------

## 1. 基本语法

```python
if 条件:
    代码块
```

- 条件为布尔结果（True/False）。
- 末尾必须有冒号 `:`。
- 代码块使用**缩进**表明从属关系。

示例：

```python
age = 20
if age >= 18:
    print("adult")
```

## 2. if / elif / else 结构

```python
if 条件1:
    ...
elif 条件2:
    ...
else:
    ...
```

- 先匹配到就执行，不再继续匹配。
- `elif` 可有多个；`else` 可省略。

示例：

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)
```

## 3. 缩进与代码块

- 推荐每级**4个空格**。
- 不要混用 Tab 与空格。
- 缩进不一致会报 `IndentationError`。

示例：

```python
n = 3
if n > 0:
    print("positive")      # 同一层级保持一致缩进
    print("done")
```

## 4. 布尔与“真值”

- 直接布尔：`True`, `False`。
- 能转成布尔的对象：非零数字、非空容器为真；0、空串、空列表、空字典、`None` 为假。

示例：

```python
if "hello":
    print("非空字符串为真")
if 0:
    print("不会执行")
```

常见“假”值：`False, None, 0, 0.0, 0j, "", [], {}, set(), range(0)`。

## 5. 比较与逻辑运算符

- 比较：`== != < <= > >=`
- 逻辑：`and`、`or`、`not`
- 链式比较：`18 <= age < 65`

示例：

```python
x = 10
if 1 < x <= 10 and not (x % 2):
    print("x在(1,10]且是偶数")
```

## 6. 多条件常用写法

**区间判断（链式比较）：**

```python
if 0 <= score <= 100:
    print("有效分数")
```

**成员判断：**

```python
op = input("选择运算(+ - * /): ")
if op in ["+", "-", "*", "/"]:
    print("合法运算符")
```

**任意/全部条件：**

```python
u, v, w = True, False, True
if any([u, v, w]):
    print("至少一个为真")
if all([u, w]):
    print("全部为真")
```

## 7. 嵌套与组合

```python
age = 25
is_member = True
if age >= 18:
    if is_member:
        price = 50
    else:
        price = 80
else:
    price = 30
print(price)
```

> 建议：能用 `elif` 或计算式合并时，就避免深层嵌套。

## 8. 条件表达式（三元运算）

```python
# 语法：A if 条件 else B
age = 20
status = "adult" if age >= 18 else "minor"
```

适合简单赋值场景，避免写成多行。

## 9. 输入与类型转换

`input()` 返回**字符串**。数值判断需先转型。

```python
raw = input("输入年龄: ")
if raw.isdigit():#字符串非空且全部是数字字符
    age = int(raw)
    if age >= 18:
        print("adult")
else:
    print("非法输入")
```

## 10. 常见错误与规避

1. `=` 与 `==` 混淆：

```python
# 错误： if x = 1:
# 正确：
if x == 1:
    ...
```

1. 漏写冒号 `:`。
2. 缩进不一致或混用 Tab/空格。
3. 用 `is` 比较数值或字符串：`is` 比身份，`==` 比值。

```python
# 不要这样： if x is 1:
# 应该：
if x == 1:
    ...
```

1. 把 `and/or` 写成按位运算 `&`/`|`：布尔逻辑应使用 `and/or`。
2. 浮点数直接相等比较：

```python
x = 0.1 + 0.2
if abs(x - 0.3) < 1e-9:
    print("近似相等")
```

1. 类型未统一比较：`"3" == 3` 为 `False`，先转换类型。

## 11. 典型模式

**守卫式返回（在函数中早退出）：**

```python
def safe_div(a, b):
    if b == 0:
        return None
    return a / b
```

## 14. 速查清单

- 结构：`if / elif / else`，末尾冒号。
- 缩进：每级4空格，禁用 Tab。
- 常用：链式比较、`in`、`any/all`、三元表达式。
- 避坑：`=` vs `==`；不要用 `is` 比值；避免浮点直接相等；逻辑用 `and/or`。