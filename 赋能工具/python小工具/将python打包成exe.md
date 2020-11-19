### 背景
我们做的工具有时需要给不会用命令行的人用，所有打包成exe可以简化相关操作。

### 依赖库
PyInstaller 是一个十分有用的第三方库，可以用来打包 python 应用程序，打包完的程序就可以在没有安装 Python 解释器的机器上运行了。

安装：pip install pyinstaller 

使用：pyinstaller -F helloworld.py

其中，-F 表示打包成单独的 .exe 文件，这时生成的 .exe 文件会比较大，而且运行速度回较慢。仅仅一个 helloworld 程序，生成的文件就 5MB 大。

另外，使用 -i 还可以指定可执行文件的图标； -w 表示去掉控制台窗口，这在 GUI 界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！

PyInstaller 会对脚本进行解析，并做出如下动作：

1、在脚本目录生成 helloworld.spec 文件； 2、创建一个 build 目录； 3、写入一些日志文件和中间流程文件到 build 目录； 4、创建 dist 目录； 5、生成可执行文件到 dist 目录；