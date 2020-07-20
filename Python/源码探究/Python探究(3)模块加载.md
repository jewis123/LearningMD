## module存在的意义

- 代码复用
- 划分名字空间

## 使用module方式

- import动态加载
- python module.py的形式直接加载

## Python运行环境初始化

- 线程环境初始化：这期间主要做的是**线程状态对象**（PyThreadState）和**进程状态对象**（PyInterperState）之间建立联系。
- 类型系统初始化
- 设置全局变量`builtin_object`
- 其他

## 系统module初始化

这一部分的初始化发生在上述第一点和第二点之间，通过**`_PyBuiltin_Init`**来设置。而第一个被创建出来的`module`是**`__builtin_`** `module`。后续所有加载出来的`module`都储存在一个**`PyDictObject`**对象中，同时这个对象被保存在进程状态对象上。

### **`_PyBuiltin_Init`**设置系统模块两步骤

- 创建**`PyModuleObject`**对象
- 设置`module`，将所有类型对象全部加入新建的**`__builtin_`** `module`中。对应源码中的**`Py_InitModule4`**
- **`Py_AddModule`** + **`Py_GetModuleDict`** + **`PyModule_New`**来创建`module`对象本身，这是模块对象会被加入前文提到的一个**`PyDictObject`**对象中，有`Python`内部维护，这里存在了所有被加载到内存的模块对象。

