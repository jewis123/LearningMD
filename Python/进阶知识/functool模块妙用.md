- **@functools.lru_cache**

> @functools.lru_cache(maxsize=128, typed=False)
> New in version 3.2.
> Changed in version 3.3: Added the typed option.

这个装饰器实现了备忘的功能，是一项优化技术，把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。lru 是（least recently used）的缩写，即最近最少使用原则。表明缓存不会无限制增长，一段时间不用的缓存条目会被扔掉。

适合缓存递归中的重复计算结果，减少调用次数。

- **@functools.singledispatch**

> New in version 3.4.

python不支持函数的重载，但是这个装饰器能够将普通函数转变成泛函数。

比如你要针对不同类型的数据进行不同的处理，而又不想将它们写到一起，那就可以使用 @singledispatch 装饰器了

```python
@functools.singledispatch
def typecheck():
    pass

@typecheck.register(str)
def sameNameFunc(text):
    print(type(text))
    print("str--")

@typecheck.register(list)
def sameNameFunc(text):
    print(type(text))
    print("list--")

@typecheck.register(int)
def sameNameFunc(text):
    print(type(text))
    print("int--")
```