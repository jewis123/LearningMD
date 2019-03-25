#### 提要

Teleport是交互系统中的一个重要部分，用来实现瞬移，一般和手柄上的触摸板组合使用。常用的操作是通过触摸板（或者手柄的移动）获取方向，按下触摸板显示瞬移光标，放开触摸板执行瞬移。另外，瞬移范围可以是区域型的也可以是点型。

#### 相关组件

- Teleport：实现瞬移的核心组件。
- TeleportArc：用来显示瞬移定位抛物线，基于Collider的射线检测。
- TeleportArea：用来指定可瞬移区域。
- TeleportPoint：用来指定可瞬移点。
- IgnoreTeleportTrace：添加到有Collider组件的物体上会让瞬移抛物线透过它。
- AllowTeleportWhileAttachedToHand：玩家抓取带有这个组件的物体时会执行瞬移。

