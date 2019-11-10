print("HELLO-WORLD")

-- 这是一个单行注释
--[[
这是一个双行注释
--]]
---------LUA之旅正式开始--------------

--Lua 是一个区分大小写的编程语言

--LUA中 不是没有 分号和花括号

--标识符用于定义变量，在LUA中不允许使用特殊字符如 @, $, 和 % 来定义标示符
--最好不要使用下划线加大写字母的标示符，因为Lua的保留字也是这样的。

--关键字
--[[
and , elseif , function , nil , return , while , break, end, if , not , then ,
do, false , in , or , true , else  , for , local , repeat , until
--]]
--默认情况下变量是全局的，local标记局部变量
--访问没有初始化的全局变量不会出错，但是会返回nil
print(b)

--LUa 数据类型
--lua是动态类型语言，变量不需要类型定义，只要赋值就可以
--8种基本类型
--[[
      nil, boolean , number , stirng , userdata , function , thread , table
--]]
print(type("hello"))
print("----------------------------------------------------------")

--nil除了被用来表示空，还可以对全局变量和table起到“删除”的作用。
--给他们付一个nil值，等同于把他们全部删掉

table1 = {key1 = "vall", key2 = "val2", key3 = "val3"}
for k, v in pairs(table1) do
  print(k .. "-" .. v)
end
print()
table1.key1 = nil
for k, v in pairs(table1) do
  print(k .. "-" .. v)
end
print("----------------------------------------------------------")

--boolean
--lua 把false和nil看成假，其他都为真

--number
--lua中只有double类型的数字

--string
--双引号或单引号表示
--也可以[[ ]]来表示“一块”字符串

html =
  [[
    <html>
    <head>This is head</head>
    <body>
       <a herf="http://www.baidu.com/">baidu</a>
    </body>
    </html>
  ]]
print(html)
print("----------------------------------------------------------")

--在对一个数字字符串进行算数操作时，lua会尝试将这个数字字符串转换成一个数字：
print("1" + 2)
print("2" + "2")
print("----------------------------------------------------------")

--使用连字符 ..
print("hello" .. "-" .. "world")
print(157 .. 428) --注意。。两边要空格
print("----------------------------------------------------------")

