## **渲染架构**

根据SRP工作流进行定制化，主要工作为一下几块：

\- 细分渲染阶段
\- 定制Pass（渲染指令的封装，便于重用）
\- 封装Pass装填流程（组合pass，达到不同的相机渲染效果）
\- 封装Pass渲染流程（对接Render流程，逐个调用pass的渲染）

## **细分渲染阶段**

在盗墓中，渲染关键阶段的划分非常的细致，可以总结流程如下：

- BeginFrameRendering
- 开始逐相机渲染
  - BeginCameraRendering
  - EmitWorldGeometryForSceneView（将世界场景中的UI以透明对象形式提交上下文, 编辑器模式下方便预览效果）
  - Cull（执行剔除）
  - Setup（pass排队)
  - 开始渲染各pass
    - 设置各种settings结构体
    - ExecuteCommandBuffer
    - DrawRenderers
- Draw Default Pipeline (用于兼容管线不支持的着色器Pass类型)
- Submit （提交管线执行渲染事务）



## **自定义Pass**

使得渲染指令代码的重用性更高。

![](img\renderUIpass.png)



## **封装Pass装填流程**

通过不同的pass组合方式，形成不同的相机渲染功能。增加灵活性。

比如DMM中默认管线渲染顺序是这么设定的：

- shadow pass
- 一系列数据准备
- 非透明Pass渲染
- 天空盒渲染
- 透明渲染

如果有另一个须有不渲染天空盒，就可以创建一个新类，把不用的pass移除即可。

![](img\RenderSetup.png)