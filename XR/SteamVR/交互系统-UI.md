### 提要

VR中的UI不同于我们常见的UI，它更加注重沉浸感，所以UI设计在VR中尤为重要。

#### 问题描述

HUD (head-up display)是非VR游戏中最常见的UI类型。  它有两个特点： 

1. HUD画面是离摄像机镜头最近的物体，其他物体都会被HUD挡住 
2. HUD在屏幕中位置是不变的，且很多组件在屏幕的边缘   

而这两点在VR中都是很难被接受的。首先，如果距离太近，会让用户的眼睛无法聚焦。其次，VR中的屏幕不是矩形的，边缘一般比较模糊，所以把UI放在边缘会看不清楚；而且如果位置还是固定的，不受视野控制，那就更不自然了 ———— 用户会因为看不清楚而本能地转头去看，而即使转头，它的位置还是在边缘。 

所以，在VR中使用3DUI来作为替代。

### SteamVR中的3DUI

SteamVR中需要将UI渲染模式设置为世界空间，又因为InteractiveSystem是基于**物理**的，也就是说想要做可交互UI要通过3D来实现，所以所有需要交互的对象都必须加上碰撞盒。

由于VR的输入特性，UI交互就涉及手柄操作，因此，VR中的UI设计是比较复杂的，首先要设计3DUI样式，其次要确定交互方式。

总结下，VR中的3DUI分为两种：平面形式和立体形式，但是都需要添加物理碰撞盒。立体UI一般通过手部交互，平面UI一般通过射线交互。

在Interactions_Example示例中，我们可以发现立体UI交互需要完成的几个步骤

- UI对象要加上Interactable组件（不光是UI对象，所有可交互对象都要加上这个组件，可以说这个组件是SteamVR交互系统的核心组件）
- UI Element组件（需要绑定事件函数），如果是平面型UI也可以直接向
- 另外UI对象添加一个子物体绑定Collider组件用于检测。
- 自定义的事件用于添加到UI Element槽中

**相关组件**

Interactable：负责交互

UI Element：负责UI事件，是基于手部的交互

**库**

调用 Valve.VR.InteractionSystem