--使用#计算字符串长度，放在字符串前面
len = "nibushiyigerenzaifendou"
print(#len)
print("----------------------------------------------------------")

--table
--[[
在 Lua 里，table 的创建是通过"构造表达式"来完成，最简单构造表达式是{}，用来创建一个空表。
也可以在表里添加一些数据
--]]
--Lua中表其实是一个 关联数组
--可以像数组一样操作表
--E.G.
a = {}
a["key"] = "value"
key = 10
a[key] = 22
a[key] = a[key] + 11
for k, v in pairs(a) do
  print(k .. ":" .. v)
end
print("----------------------------------------------------------")

--注意！ lua中的默认索引从 1 开始
--E.G.
--local标记局部变量
local b = {11, 22, 33, 44}
for key, value in pairs(b) do
  print("Key", key)
end
print("----------------------------------------------------------")

--注意，table不固定长度，不够会自动增长，空为nil , 真方便

--函数 function
--LUA中函数被看作是“第一类值”,因此可以存在变量里
--E.G.

function factorial(n) --尽然不要返回值类型
  if n == 0 then
    return 1
  else
    return n * factorial(n - 1)
  end
end

print(factorial(5))
factorial2 = factorial --简单粗暴，应该是代表同一个函数
print(factorial2(5))
print("----------------------------------------------------------")

--function可以以匿名函数的方式通过参数传递
--E.G.创建一个函数，将table的键值对交给匿名函数处理相加

function testFun(tbl, fun) --函数定义
  for k, v in pairs(tbl) do
    print(fun(k, v))
  end
end

tbl = {key = "val1", key2 = "val2", key3 = "val3"}
testFun(
  tbl,
  function(key, val) --匿名函数
    return key .. "=" .. val
  end
)
--我们还可以随时改变这个匿名函数
tab2 = {key1 = "val3", key2 = "val4"}
testFun(
  tab2,
  function(key, val) --匿名函数2
    return key .. "+" .. val
  end
)
print("----------------------------------------------------------")

--循环
--while(循环条件)do..执行语句.end
--for..循环方式.do..执行语句.end
--repeat.执行语句..until循环条件
--多层嵌套

--for分为两种，数值FOR/泛型FOR
--[[   1. for var=exp1,exp2,exp3 do
             do something
		  end
--]]
--E.G.
for i = 10, 1, -1 do --从10开始到1，步长为-1
  print(i)
end
print("----------------------------------------------------------")

--[[
       2.通过迭代器遍历所有值，类似foreach
--]]
--E.G.
--ipairs  是LUA中的迭代器函数，用来迭代数组
days = {"Suanday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}
for i, v in ipairs(days) do
  print(v)
end
print("----------------------------------------------------------")

--注意！ LUA中两个迭代器：ipairs/pairs

--pairs:可以遍历表中所有的KEY，并且除了迭代器本身以及遍历本身还可以返回nil
--但ipairs不能返回nil，只能返回数字0，遇到nil则退出。他只能遍历到表中出现的第一个不是整数的key

--LUA流程控制略有区别，只要注意在条件语句后加then，流程结束后加end，且没有花括号包围

--LUA函数格式略有区别，无需返回值类型，在function关键字前有标注全局性的参数

--E.G. 比较两个返回值的最大值

function max(num1, num2)
  if (num1 < num2) then
    return num2
  else
    return num1
  end
end
print("最大值", max(1, 10))
print("----------------------------------------------------------")

--E.G.函数作为参数传递
myprint = function(param) --匿名函数的定义
  print("函数   #", param, "   #")
end

function add(num1, num2, fun) --调用函数定义
  fun(num1 + num2)
end

myprint(10) --调用
add(2, 5, myprint) --调用
print("----------------------------------------------------------")

--多返回值, 很赞
--例如string.find 可以查找匹配字串的起始结束下标

s, e = string.find("jdiniqndi", "ni")
print(s, e)

function MaximunFun(a)
  local max_index = 1
  local maxi = a[max_index]
  for i, val in ipairs(a) do
    if val > maxi then
      max_index = i
      maxi = val
    end
  end
  return maxi, max_index
end

print(MaximunFun({8, 10, 23, 12, 5}))

print("----------------------------------------------------------")

--值得注意的是：这个多返回值列表会根据变量的个数自动调整返回个数 ：
function foo0 () end                   -- returns no results
function foo1 () return 'a' end        -- returns 1 result
function foo2 () return 'a','b' end    -- returns 2 results

--1. 如果函数调用是表达式最后一个参数或者仅有的参数时，不足补nil,多余丢弃
x,y = foo1()              -- x='a', y=nil
x, y = foo2()             -- x='a', y='b'
x = foo2()                -- x='a', 'b' is discarded
x, y, z = 10, foo2()      -- x=10, y='a', z='b'

--2. 其他情况只返回第一个值
x,y = foo2(), 20         -- x='a', y=20
x,y = foo0(), 20, 30     -- x='nil', y=20, 30 is discarded

--3. 函数调用在表构造函数中初始化时，和多值赋值时相同。
a = {foo0()}             -- a = {}    (an empty table)
a = {foo1()}             -- a = {'a'}
a = {foo2()}             -- a = {'a', 'b'}
a = {foo0(), foo2(), 4}  -- a[1] = nil, a[2] = 'a', a[3] = 4

--4. return f()这种形式，则返回“f()的返回值”

--5. 可以使用圆括号强制使调用返回一个值。
print((foo0()))      --> nil
print((foo1()))      --> a
print((foo2()))      --> a
--5.1 一个return语句如果使用圆括号将返回值括起来也将导致返回一个值。



print("----------------------------------------------------------")

--可变参数  符号为3个点
--Lua函数可以接受可变数目的参数
--E.G.  计算平均值
function average(...)
  result = 0
  local arg = {...}
  for i, v in ipairs(arg) do
    result = result + v
  end
  print("共传入" .. #arg .. "个数") --#arg表示参数个数
  return result / #arg
end

print("平均值为： ", average(10, 2, 5, 6, 47))

print("----------------------------------------------------------")

--参数命名
function bonus(quantity, price, rate)
  return quantity * price * rate;
end

function SalerBonus(saler)   --传入的实际是个表
 if type(saler.name) ~= "string" then
     print("no name");
 elseif type(saler.sex) ~= "string" then
     print("no sex");
 elseif type(saler.age) ~= "number" then
     print("no age");
 end

 return bonus(saler.quantity or 20, 
              saler.price or 10, 
              saler.rate or 0.1);
end


print("Tony's bonus is "..SalerBonus{name="Tony", 
sex="male", age=20}.."$");

print("Andy's bonus is "..SalerBonus{name="Andy", 
sex="female", age=25, quantity=50, price=20, rate=0.15}.."$");

print("----------------------------------------------------------")

--LUA运算符
--算数运算符  + ,-, *, %, /, ^
--关系运算符  ==，>, <, >=, <=, ~=     ~=表示不等于
--逻辑运算符  and , or , not    即与，或，非
--其他运算符  ..（连字符）    #（长度符）

--[[  优先级次序,由高到低

^
not    - (unary)
*      /
+      -
..
<      >      <=     >=     ~=     ==
and
or

--]]
--字符串操作
--string.upper(mainString) ,  string.lower(mainString)    大小写

--string.gsub(mainString,findString,replaceString,num)     替换num次，不填num全部替换

print(string.gsub("ni hao hao ma", "hao", "zai", 1)) --num向符合条件的数字取整

--string.find(mainString,findString)  -- 返回查找字串的首尾下标

--strin.reverse(mainString)    --字符串反转

--string.format(...)           --返回一个类似printf的格式化字符串

--string.sub(string,i,j)       --返回i,j之间的字串
local string = "[sdnisndi]"
print(string.sub(string, 2, -2))

--[[string.char(arg)  ,  string.byte(arg[,int])
char 将整型数字转成字符并连接，
byte 转换字符为整数值(可以指定某个字符，默认第一个字符)。
--]]
--E.G.
print(string.char(97, 98, 99, 100)) --针对ascii码
print(string.byte("ABCD", 4)) --4表示转换第四个字符，不填默认为1

--计算字符串长度        string.len(arg)

--返回字符串的n个拷贝    string.rep(string, n)

--string.gmatch(str.pattern)     注意和下面的match区分
--返回一个迭代函数，每次调用这个函数，直到找不到符合的并返回nil
--E.G.
for word in string.gmatch("Hello Lua user", "%a+") do --%a+ 是什么鬼？往下看，这是匹配模式
  print(word)
end
print("----------------------------------------------------------")

--string.match(str,pattern,init)
--它只寻找源字串str中的第一个配对，init为起始位，默认为1
--E.G.
print(string.match("I have 2 questions for you.", "%d+ %a+")) --第二个参数是匹配模式

print(string.format("%d,%q", string.match("I have 2 questions for you.", "(%d+) (%a+)")))

--千万不要将格式化字符串的转义码和匹配模式字符搞混淆
print("----------------------------------------------------------")

--字符串查找与反转 string.reverse（string）
--E.G.
string = "Lua Tutorial"
print(string.find(string, "Tutorial"))
reversedString = string.reverse(string)
print("新字符串为：", reversedString)

print("----------------------------------------------------------")

--字符串的格式化
--[[
Lua 提供了 string.format() 函数来生成具有特定格式的字符串,
 函数的第一个参数是格式 ,
之后是对应格式中每个代号的各种数据。


1. %c     接受一个数字，并将其装换成ASCII码
2. %d, %i 接受一个数字并将其转换成有符号的整数格式
3. %o     接受一个数字并将其转换成8进制格式
4. %u     接受一个数字并转换成无符号整数
5. %x - 接受一个数字并将其转化为十六进制数格式, 使用小写字母
6. %X - 接受一个数字并将其转化为十六进制数格式, 使用大写字母
7. %e - 接受一个数字并将其转化为科学记数法格式, 使用小写字母e
8. %E - 接受一个数字并将其转化为科学记数法格式, 使用大写字母E
9. %f - 接受一个数字并将其转化为浮点数格式
10. %g(%G) - 接受一个数字并将其转化为%e(%E, 对应%G)及%f中较短的一种格式
11. %q - 接受一个字符串并将其转化为可安全被Lua编译器读入的格式
12. %s - 接受一个字符串并按照给定的参数格式化该字符串
--]]
--进一步的，可以在%后添加参数，并以如下的顺序读入：
--[[
     1. 符号： 一个 + 号，表示其后的数字转义符将让正数显示正号，默认只有负数显示符号
	 2.占位符：一个 0 ，在后面指定了字串宽度时占位用，不填时默认为空格
	 3.

--]]
--E.G.
string1 = "lua"
string2 = "Tutorial"
num1 = 10
num2 = 20
--字符串格式化
print(string.format("基本格式化 %s %s", string1, string2)) --%s 类似C#中{0}
--日期格式化
date = 31
month = 10
year = 2017
print(string.format("日期： %02d/%02d/%03d", date, month, year))
--十进制格式化
print(string.format("%.4f", 1 / 3)) --保留小数后四位

print("----------------------------------------------------------")

--匹配模式
--[[

   Lua 中的匹配模式直接用常规的字符串来描述。
   它用于模式匹配函数 string.find, string.gmatch, string.gsub, string.match。
   你还可以在模式串中使用字符类。
   字符类指可以匹配一个特定字符集合内任何字符的模式项。
   比如，字符类%d匹配任意数字。所以你可以使用模式串 '%d%d/%d%d/%d%d%d%d' 搜索 dd/mm/yyyy 格式的日期：

--]]
--E.G.
s = "Deadline is 30/05/1999,firm"
date = "%d%d/%d%d/%d%d%d%d"
print(string.sub(s, string.find(s, date)))

print("----------------------------------------------------------")

--[[          完整如下

       .(点): 与任何字符配对
	   %a: 与任何字母配对
       %c: 与任何控制符配对(例如\n)
       %d: 与任何数字配对
	   %l: 与任何小写字母配对
       %p: 与任何标点(punctuation)配对
       %s: 与空白字符配对
       %u: 与任何大写字母配对
       %w: 与任何字母/数字配对
       %x: 与任何十六进制数配对
       %z: 与任何代表0的字符配对
       %x(此处x是非字母非数字字符): 与字符x配对. 主要用来处理表达式中有功能的字符(^$()%.[]*+-?)的配对问题, 例如%%与%配对
     [数个字符类]: 与任何[]中包含的字符类配对. 例如[%w_]与任何字母/数字, 或下划线符号(_)配对
     [^数个字符类]: 与任何不包含在[]中的字符类配对. 例如[^%s]与任何非空白字符配对



	 '%' 用作特殊字符的转义字符，因此只要记住%后的字符代表什么意思就行

	 模式条目可以是：
	    单个字符类匹配该类别中任意单个字符
		单个字符跟一个 “ * ” ， 将匹配 >= 0 个该类字符，自动取尽可能多
		单个字符跟一个 “ + ” ， 将匹配 >=1 个该类字符。自动取尽可能多
		单个字符跟一个 “ - ” ， 将匹配 >= 0 个该类字符，自动取尽可能少
	    单个字符跟一个 '?'， 将匹配 0 / 1 个该类的字符。 只要有可能，它会匹配一个；
        %n， 这里的 n 可以从 1 到 9； 这个条目匹配一个等于 n 号捕获物（后面有描述）的子串。

		%bxy， 这里的 x 和 y 是两个明确的字符； 这个条目匹配以 x 开始 y 结束， 且其中 x 和 y 保持 平衡 的字符串。
		意思是，如果从左到右读这个字符串，对每次读到一个 x 就 +1 ，读到一个 y 就 -1， 最终结束处的那个 y 是第一个记数到 0 的 y。
		举个例子，条目 %b() 可以匹配到括号平衡的表达式。

		%f[set]， 指 边境模式； 这个条目会匹配到一个位于 set 内某个字符之前的一个空串， 且这个位置的前一个字符不属于 set 。
		集合 set 的含义如前面所述。 匹配出的那个空串之开始和结束点的计算就看成该处有个字符 '\0' 一样。

--]]
--E.G. 将阿拉伯数字转换成汉子数字：
local function NumToCN(num)
  local size = #tostring(num) --# 表示取长度， tostring 表示转为字符串
  local CN = ""
  local StrCN = {"一", "二", "三", "四", "五", "六", "七", "八", "九"}
  for i = 1, size do
    CN = CN .. StrCN[tonumber(string.sub(tostring(num), i, i))] --tonumber转为数字
  end
  return CN
end
print(NumToCN(123456789))
print("----------------------------------------------------------")

--E.G. 分隔字符串
local function StrSplit(inputStr, sep)
  if (sep == nil) then
    sep = "%s"
  end
  local t = {}
  local i = 1
  for str in string.gmatch(inputStr, "[^" .. sep .. "]+") do --gmatch返回迭代器哦，尽可能多的匹配不包含sep
    t[i] = str --向表中加元素
    i = i + 1
  end
  return t --把整个表返回出去
end
local a = "1234567d,汉字"
local c = ":"
c = StrSplit(a, ",") --这里会依照, 号将表截成两段
print(c[1])
print("----------------------------------------------------------")

--数组,迭代器
--[[
    泛型for循环保存了3个值：迭代器函数、状态常量（invariant state）、控制变量（control variable）。
泛型for的语法如下：

for<var-list> in <exp-list> do
       <body>
end

var-list是一个或多个变量列表。exp-list是一个或多个表达式列表，通常只含一个元素即对工厂函数的调用。
变量列表的第一个元素称为“控制变量”。

--]]
array = {"a", "b", "c", "d"}
for k, v in pairs(array) do
  print(k .. " " .. v)
end
print("----------------------------------------------------------")

--无状态迭代器
--无状态的迭代器是指不保留任何状态的迭代器，
--因此在循环中我们可以利用无状态迭代器避免创建闭包花费额外的代价。

--E.G.实现数字n的平方

function square(iter, current)
  if current < iter then
    current = current + 1
    return current, current * current
  end
end
for k, v in square, 3, 0 do
  print(k, v)
end

print("----------------------------------------------------------")

--E.G.迭代器和ipairs的实现
function iter(a, i)
  i = i + 1
  local v = a[i]
  if v then
    return i, v
  end
end

function ipairs(a)
  return iter, a, 0
end

--[[  看到现在，我才对之前所说的泛型for循环的状态变量和控制变量有了一定的认识：
      当Lua调用ipairs(a)开始循环时，他获取三个值：迭代函数iter、状态常量a、控制变量初始值0；
	  然后Lua调用iter(a,0)返回1,a[1]（除非a[1]=nil）；
	  第二次迭代调用iter(a,1)返回2,a[2]……直到第一个nil元素。
--]]
--多状态迭代器
--[[
很多情况下，迭代器需要保存多个状态信息而不是简单的状态常量和控制变量，最简单的方法是使用闭包
还有一种方法就是将所有的状态信息封装到table内，将table作为迭代器的状态常量，
因为这种情况下可以将所有的信息存放在table内，所以迭代函数通常不需要第二个参数。
--]]
--E.G. 自定义迭代器

array = {"Lua", "Tutorial"}

function elementIterator(tabl)
  local index = 0
  local count = #tabl
  --闭包函数
  return function()
    index = index + 1
    if index <= count then
      --返回迭代器当前元素
      return tabl[index]
    end
  end
end

for element in elementIterator(array) do
  print(element)
end

print("----------------------------------------------------------") --连接从start~end的字符，以sep隔开

--table 表
--[[

当我们为 table a 并设置元素，然后将 a 赋值给 b，则 a 与 b 都指向同一个内存。
如果 a 设置为 nil ，则 b 同样能访问 table 的元素。
如果没有指定的变量指向a，Lua的垃圾回收机制会清理相对应的内存。

--]]
--table 的索引下标不一定只是数字

--[[          秀出一波table的操作  [, XXX]  表示可选参数

   1. table.concat(table[,sep[,start[,end]] -- 2. table.insert(talbe,[pos,]value)          --在指定位置pos插入一个value的值，默认在数组末尾
-- 3. table.remove(table[,pos])                --移除POS位的元素，默认末尾处
-- 4. sort(table[,comp])                       --升序排序

--]]

--E.G. concat()

fruits = {"banana", "orange", "apple"}
--返回table连接后的字符串
print("连接后的字符串：", table.concat(fruits))

--指定连接字符
print("连接后的字符串：", table.concat(fruits, ","))

--指定索引连接table
print("连接后的字符串：", table.concat(fruits, ",", 2, 3))

print("----------------------------------------------------------")

--E.G.插入和移除
table.insert(fruits, "mango") --默认插末尾
table.insert(fruits, 2, "pear")
table.remove(fruits) --默认删末尾

--E.G.table排序
print("before sort: ")

for k, v in pairs(fruits) do
  print(k .. " " .. v)
end
print()
table.sort(fruits)
print("after sort: ")

for k, v in pairs(fruits) do
  print(k .. " " .. v)
end
print("----------------------------------------------------------")

--E.G.获取table中的最大值

function table_maxn(tbl)
  local mn = nil
  for k, v in pairs(tbl) do
    if (mn == nil) then --第一次赋值
      mn = v
    end
    if mn < v then --如果小于V，则赋值
      mn = v
    end
  end
  return mn
end
tbl = {[1] = 2, [2] = 6, [3] = 34, [26] = 5}
print("tbl 最大值：", table_maxn(tbl))
print("tbl 长度：", #tbl)
print("----------------------------------------------------------")

--LUA模块与包
--模块类似于一个封装库，Lua 加入了标准的模块管理机制，
--可以把一些公用的代码放在一个文件里，以 API 接口的形式在其他地方调用，有利于代码的重用和降低代码耦合度。

--[[
Lua 的模块是由变量、函数等已知元素组成的 table，因此创建一个模块很简单，就是创建一个 table，
然后把需要导出的常量、函数放入其中，最后返回这个 table 就行。

--]]
--E.G.

--文件名为 module.lua
--引用模块

local m = require "module"
print(m.constant)
m.func3()
print("----------------------------------------------------------")

--LUA元表
--[[

在 Lua table 中我们可以访问对应的key来得到value值，但是却无法对两个 table 进行操作。
因此 Lua 提供了元表(Metatable)，允许我们改变table的行为，每个行为关联了对应的元方法。
例如，使用元表我们可以定义Lua如何计算两个table的相加操作a+b。

有两个很重要的函数来处理元表：
setmetatable(table,metatable): 对指定table设置元表(metatable)，如果元表(metatable)中存在__metatable键值，setmetatable会失败 。
getmetatable(table): 返回对象的元表(metatable)。

--]]
--E.G. 以下实例演示了如何对指定的表设置元表

mytable = {}
mymetatable = {}
setmetatable(mytable, mymetatable)

--以上代码可直接写成一行：mytable = setmetatable({},{})

getmetatable(mytable)

--   __index(双_) 元方法

--  当__index是一个表时，lua会查找对应的键,没有则返回nil

other = {foo = 3}
t = setmetatable({}, {__index = other})
print(t.foo)

--  当__index包含一个函数时，lua会调用该函数，并将table和键作为参数传递进去

mytable =
  setmetatable(
  {key1 = "value1"},
  {
    __index = function(mytable, key)
      if key == "key2" then
        return "metetatablevalue"
      else
        return nil
      end
    end
  }
)

print(mytable.key1, mytable.key2)
print("----------------------------------------------------------")
--[[
以上可以简写为：
    mytable = setmetatable({key1 = "value1"},{__index = {key2 = "metetatablevalue"}})
    print(mytable.key1,mytable.key2)
--]]
--[[
Lua查找一个表元素时的规则，其实就是如下3个步骤:
1.在表中查找，如果找到，返回该元素，找不到则继续
2.判断该表是否有元表，如果没有元表，返回nil，有元表则继续。
3.判断元表有没有__index方法，如果__index方法为nil，则返回nil；
  如果__index方法是一个表，则重复1、2、3；
  如果__index方法是一个函数，则返回该函数的返回值。
--]]
--   __newindex 方法
--   __newindex用来对表更新， __index用来对表访问
--当你给表的一个缺少的索引赋值，解释器就会查找__newindex 元方法：如果存在则调用这个函数而不进行赋值操作。
--E.G.

mymetatable = {}
mytable = setmetatable({key1 = "value1"}, {__newindex = mymetatable})

print(mytable.key1)

mytable.newkey = "新值2"
print(mytable.newkey, mymetatable.newkey)

mytable.key1 = "新值1"
print(mytable.key1, mymetatable.key1)
print("----------------------------------------------------------")

--给表添加操作符 ---
--使用之前自定义的取最大值函数table_maxn
--执行两表相加操作

mytable =
  setmetatable(
  {1, 2, 3},
  {
    __add = function(mytable, newtable)
      for i = 1, table_maxn(newtable) do
        table.insert(mytable, table_maxn(mytable) + 1, newtable[i])
      end
      return mytable
    end
  }
)

secondtable = {4, 5, 6}

mytable = mytable + secondtable

for k, v in ipairs(mytable) do
  print(k, v)
end
print("----------------------------------------------------------")

--表的的操作函数 ， 完整如下

--[[

    __add      +
	__sub      -
	__mul      *
	__div      /
	__mod      %
	__unm      -
	__concat   ..
	__eq       ==
	__lt       <
	__le       <=

--]]
--  __call元方法    在调用一个值时调印。

--E.G.计算表中元素的和

--计算表中最大键函数，table.maxn 在lua5.2后无法使用
--依旧是用之前自定义的table_maxn函数,计算表元素个数

-- 定义元方法__call
function table_maxn(t)
  local mn = 0
  for k, v in pairs(t) do
    if mn < k then
      mn = k
    end
  end
  return mn
end

-- 定义元方法__call
mytable =
  setmetatable(
  {10},
  {
    __call = function(mytable, newtable)
      sum = 0
      for i = 1, table_maxn(mytable) do
        sum = sum + mytable[i]
      end
      for i = 1, table_maxn(newtable) do
        sum = sum + newtable[i]
      end
      return sum
    end
  }
)
newtable = {10, 20, 30}
print(mytable(newtable))
print("----------------------------------------------------------")

--  __tostring 元方法，用于修改表的输出行为。
tablestring =
  setmetatable(
  {1, 2, 3},
  {
    __tostring = function(tablestring)
      sum = 0
      for k, v in ipairs(tablestring) do
        sum = sum + v
      end
      return "表中元素和为： " .. sum
    end
  }
)
print(tablestring)
print("----------------------------------------------------------")

