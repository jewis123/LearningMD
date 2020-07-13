[TOC]

## .py文件转变

我们在执行**py文件**的时候会激活**python解释器**去编译文件代码，产生一组Python的**字节码**，再交给**Python虚拟机**按序执行。

### 编译结果

python代码经过解释器编译得到的内容，准确来说不只是字节码，还包含一些源代码中的静态信息。

这些静态信息是由解释器在运行时，从源代码中收集的（常量，字符串等），它们会被暂时储存在**PyCodeObject**中，在Python运行结束后，`PyCodeObject`的内容会被保存到**pyc文件**。

所以，`PyCodeObject`才是解释器的编译结果，`pyc`文件只是保存到硬盘的形式，供下次运行快速在内存中直接创建PyCodeObject对象。

- 那么PyCodeObject的创建规则是怎样的呢？

  当编译到一个新的作用域时，就会创建一个PyCodeObject去对应这块代码。

- pyc文件的产生

  在交互式环境中，由于代码的运行需求是临时性的所以不会产生pyc文件。而`.py`文件中加入了`import`,就会触发创建pyc文件，这个pyc文件对应的就是被导入的模块的信息。

- pyc文件包含的内容

  - magic_number：不同的python版本magic_number也不同，python不会加载不属于自己版本magic_number的pyc文件。
  - 时间：py文件和pyc文件时间修改时间不同，会导致重现创建pyc文件。
  - PyCodeObject



