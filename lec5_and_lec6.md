# Python 循环语法速览与练习

## 1. 基本语法

### 1.1 `for` 遍历

```python
for x in iterable:
    # 使用 x
```

- 适用于：列表、元组、字典、集合、字符串、生成器等可迭代对象。
- 常用配套：`range`、`enumerate`、`zip`。

### 1.2 `range`

```python
range(stop)             # 0..stop-1
range(start, stop)      # start..stop-1
range(start, stop, step)# 支持负步长
```

### 1.3 `while` 条件循环

```python
while condition:
    # 循环体
    # 注意更新状态，避免死循环
```

### 1.4 `break / continue / pass`

```python
for x in xs:
    if bad(x):
        break      # 立即退出本层循环
    if skip(x):
        continue   # 跳过本次，继续下次
    pass           # 占位，不做事
```

### 1.5 `for … else` / `while … else`

- 当循环**未触发 `break`** 正常结束时，执行 `else`。

```python
for x in xs:
    if x == target:
        print("found")
        break
else:
    print("not found")
```

### 1.6 `enumerate` 获取索引

```python
for i, v in enumerate(xs, start=0):
    ...
```

### 1.7 `zip` 并行遍历

```python
for a, b in zip(xs, ys):   # 以最短序列为准
    ...
```

### 1.8 字典与集合迭代

```python
for k in d:            # 等价于 d.keys()
for k, v in d.items():
for v in d.values():

for s in my_set:       # 集合遍历无固定顺序
    ...
```

### 1.9 常见模式

- 聚合：`sum/len/min/max/any/all` 或手写累加器
- 搜索：配合 `break` 与 `for-else`
- 状态机：记录上一个元素或当前状态

------

## 2. 与常用数据结构的结合

### 2.1 列表（构造、变换、过滤）

```python
# 变换
src = [1, -2, 3]
dst = []
for x in src:
    dst.append(abs(x))

# 过滤
evens = []
for x in src:
    if x % 2 == 0:
        evens.append(x)
```

等价的推导式：

```python
dst   = [abs(x) for x in src]
evens = [x for x in src if x % 2 == 0]
```

### 2.2 字典（计数、映射）

```python
s = "banana"
cnt = {}
for ch in s:
    cnt[ch] = cnt.get(ch, 0) + 1

# 键值变换
d = {"a":1, "b":2}
d2 = {}
for k, v in d.items():
    d2[k.upper()] = v * 10
```

推导式：

```python
cnt2 = {ch: s.count(ch) for ch in set(s)}  # 注意：count 内部有循环，整体是多次扫描，但无嵌套写法
d2   = {k.upper(): v*10 for k, v in d.items()}
```

### 2.3 集合（去重、成员测试 O(1) 均摊）

```python
xs = [1,2,2,3,1]
seen = set()
dedup = []
for x in xs:
    if x not in seen:
        seen.add(x)
        dedup.append(x)
```

### 2.4 字符串（遍历与构造）

```python
s = "AbcD"
upper_only = []
for ch in s:
    if ch.isupper():
        upper_only.append(ch)
result = "".join(upper_only)
```

### 2.5 `map`/`filter` 对比

```python
# map：函数映射
list(map(str.strip, [" a ", " b "]))   # ['a','b']

# filter：布尔过滤
list(filter(lambda x: x%2==0, [1,2,3,4]))  # [2,4]

# 与循环等价，性能差异可忽略，代码可读性按团队规范选
```

### 2.6 生成器表达式 + 聚合

```python
total_abs = sum(abs(x) for x in xs)
all_ok    = all(x >= 0 for x in xs)
any_neg   = any(x < 0 for x in xs)
```

### 2.7 修改列表的注意点

- 遍历时不要原地删除元素，容易跳项。可遍历拷贝或倒序删除，或新建结果列表。

------

## 3. 练习题（15 题，无嵌套循环）

> 要求：每题至多使用一个循环层级，可用内置函数与条件判断。

1. 计算 `1..n` 的平方和。输入 `n`，输出和。
2. 用 `while` 计算 `n!`（`n>=0`），`0! = 1`。
3. 统计列表中偶数的个数。
4. 在列表中查找目标值的**首个索引**。若不存在输出 `-1`。要求使用 `for-else`。
5. 将字符串中所有元音字母的数量分别统计到字典，如 `{'a':x,'e':y,'i':z,'o':u,'u':v}`。
6. 构造**前缀最大值**列表：输入 `[a1,a2,...,an]`，输出 `[max(a1), max(a1,a2), ..., max(a1..an)]`。
7. 找出列表的最小值与其索引（若有多处，取首个）。
8. 判断列表是否**严格递增**，是则输出 `True` 否则 `False`。
9. 对字符串执行**游程压缩**：将 `"aaabbc"` 转为 `[('a',3),('b',2),('c',1)]`（仅一层循环，比较相邻字符）。
10. 计算一批分数的**平均值**，保留两位小数；空列表输出 `0.00`。
11. 统计列表中元素出现次数，输出字典（键为元素，值为次数）
12. 实现简易 `map`：对整数列表应用函数 `f(x)=x*x+1`，返回新列表。