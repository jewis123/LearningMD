工作流程：
1.程序新增excel：excel表的第一行是列名，用中文即可，第一列为id，唯一性
2.策划编辑excel中的数据，然后使用工具导出，并在游戏中验证；

程序支持：
1.excel解析工具：excel 转 py；
2.解析当前目录下的所有excel文件；
3.代码打包成exe，减少环境依赖；

依赖库
argparse
xlrd


使用：
exe: 双击dist/main.exe使用
命令行：python mian.py -h 查看帮助
