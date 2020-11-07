### 如何创建的

通过`BuildPipeline.BuildAssetBundles`创建， 暂且不表，本节只关注AssetBundle的操作实现

### 源码探究

**AssetBundle	**

- AssetBundle缓存容器
  - PathContainer：scenePath—ABs
  - NameContainer：asset名字(不带后缀)—AssetInfo
  - FileContainer：？？—AssetInfo   
  - AssetLookupContainer:  objectID—AssetInfo
  - TypeLookupContainer: objectID— AssetInfo

- AssetBundle::Contains(name)

  【返回AB中是否包含指定Asset。】

  通过`GetPathRange`去按步骤寻找是否存在指定Asset

  1. 直接通过路径寻找
  2. 如果是精确路径直接返回
  3. 按照名字查找
  4. 按照扩展名查找

- AssetBundle::GetAllAssetNames()

  【返回AB中所有Asset(除场景AB)的名字】

  1. 如果是`streamed Scene AssetBundle`(场景ab)，则返回空（为啥？有别的接口）
  2. 将AB实例中的PathContainer缓存内容返回

- AssetBundle::GetAllScenePaths()

  【 专门返回AB中场景资产的路径】

  1. 如果不是场景AB就返回空
  2. 将AB实例中的PathContainer缓存内容返回

- AssetBundle::LoadAllAssets/ LoadAssetWithSubAssets

  【加载AB拥有的资产】

  1. 获取需要前置加载的资源（剔除重复后的列表）
  2. 加载前置资产
  3. 加载指定资产

- AssetBundle::Unload

  【卸载AB】

  1. 通过AssetBundleManager卸载AB（？）
     1. 找到所有AB所在场景
     2. 删除场景中用到的AB
  2. 。。。（下半部分在疑问板块解答处理）

**AssetBundleManager**

- 缓存容器
  1. HashToAssetBundle:  assetbundle name — assetbundle
  2. SceneNameToAssetBundleMap：sceneName — assetbundle(存在多对一的情况？为什么这么设计)

- RegisterAssetBundle: 

  【记录加载的AB对应的场景名】

**AssetBundleManifest**

记录AB对应资产清单依赖关系，并提供对外查询接口。对应UnityEngine下的同名类

**AssetBundleLoadAssetOperation**

​	UnityEngine.AssetBundleRequest 的 allAssets,asset两个属性就是通过这里返回的。

**AssetBundleLoadAssetUtility**

​	和上面一个类差不多，都属于工具类，这里对外提供了加载资产的一些操作

源码中还有诸多Operation和Utility结尾的类，都是工具类。

**AssetBundlePatching**

这个类的作用主要就是为了实现AB资源的替换。

这里面有个主要的函数：PatchAssetBundles。他会负责先卸载需要替换的AB资源，然后再异步加载替换的AB资源。

### 疑问

- AssetBundle::Transfer的目的是什么？

- AssetBundle::range 如何理解？

- FileContainer的键是什么？

- AssetBundleSaveAndLoadHelper在AssetBundleManager卸载AB后，剩余的操作在干嘛？

- AssetBundleManager在RegisterAssetBundle中给SceneNameToAssetBundleMap插值的方式会导致相同sceneName对应的AB被后续别的AB注册所覆盖，这是正确的需求吗，对应什么实际情况？

  

