[TOC]

## 直击灵魂的问题

python是怎么将模块文件(module)编译成可用对象的？

分解问题涉及的内容：对象系统，编译、虚拟机、名字空间、import机制

解答这个问题其实能还好的帮我们了解python的运作机理，分几篇探索，每篇文章会先介绍相关内容，最后做阶段性总结。

# python对象探究

## PyObject：对象系统的基石

### 包含哪些数据？

- 引用计数
- 类型对象（指向对象类型）

这些数据实际都存在PyObject_HEAD中。

## PyTypeObject：

PyObject中的第二个数据成员，对象相关的元信息实际都存在这里

### 组成成分？

- 类型名
- 占用内存大小
- 类型支持的操作
- 类型信息

### 类型对象的创建

**两种方式？**

- 多态接口创建（例如：直接实例化PyObject_XXX）
- 通过特定接口创建相应类型（例如：PyInt_FromLong(10)）
- 泛型API, (PyObject_XXX( type_instance))
- COL, 通过特定接口创建相应类型（例如：PyString_FromString(s)）

### 类型行为: PyTypeObject的3种基本操作族

tp_as_number, tp_as_sequence,tp_as_mapping，不同的操作族中包含不同的函数指针，定义了不同的类型特性。

### 混合类型对象的行为？

通过实现类型的相关魔法函数，让python内部去指定函数指针。PyTypeObject允许一种类型同时指定不同对象的行为特性。

## 万物皆对象？

### 类型对象对应的类型：PyType_Type

所有自定义class所对应的PyTypeObject对象都是通过PyType_Type这个对象创建的。

`PyType_Type`也被称为`元类型(metaclass)`（敲黑板，划重点）

### 区分类型对象和对象类型

类型对象即**PyXXObject**，对象类型即**PyXXX_Type**。**类型对象 is instance of 对象类型**。他们之间的关系可以看下图。

### 类型之间的关系

![类型关系](img/类型关系.png)

### Python对象的多态性

Python通过`PyObject` + `PyTypeObject`结合C实现了多态，在创建对象后，Python会使用`PyObject*` 来储存对象，python内部函数之间传递的都是这种泛型指针，只有通过指针所指对象的`ob_type`域才能动态确定类型。

### 引用计数

在一个对象的引用计数变为0的时候，会调用其析构函数，但并不意味着释放其内存空间，通常是将其占用的内存归还到内存池。

python假设一个对象的引用计数不会大于32位整形变量

特别的，类型对象永远不会被析构，对象指向类型对象的指针也不为视为引用。

## Python对象的分类

![对象的分类](img/对象的分类.png)

额外解释：

Fundamental对象：类型对象

Internal对象：虚拟机运行时内部使用的对象

## 回顾开头问题

从上图我们看到模块对象是由虚拟机在运行时创建出来的对象，所以在我们了解虚拟机运行时做了什么之前，暂时无法完整回答这个问题。

但是我们可以先了解**模块对象**是个什么对象类型,以及它对应的类型对象。

通过源码能看到，这个可用`module`对象他的类型是`PyModule_Type`，而对应的类型对象是**`PyModuleObject`**

![](img/PyModuleObject.png)

![module_init](img/PyModule_Type.png)