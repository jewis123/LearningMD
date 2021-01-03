### 介绍

在开始学习SRP之前首要对其进行[了解](https://www.cnblogs.com/Jaysonhome/p/12900808.html)：

SRP是Unity提供的可编程渲染管线，其中包含两套模板：URP，HDRP。相较于原始的BuiltIn渲染管线，他们拥有更加灵活（在C#侧我们能够定制整个渲染流程）、轻便的特性（不需要兼容不相干的平台），同时更能够面向未来。

#### 问题先行

- 如何控制SRP渲染流程？

### 从代码层面了解SRP工作流

srp是一种渲染管线，它继承自RenderPipline。同时需要创建出资产实例，然后在`ProjectSetting-Graphics`中指定管线资产。这样就能去执行SRP的渲染循环了。

渲染循环的入口是抽象函数`Render`

```C#
protected abstract void Render(ScriptableRenderContext context, Camera[] cameras);
```

**Context**

函数中的`Context`是上下文的意思，可以理解为持有一次渲染流程细节的对象，同时也起到一个串联注入自定义内容与渲染流程的作用。

> As a user you build up a list of commands and then execute them. The object that you use to build up these commands is called the [‘ScriptableRenderContext’](https://docs.unity3d.com/ScriptReference/Experimental.Rendering.ScriptableRenderContext.html). When you have populated the context with operations, then you can call ‘Submit’ to submit all the queued up draw calls.

![image-20210103112841286](img\ScriptableRenderContext.png)

**Command Buffer**

`SRP`的渲染是延迟执行的，它会等到**收集好所有的渲染指令**并执行提交（给gpu渲染），才会实际地去渲染内容。这就需要有一个命令缓冲（CommandBuffer）去缓存各种自定义地渲染命令。然后通过`Context.ExecuteCommandBuffer`交给渲染上下文（在上下文`Submit`的时候，交付渲染）。

由于每一帧渲染得不受上一帧影响，所以缓冲指令交付上下文后，需要清理一下`CommandBuffer`中的指令以及渲染目标。

![](img\微信图片_20210103130347.jpg)

![](img\微信图片_20210103130249.jpg)

![](img\微信图片_20210103130326.jpg)

`CommandBuffer`还有一个作用就是给帧调试器进行采样，用于在帧调试过程中展示所采样的渲染状态。

**相机，剔除**

按序渲染相机内容是RP的责任，相机看不见的内容就会被剔除(视锥剔除、遮挡剔除)。结构体([ScriptableCullingParameter](https://docs.unity3d.com/2019.4/Documentation/ScriptReference/Rendering.ScriptableCullingParameters.html))定义了什么内容需要被剔除。通过`Camera.TryGetCullingParameters`可以把这个结构体拿出来，再交付上下文去执行剔除，最终获得一个`CullingResults`，结合对应相机，上下文通过`DrawRenderers`函数去绘制剔除剩下的内容。

![](img\微信截图_20210103131205.png)

>out处通过内联变量声明将变量指向内存堆栈，通过ref 去修改引用内容。这能够避免创建大结构体的副本，以此避免不必要的内存开销。

**绘制几何**

在调用上下文`DrawRenderers`函数前会实例化两个设置（DrawingSettings, FilteringSettings)。以下图为例，设置渲染队列中只渲染非透明物体、渲染排序采用默认非透明排序、并采用了前向渲染pass。

![](img\微信截图_20210103133521.png)

![微信截图_20210103133539](img\微信截图_20210103133539.png)

**总结渲染正确顺序**

- EmitWorldGeometryForSceneView
- Cull
- Setup
- DrawRenderers
  - 不透明对象
  - 天空盒
  - 透明对象
  - Gizmos
- Draw Default Pipeline (用于兼容管线不支持的着色器Pass类型)
- Execut Command Buffer
- Clear Command Buffer
- Submit

### SRP Batcher: 加速渲染

**传统的渲染工作流：**

![](img\SRPBatch.png)

在内部渲染循环中，当检测到新材质时，CPU会收集所有属性并在GPU内存中设置不同的常量缓冲区。GPU缓冲区的数量取决于Shader如何声明其CBUFFER。

**新的SRP：**

低级渲染循环可以使材质数据持久保存在GPU内存中。如果Material内容不变，则无需设置缓冲区并将其上传到GPU。另外，有了专用的代码路径来快速更新大型GPU缓冲区中的内置引擎属性。

![SRP-Batcher-OFF](img\SRP-Batcher-OFF.png)

在这里，CPU仅处理标记为对象矩阵转换的内置引擎属性。所有材料在GPU内存中都有持久的CBUFFER，可以随时使用。

```c#
///运行时打开batcher功能
GraphicsSettings.useScriptableRenderPipelineBatching = true;

///绘制时给DrawingSettings设置标记
DrawRenderFlags.EnableDynamicBatching
```

### 扩展阅读

[Unity SRP Docs](https://blogs.unity3d.com/2018/01/31/srp-overview/)

[srp tutor](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIxMzgzMzQxOA==&action=getalbum&album_id=1448409828501848064&scene=173&from_msgid=2247487543&from_itemidx=1&count=3&uin=&key=&devicetype=Windows+10+x64&version=63010029&lang=zh_CN&ascene=0&fontgear=2)

[srp batcher](https://blogs.unity3d.com/2019/02/28/srp-batcher-speed-up-your-rendering/)