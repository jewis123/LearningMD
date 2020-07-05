- 字符串驻留

  python在编译优化时, 某些情况下会尝试使用已经存在的不可变对象，而不是每次都创建一个新对象. (这种行为被称作字符串的驻留[string interning])。许多变量可能指向内存中的相同字符串对象. (从而节省内存)

  有如下情况会发生''字符串驻留''：

  1. 所有长度为 0 和长度为 1 的字符串
  2. 编译期创建的字符串
  3. 字符串中只包含字母、数字、下划线
  4. 同一行上两个变量设置的字符串内容一致（只适用3.7以下）
  5. `长度小于 20 `的字符串进行常量折叠：'a'*20` 会被替换为 `'aaaaaaaaaaaaaaaaaaaa'
  
  [例子](https://github.com/jewis123/wtfpython-cn#-strings-can-be-tricky-sometimes%E5%BE%AE%E5%A6%99%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2-)

- hash键值相同即为同一键，不管类型是否一不一致``

  [例子](https://github.com/jewis123/wtfpython-cn#-time-for-some-hash-brownies%E6%98%AF%E6%97%B6%E5%80%99%E6%9D%A5%E7%82%B9%E8%9B%8B%E7%B3%95%E4%BA%86)

- 当在 "try...finally" 语句的 `try` 中执行 `return`, `break` 或 `continue` 后, `finally` 子句依然会执行，函数的返回值由最后的`return`决定， 所以最终执行的是`finally`的return

  ```python
  def some_func():
      try:
          return 'from_try'
      finally:
          return 'from_finally'
  Output:
  
  >>> some_func()
  'from_finally'
  ```

  

- [迭代器在解包的时候会默认执行赋值操作](https://github.com/jewis123/wtfpython-cn#-for-what%E4%B8%BA%E4%BB%80%E4%B9%88)
- 