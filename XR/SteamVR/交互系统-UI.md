#### 提要

SteamVR中的UI交互似乎需要UI渲染模式设置为世界空间，因为InteractiveSystem是基于物理的，所以所有需要交互的对象都必须加上碰撞盒。

在Interactions_Example示例中，我们可以发现UI交互需要完成的几个步骤

- UI对象要加上Interactable组件（不光是UI对象，所有可交互对象都要加上这个组件，可以说这个组件是SteamVR交互系统的核心组件）
- UI Element组件（需要绑定事件函数）
- 另外UI对象添加一个子物体绑定Collider组件用于检测。

**相关组件**

Interactable

UI Element

**库**

调用 Valve.VR.InteractionSystem