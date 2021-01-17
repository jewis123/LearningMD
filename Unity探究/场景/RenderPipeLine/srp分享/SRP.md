[toc]

#### 问题先行

- SRP的存在意义是什么？
- 如何控制SRP渲染流程？
- 其他不同之处？

### 介绍

先来看下[Unity官方词条](file:///D:/UnityEditor/2019.4.6f1/Editor/Data/Documentation/en/Manual/scriptable-render-pipeline-introduction.html)怎么说的：

​	SRP是Unity提供的一个API层，让开发者能够C#侧安排和配置渲染指令，然后通过SRP提交到Unity底层的渲染架构，有渲染架构再调用图形API进行渲染。

SRP是Unity提供的可编程渲染管线，其中包含两套模板：URP，HDRP。相较于原始的BuiltIn渲染管线，他们拥有更加灵活（在C#侧我们能够定制整个渲染流程）、轻便的特性（不需要兼容不相干的平台），同时更能够面向未来。

### 从代码层面了解SRP工作流

srp是一种渲染管线，它继承自RenderPipline。同时需要创建出资产实例，然后在`ProjectSetting-Graphics`中指定管线资产。这样就能去执行SRP的渲染循环了。

渲染循环的入口是抽象函数`Render`

```C#
protected abstract void Render(ScriptableRenderContext context, Camera[] cameras);
```

**Context**

函数中的`Context`是上下文的意思，可以理解为连接C#自定义内容和Unity底层图形架构的桥梁。

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

值得注意的是，剔除阶段不光只剔除物体，灯光也是在剔除考虑范围内的。如果可见光不存在（即灯光全被剔除的情况下），又去设置灯光索引是会导致Unity崩溃的。

**绘制几何**

在调用上下文`DrawRenderers`函数前会实例化两个设置（DrawingSettings, FilteringSettings)。以下图为例，设置渲染队列中只渲染非透明物体、渲染排序采用默认非透明排序、并只渲染前向光照的pass。

![](img\微信截图_20210103133521.png)

![微信截图_20210103133539](img\微信截图_20210103133539.png)

**最基础的一帧渲染**

![](img\最基础的一帧渲染.png)

**一帧内可细分的渲染顺序**

- BeginFrameRendering
- 开始逐相机渲染
  - BeginCameraRendering
  - EmitWorldGeometryForSceneView（将世界场景中的UI以透明对象形式提交上下文, 编辑器模式下方便预览效果）
  - Cull（执行剔除）
  - Setup（pass排队)
  - 开始渲染各pass
    - BeginPassRendering
    - DrawRenderers
  - Draw Default Pipeline (用于兼容管线不支持的着色器Pass类型)
  - Submit （提交管线执行渲染事务）

### 源码初窥

**上下文ExecuteCommandBuffer是立马执行吗？**

不是的。从源码中看到，其实是把CommandBuffer生成一份拷贝，然后加标签并入队。

![](img\ExecuteCommandBuffer.png)

**上下文DrawRenderers是立马执行吗？**

不是的。从源码中看到，指令也是被加标签后入队了。

![](img\DrawRenderers.png)

**上下文Submit之后，Unity做了什么？**

submit之后正式进入SRP渲染循环。说白了就是把之前记得流水账跑一边。

具体步骤如下：

- 准备好剔除结果中对象的依赖及数据
- 逐条执行指令队列
- 清理各种队列，缓存，小块内存分配器

**Unity底层的渲染架构是怎样的？**

- GfxDeviceClient,GfxDevice
- GfxDeviceWorker(多线程使用)

在单线程的情况下，主线程会运行一个GfxDeviceClient对象(继承自GfxDevice)，来管理渲染指令，然后提交给实际的图形API对应的GfxDevice派生类（比如GfxDeviceGLES）来实际执行渲染。

多线程情况下，GfxDeviceClient不会提交渲染指令到图形设备执行渲染，而仅仅只是维护一个ring buffer（ThreadedStreamBuffer）来缓存中间指令队列；由渲染线程GfxDeviceWorker从ring buffer中取出中间指令，然后再转交图形设备进行渲染。

**在多线程渲染下为什么要加入ring buffer机制**

两个线程之间交互必须要数据传递是线程安全的， 不能出现一个线程还没写完，另一个线程就开始读取的情况

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

### 其他不同之处

**着色器程序**

`SRP`的着色器采用`HLSL`编写。和`GLSL`最大的区别在于，它不会隐式执行任何操作，避免底层默认执行一些老旧操作。

另外，`hlsl`的`shader`代码写法上也有少许不同，通常把顶点函数和片段函数放在`hlsl`后缀的文件内，然后在shader中`#include`该文件。这样的好处是能够复用`pass`代码了，同时能够控制`pass`的执行顺序。

因为，SRP 采用了新的shader格式，所以需要对原先的shader pass进行兼容，不然就会在渲染时被忽略。

**灯光**

- Unity的默认管线针对每个对象在单独的通道中渲染每个灯光。轻量级管线针对每个对象在一次通道中渲染所有灯光。HD管线使用延迟渲染，该渲染将渲染所有对象的表面数据，然后每光源渲染一遍。
- 灯光强度在默认情况下依旧是伽马空间下的值，但是可以通过配置`GraphicsSettings.lightsUseLinearIntensity`将其设置在线性空间。
- 因为srp渲染不限制灯光数量，所以需要我们自己注意灯光索引是否越界。

### 扩展阅读

[Unity SRP Docs](https://blogs.unity3d.com/2018/01/31/srp-overview/)

[srp tutor](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzIxMzgzMzQxOA==&action=getalbum&album_id=1448409828501848064&scene=173&from_msgid=2247487543&from_itemidx=1&count=3&uin=&key=&devicetype=Windows+10+x64&version=63010029&lang=zh_CN&ascene=0&fontgear=2)

[srp batcher](https://blogs.unity3d.com/2019/02/28/srp-batcher-speed-up-your-rendering/)