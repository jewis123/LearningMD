
'''
                                          一、基础语法
'''
# py 没有语句块没有{}，它通过缩进匹配实现语句块，缩进不匹配会报 IndentationError,请务必遵守约定俗成的习惯，坚持使用4个空格的缩进。

# py中的在成员的名字前加上两个下划线__，这个成员就变成了一个私有成员（private），否则就是public

'''输入输出'''
# 输出
import random
print("hello world")

# 输入
name = input()
print("hi", name)

###############################################################

"""
多行语句
"""
# Python 通常是一行写完一条语句，但如果语句很长，我们可以在行尾使用反斜杠(\)来实现多行语句
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)


# 多变量赋值
# a=b=c=1    赋同值
# a, b, c = 1, 2, "runoob"  赋异值

###############################################################

'''保留字'''
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

###############################################################

'''
                                         二、数据类型：
'''
#                                        Number 类型：

# int bool float(浮点数) complex(复数：1+5j)  https://www.runoob.com/python3/python3-number.html
# 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。

# 到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

# 数值运算：除了加减运算；**表示乘方；%取余；/浮点除法；//整数除法

# 混合运算会把整形换成浮点型

# 常用Number运算函数需记住
t = (1, 2, 3, 4, 5)
print(max(t))

#### 多种随机函数 : 导入random库

random.choice(t)  # 从序列的元素中随机挑选一个元素
num = random.randrange(1, 100, 2)  # 从 1-100 中选取一个奇数
random.random()   # 随机生成一个【0，1）的数
random.shuffle(t)  # 将序列元素随机打乱
random.uniform(1, 10)  # 随机生成下一个实数，范围[x,y]

# 三角函数：导入math库

################################

#                                        String 类型：

# 单引号和双引号作用相同；反斜杠转义，在字符串前使用r屏蔽转义
# https://www.runoob.com/python3/python3-string.html
print("ni\nhao")
print(r"ni\nhao")
print("this""is""me", end='!\n')
print("this", "is", "me", sep=",", end='!\n')
print("this"*3)   # *号表示重复

'''
字符串的切片
'''

# 两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# 字符串不能改变
# 没有单独的字符类型，一个字符就是长度为 1 的字符串
# 截取的语法格式如下：变量[头下标:尾下标:步长]

str = "this is a string"
print(str[0:4])  # 第一个到第四个的字符
print(str[2:])  # 第三个以后所有的字符
print(str[2:9:2])  # 第三个到第九个字符间每隔1个组成的字符

# print 的\n 也算一个字符数

# 常用String操作需记住
# https://www.runoob.com/python3/python3-string.html

# 字符串格式化：
print("我叫 %s 今年 %d 岁!" % ('小明', 10))
"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))  # 指定键值

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list1 = ['菜鸟教程', 'www.runoob.com']
my_list2 = ['慕课网', 'www.mook.com']
print("网站名：{0[0]}, 地址 {1[1]}".format(my_list1, my_list2))  # "[]"前的数字表示第几个列表

# 数字格式化
# 用{}定义{}
print("{} 对应的位置是 {{0}},{}对应的位置时{{1}}".format("runoob", "com"))

# 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

################################

# Tuple

t = ('a', 'b', 'c', 'd')
# 基本和list相似，但是元素不可修改
tup1 = ()  # 空元组
tup2 = ('20',)  # 一个元素的元组
# 元组和列表可以相互转换

################################

#                                          List：

# 列表中元素的类型可以不同，甚至可以嵌套列表
# https://www.runoob.com/python3/python3-list.html
# 记住常用列表操作

# 列表被截取后返回新列表，截取规则和string类似

# 可以改变取出来的值

# 使用+号拼接列表

################################

# Set :

# 基本功能是进行 成员关系测试 和 删除重复元素
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')


# set可以进行集合运算，是一个无序的不重复元素序列
a = set('abracadabra')
b = set('alacazam')
c = set()  # 空集合
print(a)
print(a - b)     # a 和 b 的差集   =    set.difference(set1,set2..)
print(a | b)     # a 和 b 的并集   =     set.union(set1,set2..)
print(a & b)     # a 和 b 的交集   =    set.intersection(set1,set2..)
print(a ^ b)     # a 和 b 中不同时存在的元素

# 记住常用集合操作
thiset = set(("google", "taobao"))
thiset.add("Facebook")  # 添加元素

thiset.update({1, 3})  # 添加set
thiset.update((2, 3))  # 添加元组
thiset.update([1, 4], [5, 6])  # 添加list

thiset.remove('taobao')  # 元素不存在会报错
thiset.discard('yahoo')  # 不存在不会报错

thiset.pop()  # 随机移除
print(thiset)

################################

#                                         Dictionary：

# 列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# https://www.runoob.com/python3/python3-dictionary.html
dict = {}  # 先定义空字典再加元素
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
print(dict)

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}  # 直接定义字典和元素

# 1.字典的key必须是不可变类型，且不能重复；key对应的值采用最新原则

# list,dictionary,set是可变数据，number,string,tuple是不可变数据

