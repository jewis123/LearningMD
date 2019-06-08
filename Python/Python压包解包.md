python中的解包可以这样理解：一个list是一个整体，想把list中每个元素当成一个个个体剥离出来，这个过程就是解包，我们来看下面这些例子（分为10个部分）。 

**1.将list中每个元素赋值给一个变量**

```javascript
>>> name, age, date = ['Bob', 20, '2018-1-1']
>>> name
'Bob'
>>> age
20
>>> date
'2018-1-1'
```

**2.可迭代对象都可以这样做**

```javascript
# 列表
>>> a,b,c = ['a', 'b', 'c']
>>> a
'a'

>>> a,b,c = enumerate(['a', 'b', 'c'])
>>> a
(0, 'a')


# 元组
>>> a,b,c = ('a', 'b', 'c')
>>> a
'a'

# 字典
>>> a,b,c = {'a':1, 'b':2, 'c':3}
>>> a
'a'

>>> a,b,c = {'a':1, 'b':2, 'c':3}.items()
>>> a
('a', 1)


# 字符串
>>> a,b,c = 'abc'
>>> a
'a'

# 生成器
>>> a,b,c = [x + 1 for x in range(3)]
>>> a
1
```

如果可迭代对象包含的元素和前面待赋值变量数量不一致，则会报错。但是可以通过*来表示多个元素

**3.星号的使用** 

比如我们要计算平均分，去除最高分和最低分，除了用切片，还可以用解包的方式获得中间的数值

```javascript
>>> first, *new, last = [94, 85, 73, 46]
>>> new
[85, 73]
```

用*来表示多个数值

**4.压包过程** 

压包是解包的逆过程，用zip函数实现，下面例子可以对压包有一个直观的感受

```javascript
>>> a = ['a', 'b', 'c']
>>> b = [1, 2, 3]
>>> for i in zip(a, b):
...     print(i)
...
('a', 1)
('b', 2)
('c', 3)
```

**5.压包与解包混合的例子** 

下面例子实现：两个列表对应数值相加

```javascript
>>> a = [0, 1, 2]
>>> b = [1, 2, 3]
>>> for i, j in zip(a, b):
...     print(i+j)
...
1
3
5
```

细细拆解上面过程，可以看出步骤是这样的

- 先是zip函数将a b压包成为一个可迭代对象
- 对可迭代对象的每一个元素（('a', 1)）进行解包（i, j = ('a', 1)）
- 此时就可以分别调用i j变量进行计算 下面我们加入星号

```javascript
>>> l = [('Bob', '1990-1-1', 60),
...     ('Mary', '1996-1-4', 50),
...     ('Nancy', '1993-3-1', 55),]
>>> for name, *args in l:
...     print(name, args)
...
Bob ['1990-1-1', 60]
Mary ['1996-1-4', 50]
Nancy ['1993-3-1', 55]
```

**6._的用法** 

当一些元素不用时，用_表示是更好的写法，可以让读代码的人知道这个元素是不要的

```javascript
>>> person = ('Bob', 20, 50, (11, 20, 2000))
>>> name, *_, (*_, year) = person
>>> name
'Bob'
>>> year
2000
```

**7.多变量同时赋值** 

之前赋值符号右侧都是可迭代对象，其实右侧也可以是多个变量

```javascript
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>> a = 1, 2
>>> a
(1, 2)
```

下面用法都会报错

```javascript
*a = 1, 2
a, b, c = 1, 2
```

可以这样

```javascript
*a, = 1, 2
```

**8.\*之可变参数** 

函数定义时，我们使用*的可变参数，其实也是压包解包过程

```javascript
>>> def myfun(*num):
...     print(num)
...
>>> myfun(1,2,5,6)
(1, 2, 5, 6)
```

参数用*num表示，num变量就可以当成元组调用了。

其实这个过程相当于*num, = 1,2,5,6

**9.\*之关键字参数**

