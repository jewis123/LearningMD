### 什么是JIT

它是[动态编译](https://www.jianshu.com/p/14c3d36e6ffa)的一种形式，是优化虚拟机运行的技术。

那，他是怎么优化虚拟机的运行过程的呢？

`Lua`代码通过`Luac`编译成字节码，然后会再通过解释器将字节码转换成机器码。字节码到机器码的转换过程中会存在重复的热点函数，这个时候通过`JIT`

一次性编译热点代码，然后缓存起来，避免解释器重复解释。下图描绘了这个过程：

![](转码流程图.png)

luajit的jit模式（pc和安卓可用）、luajit的interpreter模式（ios下只能运行这个）。

### Lua 和 LuaJIT

#### 组成部分

Lua主要由以下三部分组成：

1. 语法实现。
2. 库函数。
3. 字节码。

LuaJIT主要由以下四部分组成：

1. 语法实现。
2. Trace JIT编译器。
3. 库函数。
   1. 原生库++（强化过的原生库）
   2. bit
   3. ffi
   4. jit
4. 字节码

#### 关系

Lua是一种编程语言，LuaJIT是Lua的一种运行时编译器，它支持将Lua代码进行运行时优化，所以它对应的Lua支持是要关注版本的。

[相关资料：UWA文章](https://blog.csdn.net/UWA4D/article/details/72916830?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.not_use_machine_learn_pai&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-3.not_use_machine_learn_pai)做如下总结：

LuaJIT并不能百分百JIT化Lua代码，也就是说他的优化功效是比较难控制的，受系统平台、Lua版本语法的限制。另外，再使用LuaJIT前要充分了解它潜在的坑点，不然反而会出现性能问题，例：

- 提前分配给LuaJIT64兆连续内存空间；
- 需要照着LuaJIT的偏好写Lua代码(因为部分Lua编译出来的字节码LuaJIT并不支持)；
- LuaJIT在局部变量过多的时候会导致寄存器不够用，所以要避免过多局部变量，并限制局部变量的生命周期。
- 调用C/C#代码无法JIT化，需要使用ffi，或者2.1.0+版本LuaJIT
- 不要过度使用C#调用Lua，很慢。
- LuaJIT虽然难以驾驭，但是可以使用`Interpreter`模式，行为更接近原生Lua，性能平均也能快2~3倍，同时不需要对Lua语言进行过多优化。
- 最大的问题：目前停止迭代了，Lua标准停在了5.1上。

### 结语

JIT是一个比较通泛的问题，相关的话题在JAVA, Python上也会有涉及，由于LuaJIT已经停止维护，所以大概率会淡出人们视线。

