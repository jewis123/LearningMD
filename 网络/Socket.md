### 什么时是Socket

Socket是封装在TCP/IP层上的一个中间件，屏蔽了底层的复杂性。应用程序可以通过Socket来向网络发送请求或应答请求。它是支持TCP/IP协议的网络通信的基本操作单元。

- 服务器端
  · socket：建立服务器Socket实例
  · bind: 绑定IP和端口
  · listen: 开始监听端口
  · accept：接收客户端请求
  · read: 读取客户端传来的数据
  · write: 给客户端传递数据
  · close： 关闭Socket，结束通信
- 客户端
  · socket: 建立Socket实例
  · connect：向服务器发送建立连接请求
  · read : 读取服务器发来的数据
  · write: 向服务器发送数据
  · close: 关闭Sokect,结束通信



