[TOC]

## 入门：python re模块

1. 创建正则表达式对象：re.complie

   将正则表达式得样式编译为一个正则对象（re.Pattern），这样同一个模式做多次匹配

2. 利用正则对象进行匹配

   正则对象拥有的[方法](https://docs.python.org/zh-cn/3.7/library/re.html?highlight=findall#re-objects)包括：match、search、find等

3. 匹配结果类型为匹配对象（re.Match）

   匹配对象拥有的[方法](https://docs.python.org/zh-cn/3.7/library/re.html?highlight=findall#match-objects)包括：expand、grouop、start、span等

4. 如果只是少量使用正则，那么可以不用编译正则对象并缓存，直接使用re模块提供的[类似接口](https://docs.python.org/zh-cn/3.7/library/re.html?highlight=findall#re.search)：

- ```python
  patternObj = re.compile(pattern)
  marchObj = patternObj.match(rawString)
  #等价于
  result = re.match(pattern, string)
  ```

  常用方法：

  - re.search：扫描整个字符串并返回第一个成功的匹配，否则返回None。
  - re.match：只尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，就返回none。

  - re.findall：在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
  - re.finditer：和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

  

  - re.sub：用于替换字符串中的匹配项
  - re.split：按照能够匹配的子串将字符串分割后返回列表。

  [常用标志位](https://docs.python.org/zh-cn/3.7/library/re.html#re.A)（先眼熟，用到时再强化记忆）

  **注意**

  - 模式和给定字串可以是Unicode字符串（str），也可以是8位字节串（byte），但是两者在匹配时不能混用，另外在做字符串替换时也要类型相同。
  - 如果要匹配反斜杠(`“\”`)，那正则模式必须写成 `"\\\\”`。因为正则表达式里匹配一个反斜杠必须是 `“\\”` ，而每个反斜杠在普通的 Python 字符串里都要写成 `“\\"` 。另外，正则也可以这么写： `r"\n"` 。在带有 `'r'` 前缀的字符串字面值中，反斜杠不必做任何特殊处理。 
  - 正则表达式可以拼接。 如果 *A* 和 *B* 都是正则表达式， 那么 *AB* 也是正则表达式。通常， 如果字符串 *p* 匹配 *A* 并且另一个字符串 *q* 匹配 *B*, 那么 *pq* 可以匹配 AB。除非 *A* 或者 *B* 包含低优先级操作、*A* 和 *B* 存在边界条件，或者有命名组引用。

虽然re模块的API都是封装正则对象的，但是了解正则对象有利于我们理解api内部做了什么。

**更详细**：

1. [re模块说明](https://docs.python.org/zh-cn/3.7/library/re.html)
2. [re How Tos](https://docs.python.org/zh-cn/3.7/howto/regex.html#regex-howto)

## Pattern对象

### 使用Flag配置

pattern对象都可以设置flag，这个flag是RegexFlag类型的，用来配置匹配注意点，例如：re.A只匹配ascii。

### 使用compile

编译正则表达式为正则对象并返回。

```
re.compile(sPattern[, iFlag])
->re._compile(sPattern, flags)
```

### 使用search

扫描整个 *string* 寻找第一个匹配的位置， 并返回一个相应的matchObj。这里需要区分无匹配和0长度匹配。如果 *rx* 是一个编译后的正则对象， `rx.search(string, 0, 50)` 等价于 `rx.search(string[:50], 0)`。

```python
re.search(sPattern, string[, iFlag])
-> re._compile(sPattern, flags).search(string)
-> sre.sre_compile.compile(sPattern, flags).search(string)
```

源码中其实是将编译正则对象的过程封装起来了。使用re.search时，不能传入已经编译好的pattern对象。

### 使用match

## Match对象

直接输出matchObj，可以查看一些匹配数据。

```python
>>> result = re.match(r"(?P<first_name>\w+——\w+) (?P<last_name>\w+)", "Malc——olm Reynolds 胡同华人 dwr")
>>> print(result)
<re.Match object; span=(0, 18), match='Malc——olm Reynolds'>
```

输出结果中，span表示匹配范围，match表示完全匹配结果

### 使用group

正则匹配到的结果通过Match对象返回，group相关API可以像列表一样去获取结果。

```python
>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
>>> m.group('first_name')  #只返回'first_name'匹配到的内容  = m.group(1)
'Malcolm'
>>> m.group('last_name') #只返回'last_name'匹配到的内容 = m.group(2)
'Reynolds'
>>> m.group()  # 默认返回完全匹配 = m.group(0)
'Malcolm Reynolds'
>>> m.groups()  # 返回匹配列表
('Malcolm', 'Reynolds')
```

`(?P<first_name>re)`:  给re起一个组名，方便引用