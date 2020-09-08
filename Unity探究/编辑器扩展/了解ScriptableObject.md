### 什么是ScriptableObject？

- 一种数据容器，与实例无关

### 能干什么用？

- 复用数据减少内存占用。相同实例对象共享数据。
- 作为配置文件
- 能够像普通资源一样管理，实现场景间共享、项目间重用。
- 结合其他标记语言，可以方便得实现读取转换。
- 作为代理对象，管理/执行一部分可配置逻辑，然后传递给MonoBehaviour进行调用。
- 配合编辑器扩展功能，能够自定义一些操作。很常用的。

### 特点

不能作为组件绑定在GameObject上，只能作为Asset保存。

### 如何使用

非常简单，只需要把平时的继承自MonoBehaviour改成ScriptableObject即可：

#### 基本使用

```C#
using UnityEngine;

[CreateAssetMenu(menuName="MySubMenue/Create MyScriptableObject ")]
public class MyScriptableObject : ScriptableObject
{
    public int someVariable;
}
```

#### 动态创建

```C#
ScriptableObject.CreateInstance<MyScriptableObject >();
```

#### 回调函数

OnEnable/OnDisable/OnDestroy

#### 生命周期

- 和其他资源一样
- 拥有实体（.asset/ab）：通过资源管理途径卸载/加载
- 动态生成：通过GC卸载；HideFlags.HideAndDontSave可避免被卸载回收。