```javascript
>>> def myfun(**kw):
...     print(kw)
...
>>> myfun(name = "Bob", age = 20, weight = 50)
{'weight': 50, 'name': 'Bob', 'age': 20}
```

键值对传入**kw，kw就可以表示相应字典。

**的用法只在函数定义中使用，不能这样使用

```javascript
a, **b = {'weight': 50, 'name': 'Bob', 'age': 20}
```

**10.可变参数与关键字参数的细节问题** 

(1)函数传入实参时，可变参数(*)之前的参数不能指定参数名

```javascript
>>> def myfun(a, *b):
...     print(a)
...     print(b)
...
>>> myfun(a=1, 2,3,4)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument

>>> myfun(1, 2,3,4)
1
(2, 3, 4)
```

(2)函数传入实参时，可变参数(*)之后的参数必须指定参数名，否则就会被归到可变参数之中

```javascript
>>> def myfun(a, *b, c=None):
...     print(a)
...     print(b)
...     print(c)
...
>>> myfun(1, 2,3,4)
1
(2, 3, 4)
None
>>> myfun(1, 2,3,c=4)
1
(2, 3)
4
```

如果一个函数想要使用时必须明确指定参数名，可以将所有参数都放在可变参数之后，而可变参数不用管它就可以，也不用命名，如下

```javascript
>>> def myfun(*, a, b):
...     print(a)
...     print(b)
...
>>> myfun(a = 1,b = 2)
1
2
```

可变参数的这两条特性，可以用于将 只需要按照位置赋值的参数 和 需要明确指定参数名的参数区分开来

(3)关键字参数都只能作为最后一个参数，前面的参数按照位置赋值还是名称赋值都可以

下面展示一个既用可变参数有用关键字参数的例子

```javascript
>>> def myfun(a, *b, c, **d):
...     print(a)
...     print(b)
...     print(c)
...     print(d)
...
>>> myfun(1, 2, 3, c= 4, m = 5, n = 6)
1
(2, 3)
4
{'n': 6, 'm': 5}
```

(4)可变参数与关键词参数共同使用以表示任意参数

下面是这一点在装饰器当中的使用

```javascript
>>> def mydecorator(func):
...     def wrapper(*args, **kw):
...         print('I am using a decorator.')
...         return func(*args, **kw)
...     return wrapper
...
>>> @mydecorator
... def myfun(a, b):
...     print(a)
...     print(b)
...
>>> myfun(1, b = 2)
I am using a decorator.
1
2
```

(如果有的读者不熟悉装饰器，只需要知道，使用@定义myfun相当于myfun = mydecorator(myfun)，定义出来的myfun其实是返回结果wrapper函数)

wrapper函数使用args, *kw作为参数，则被修饰的myfun函数需要的参数无论是什么样的，传入wrapper都不会报错，这保证了装饰器可以修饰各种各样函数的灵活性。毕竟我们一般在函数中传入参数时，要么所有参数名都写，要么前面几个不写，后面的会写，这样使用args, *kw完全没有问题。

**11.解包作为参数传入函数中** 

首先定义一个函数

```javascript
def myfun(a, b):
    print(a + b)
```

列表元组的解包

```javascript
>>> n = [1, 2]
>>> myfun(*n)
3
>>> m = (1, 2)
>>> myfun(*m)
3
```

字典的解包

```javascript
>>> mydict = {'a':1, 'b': 2}
>>> myfun(**mydict)
3
>>> myfun(*mydict)
ba
```

一个应用

```javascript
>>> bob = {'name': 'Bob', 'age': 30}
>>> "{name}'s age is {age}".format(**bob)
"Bob's age is 30"
```

**12.多返回值函数** 

下面过程也涉及到了解包

```javascript
def myfun(a, b):
    return a + 1, b + 2
>>> m, n = myfun(1, 2)
>>> m
2
>>> n
4
```

其实本身是一个元组

```javascript
>>> p = myfun(1, 2)
>>> p
(2, 4)
```