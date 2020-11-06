- 查看设备： adb devices
- 查看启动进程的包名：adb shell am monitor
- 查看自己安装的app包名：adb shell pm list packages -3
- 查看正在运行的进程： adb shell ps | findstr [,进程名]
- 输出带时间的logcat日志到本地文件：adb logcat -v threadtime -> F:/logcat.txt



【连接夜神模拟器】

https://www.yeshen.com/faqs/H15tDZ6YW