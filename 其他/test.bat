@echo off


echo "hello"

:: 这里是注释。


call other.bat

::创建一个目录
md otherdir  

::重命名
ren otherdir anotherdir

::call another.bat

::输出文本内容
type text.txt


::删除文件
::del a.txt

pause
