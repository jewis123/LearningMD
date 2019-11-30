### import时python内部做了什么

当执行<u> from package import moudel as mymoudel</u>  导入命令时，python解释器会查找pacakage这个包的moudel模块，并将模块作为mymoudel导入到当前命名空间。所以import语句主要做了两件事：

- 查找相应的模块
- 加载模块到当前命名空间

#### 如何查找模块

在import第一阶段，主要完成了查找要引入模块的功能，过程如下：

1. 检查sys.modules（保存了之前import的类库缓存），如果模块被找到，则到第二步
2. 检查sys.meta_path。meta_path是一个list，里面保存了一些finder对象，如果找到该模块的话，就会返回一个finder对象。
3. 检查一些隐式对象，不同的python实现有不同的隐式finder，但是都会有sys.path.hooks,sys.path_importer_cache以及sys.path
4. 如果上两步都没找到，就抛出ImportError

详细：<https://github.com/Liuchang0812/slides/tree/master/pycon2015cn>

