##  什么是Addressbable?

- 可以替代`AssetBundle`的高阶资源管理系统，但是它是基于`AssetBundle`的更上层。
- 将资源管理交给系统自动处理
- 本地或异地都可以追踪
- 更加可控的内存管理
- 给资源添加信标（`Address`），使系统可以找到资源（先扫描本地再扫描远端）
- 可以进行多服打包测试
- 可以直接通过资产名加载
- 可以查询物件位置
- 系统自己处理资源关联性
- 可以自定义资产Build流程
- 可以将整个场景作为Addressable资源，加载的时候，会下载所有关联资源到本地。

## 使用Addressable

### Instantiate的问题

- 同步执行，线程阻塞
- 资源需要已在本地

### Addressable怎么处理

- 使用`InstantiateAsync`异步实例化
- 资产物件对象类型变成了`AssetReference`
- 使用`LoadAssetAsync`异步加载资源，对资源所在位置不做要求；通过回调确认加载完毕

### Lable

- 满足一次性加载同类资源的需求
- 通过Lable获取资产清单，然后分类加载

### 处理资产替换

系统可以自动分析替换差异，然后打出差异包

### 性能分析

通过Addressaable Profiler可以检查资产加/卸载管理，Fps等情况。

### 投入Addressable怀抱

### 其他资料

[官方教程](https://github.com/Unity-Technologies/AddressableAssetsWebinar)

https://www.jianshu.com/p/e79b2eef97bf