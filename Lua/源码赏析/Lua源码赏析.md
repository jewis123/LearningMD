### 源码目录划分

http://www.lua.org/source/5.3/

**虚拟机运作核心**

lapi.c 		         C语言接口
lctype.c              C标准库中`ctype`相关实现
ldebug.c 			Debug接口
ldo.c            		函数调用以及栈管理
lfunc.c         		函数原型及闭包管理
lgc.c             		垃圾回收
lmem.c       		内存管理接口
lobject.c      		对象操作的一些函数
lopcodes.c 		虚拟机的字节码定义
lstate.c       		全局状态机

lstring.c 			字符串池
ltable.c 			表类型的相关操作
ltm.c 				元方法
lvm.c 				虚拟机 (对字节码解析并运作)
lzio.c 				输入流接口

**源代码解析及预编译字节码**

lcode.c 			代码生成器
ldump.c 			序列化预编译的 Lua 字节码
llex.c 				词法分析器
lparser.c 			解析器
lundump.c 		还原预编译的字节码

**可执行的解析器，字节码编译器**

lua.c 解释器
luac.c 字节码编译器

**内嵌库（lib后缀）**



### 代码风格

- `Lua`的内部模块暴露出来的 `API` 以 `luaX_xxx` 风格命名，即 `lua`后跟一个大写字母表识内部模块名（比如 `luaT_objtypename`），而后由下划线加若干小写字母描述方法名。
- 供外部程序使用的 `API` 则使用 `lua_xxx` 的命名风格。这些在`lua`的官方文档里有详细描述。定义在`lua.h`文件中。
- `luaV`系列 `API` 和虚拟机操作相关，对应在`lvm.h`中
- `luaL`系列 `API` 供库开发使用，对应在`lauxlib.h`中
- `luaE`开头的`API`和全局状态机相关，对应在`lstate.c`
- `luaD`开头的`API`和函数调用相关，对应在`ldo.c`
- `luaF, luaH, luaS， luaT`开头的`API`和`function,table,string,metatable`操作相关，分别对应在`lfunc.c, ltable.c, lstring.c, ltm.c`。
- 不同的数据类型最终被统一成`LuaObjcet`，相关操作以`luaO`开头,，对应在`lobject.c`。
- `luaM`开头的`API`和内存管理相关，对应在`lmem.c`
- `luaZ`开头的`API`和带缓冲的流处理相关，对应在`lzio.c`
- `luaC`开头的`API`和GC相关，对应在`lgc.c`
- `luaY`开头的`API`和代码解析相关，对应在`lparser.c`， 将lua程序转成字节码和常量数据
- `luaK`开头的`API`，对应在`lcode.c`
- `luaU`开头的`API`和预编译相关，把运行时编译结果生成字节码，对应在`ldump.c, lundump.c`中
- 直接以`lua`开头的`API`，可用C程序直接调用.

### 推荐源码阅读次序

- 外围库
- 虚拟机实现
- string,table,metatable
- debug模块
- parser
- GC