# type()查询类型

# isinstance(,)判断类型

# type()不会认为子类是父类类型，isinstance会

# 记住字典操作


# 数据类型转换
# 一般用目标类型强转对象即可，python有多种内置类型转换函数

###############################################################
'''
                                            三、流程控制
'''

'''
运算符
'''
# 1.逻辑运算符
# python没有 && ， ||， ！
# 用         and, or , not 替代

# 2.成员运算符
# in, not in

# 3.身份运算符:用于判断是否同一引用
#               is, is not

###############################################################

'''
分支结构
'''
# if else
if name == "ddddd":
    print("yes")
elif name == "sss":
    print("no")
else:
    pass


###############################################################

'''
循环
'''
# while循环
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:  # 可加可不加
    print(count, " 大于或等于 5")

# for循环
sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:  # 可加可不加
    print("没有循环数据!")
print("完成循环!")

# 遍历数字序列可以使用range（）生成一个指定序列
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

# 还可以使用list(range())函数来创建一个列表
# pass是空语句，是为了保持程序结构的完整性。

###############################################################
'''
                                          四、函数
'''

'''
函数基础
'''
# 例子
def summer(lis):
    """
    这里是函数的说明文档，doc的位置
    :param ：形参定义，属传入参数
    :return: 返回值的说明
    """
    total = 0
    for i in lis:
        total += i
    return total

'''
参数:位置参数、默认参数、动态参数
'''

# 1. 函数可以返回几乎任意python对象
# 2. 可以多返回
# 3. 默认参数必须在位置参数后面
# 4. 默认参数要么才传参是都指定名字，要么按原顺序传入且都不指定名字
# 5. 参数传入是如果都用形参名指定，可以不按照形参定义顺序传递
# 6. 默认参数如果指向可变对象，结果会多次叠加,因为python中参数的传递其实传递的是地址，不变量的地址是不会变的
def func(a=[]):
    a.append("A")
    return a

print(func())
print(func())
print(func())
## >>>['A']
## >>>['A', 'A']
## >>>['A', 'A', 'A']

## 如上可改为
def func(a=None):
    # 注意下面的if语句
    if a is None:
        a = []
    a.append("A")
    return a

#     动态参数：
# Python的动态参数有两种，分别是*args和**kwargs，必须放在所有位置参数和默认参数后面

## 1.*args：一个星号表示接收任意个参数。调用时，会将实际参数打包成一个元组传入形式参数。如果参数是个列表，会将整个列表当做一个参数传入。
##      如果想把列表等序列对象拆分出来， 可以在对象前加 一个星号
def func(*args):
    for arg in args:
        print(arg)

li = [1, 2, 3]
func(li)
## >>> [1,2,3]
func(*li)
## >>> 1
## >>> 2
## >>> 3

## 2.**kwargs：两个星表示接受 <br>键值对</br> 的动态参数，数量任意。调用的时候会将实际参数打包成字典，对kwarg的修改不会对原字典造成修改。
##        如果想把字典中的键值对拆分出来， 可以在对象前面加两个星号
def func(**kwargs):
    for kwg in kwargs:
        print(kwg, kwargs[kwg])

dic = {
    'k1': 'v1',
    'k2': 'v2'
}

func(**dic,k3='v3')
## >>> k1 v1
## >>> k2 v2
## >>> k3 v3


## 3. “万能”参数：把*args和**kwargs组合使用，理论上可以接收任意参数，但*args要放在*kwargs之前
# 例子
def func(a, b, c=1, *args, **kwargs):
    print('c的值是:', c)
    for arg in args:
        print(arg)

    for kwg in kwargs:
        print(kwg, kwargs[kwg])


lis = ['aaa', 'bbb', 'ccc']
dic = {
    'k1': 'v1',
    'k2': 'v2'
}

func(1, 2, *lis, **dic)
## >>>c的值是: aaa               
##...bbb
##...ccc
##...k1 v1
##...k2 v2
####因为传参规则（一切没有提供参数名的实际参数，都会当做位置参数按顺序从参数列表的左边开头往右匹配！），按照传参循序lis第一个值会传给默认参数c

## 4. 关键字参数：为了避免用户随意传参，提醒用户一定要输入的参数
###   关键字参数前面需要一个特殊分隔符*和位置参数及默认参数分隔开来，*后面的参数被视为关键字参数。
###   如果函数定义中已经有了一个*args参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了。



'''
 迭代器
'''


'''
列表推导式
'''
# 推导式（列表推导式、字典推导式、集合推导式）：Python的一种独有特性，可以从一个数据序列构建另一个新的数据序列的结构体。
# https://www.cnblogs.com/tkqasn/p/5977653.html

'''
if __name__ == '__main__':
'''
# __name__是所有模块都会有的一个内置属性：当你有个文件test.py，你作为模块导入其他文件__name__ = "test"
# 当文件以程序形式而不是模块形式被执行时，__name__ = "main", 将会执行这块函数定义的内容,即程序入口函数


'''导模块'''
# import 与 from...import

# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
