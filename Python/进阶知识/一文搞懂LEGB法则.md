## 什么是LEGB法则

LEGB是**Local, Enclosing, Global, and Built-in**的缩写，表示几种不同的作用域，对应不同的级别，越往后作用范围越大。通过LEGB法则来有序的查找名字，避免重名等带来的问题。

## 区分作用域和命名空间

python编译运行后将名字（可以是变量名，类名，包名等）和内存上所指对象以字典的形式保存起来的，这字典被称为名字空间。我们可以通过在模块中执行**moduleName.\__dict\___**查看本模块名字空间中的所有名字。

```
>>> import sys
>>> sys.__dict__.keys()
dict_keys(['__name__', '__doc__', '__package__',..., 'argv', 'ps1', 'ps2'])
```

与此同时，名字空间按照不同的不同的创建时机被区分为 内置名字空间、模块名字空间、局部名字空间。内置名字空间在python解释器启动时创建；全局名字空间在模块创建时创建；局部名字空间在函数创建时创建。

而作用域则决定了我们在程序中能否直接通过名字空间中的名字直接访问到内存上对应对象。作用域按照LEGB法则被分为四类：函数作用域、嵌套作用域、模块作用域、内置作用域。

## LEBG的查找过程

从嵌套作用域起，通过首先检查局部作用域或最内层函数的局部作用域来解析名字。然后，Python会查看从最内层作用域到最外层作用域的外部函数的所有封闭作用域。如果找不到匹配项，则Python将查看全局作用域和内置作用域。如果找不到名字，则会出现错误。

### 获取名字的方法

- 局部作用域

  ```
  def  square():
      result = base ** 2
      print(f'The square of {base} is: {result}')
      
  >>> square.__code__.co_varnames  #查看局部名字空间包含的名字
  ('base', 'result')
  >>> square.__code__.co_argcount  #获取参数数量
  ```

- 模块作用域：**moduleName.\__dict\___**
- 全局作用域: **dir()**

### Tips

> 修改全局名字通常被认为是不好的编程习惯，因为它可能导致代码如下：
>
> - **调试困难：程序中**几乎所有语句都可以更改全局名字的值。
> - **难以理解：**您需要了解所有访问和修改全局名字的语句。
> - **不可能重用：**该代码取决于特定于特定程序的全局名字。
>
> 良好的编程习惯建议使用本地名字而不是全局名字。这里有一些提示：
>
> - **编写**依赖于本地名字而不是全局名字的独立功能。
> - 无论您处于什么范围，**都应尝试**使用唯一的对象名字。
> - **避免**在整个程序中修改全局名字。
> - **避免**跨模块名字修改。
> - **使用**全局名字作为在程序执行期间不会更改的常量。

## 修改不同作用域的对象

py3提供了两个关键字：global, nonlocal

- global将修饰的名字指向全局名字空间中对应的名字；

- nonlocal将修饰的名字指向局部名字空间中对应的名字；

以上两种都不会在当前名字空间中创建新名字。

```python
>>>a = 11
>>>def square(base):
...    global a
...    result = base ** 2
...    print(f'The square of {base} is: {result}')
>>>print(square.__code__.co_varnames)
# 结果：
('base', 'result')
```

注意：

可以更新global修饰的名字对象，nonlocal修饰的对象也可以被嵌套函数更改，但是如果嵌套函数中用到了外部函数的名字对象但是没有用nonlocal修饰它，那它只能被调用不能被修改。

## 通过import将名字导入作用域

```python
>>> dir()
['__annotations__', '__builtins__',..., '__spec__']
>>> import sys
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'sys']
>>> import os
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'os', 'sys']
>>> from functools import partial
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'os', 'partial', 'sys']
```

