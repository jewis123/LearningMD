### 用到的库

目前主流的是argparse。getopt，optparse这两个库因为其复杂的使用方法都被淘汰了。

优点：声明参数简单，能能自动生成帮助和使用手册，并在用户输入无效参数时发出报错信息。

### 使用argparse

- 在使用该库功前首先要实例化ArgumentParser。ArgumentParser有一系列参数来描述对象信息。

- 调用add_argument，增加一个参数声明。有一系列参数来指定参数用途。
- 调用 parse_args()，解析参数。一般没有参数，通过命令行读取参数列表。

### 实例

```python
def parseArg():
	'''
	解析命令行参数
	:return: 参数列表
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument('infile', type = str, help= u'待解析的excel')
	parser.add_argument('-idx',dest = 'idx',type = int, help= u'excel页签索引') #可选属性
	parser.add_argument('outfile', type = str, help= u'输出文件')
	args = parser.parse_args()
	return args
	
if __name__ == '__main__':
	args = parseArg()
	infile = args.infile
	if not infile:
		print ('[ERROR]:EMPTY IN FILE PATH!')
	index = args.idx if args.idx else 0
	outfile = args.outfile
	if not outfile:
		print('[ERROR]:EMPTY OUT FILE PATH!')
	print(infile, outfile, index)
```

### 官方文档

https://docs.python.org/zh-cn/3/library/argparse.html#argumentparser-objects

