- 合并两个字典到新字典

  ```
  >>> x = {'a': 1, 'b': 2}
  >>> y = {'b': 3, 'c': 4}
  
  >>> z = {**x, **y}
  
  >>> z
  {'c': 4, 'a': 1, 'b': 3}
  
  # In Python 2.x you could
  # use this:
  >>> z = dict(x, **y)
  >>> z
  {'a': 1, 'c': 4, 'b': 3}
  
  ```

  

- 一次性判断多个flag

  ```
  x, y, z = 0, 1, 0
   
  if x == 1 or y == 1 or z == 1:
      print('passed')
   
  if 1 in (x, y, z):
      print('passed')
   
  # These only test for truthiness:
  if x or y or z:
      print('passed')
   
  if any((x, y, z)):
      print('passed')
  ```

- 通过值排序字典

```
>>> xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
 
>>> sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
 
# Or:
 
>>> import operator
>>> sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

- 截断汉字
```
str1 = '中国人大大当时'
aa = str1.decode('utf-8')[:3].encode('utf-8')
print aa
>>>中国人
```

- 使用nametuple创建tuple的子类 —— 一种可命名的tuple
```
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

```

- 将字典或列表解成单个元素

```python
def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1

```

- 使用json.dumps格式化字典

```python
>>> my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
>>> my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞

# The "json" module can do a much better job:
>>> import json
>>> print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
>>> json.dumps({all: 'yup'})
TypeError: keys must be a string
```

- 获取矩阵列最大值

```python
maxes = {max(columns) for columns in zip(*matrix)}
```

- 使用timeit库给方法计时

```python
>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))',
                  number=10000)

0.3412662749997253

>>> timeit.timeit('"-".join([str(n) for n in range(100)])',
                  number=10000)

0.2996307989997149

>>> timeit.timeit('"-".join(map(str, range(100)))',
                  number=10000)

0.24581470699922647

```

