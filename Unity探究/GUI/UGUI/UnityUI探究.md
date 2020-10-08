[TOC]

## UI的基本原理

#### 术语

- 画布(Canvas) 是以原生代码编写的Unity组件，它给Unity的渲染系统提供按层划分的几何系统，可以在其内部或其上层绘制其他几何形状。

画布负责将其内部的几何形状合并到批处理、生成合适的渲染指令并发送到Unity图形系统。这些操作都由原生C++代码完成，这被称为 **重新批处理(re batch) 或 批处理构建(batch build)** 。当一个画布被标记为含有需要重新批处理的几何形状时，称这个画布为 脏(dirty) 画布。

- 由 CanvasRenderer 组件向画布提供几何形状。

- 子画布(Sub-canvas) 是嵌套在其他画布组件内部的画布组件。子画布能够将其孩子节点与其父画布隔离开，***一个被标记为脏的子节点不会迫使其父画布重新构建几何内容，反之亦然***。有几种特殊情况会使上述情形失效，比如，*改变父画布导致子画布改变尺寸* 。

- Graphic 类是由Unity UI系统的C#库提供的基类，所有的向画布系统提供可绘制几何内容的UI系统C#类都继承它。大多数内置的UI系统绘图类都是通过 MaskableGraphic 子类实现的，这个子类实现了 IMaskable 接口，可以被遮罩。Drawable类的主要子类是 Image 和 Text ，它们能提供与其名称相对应的内容。

- Layout 组件控制RectTransform的尺寸和位置，它通常用于创建具有复杂布局并且内部组件需要相对尺寸或者相对位置的UI。Layout组件只依赖RectTransform并且只影响与其关联的RectTransform的属性。他们不依赖Graphic类，并且可以独立于UI系统的Graphic类使用。

Graphic和Layout组件都依赖 CanvasUpdateRegistry 类，该类没有在Unity编辑器中公开。这个类跟踪那些需要进行更新的Layout组件和Graphic组件集合，并在与其相关的画布调用 willRenderCanvases 事件时根据需要触发更新(update)。

Layout和Graphic组件的更新称为 重建(rebuild) 。关于重建过程的进一步详述会在下文中出现。

#### 渲染细节
当使用UI系统构建用户界面时，要时刻注意——***所有的几何形状都会在透明队列(Transparent queue)中绘制***。也就是说，由UI系统生成的几何形状都带有**Alpha混合**，从**后向前地绘制**。

- 站在性能地角度上，需要记住地一件重要的事情是，从多边形栅格化而得到的每个像素都会被采样，即使它们被其他不透明多边形完全遮盖。在移动设备上，这种高层重绘(overdraw)会迅速超出GPU的填充率(fill-rate)容量。

#### 批处理构建（batch building）过程（画布）
在批处理构建过程中，***画布合并用于表示UI元素的网格(mesh)***，生成合适的渲染指令发送到Unity的绘图管线。这一过程的**结果会被缓存并重用，直到画布被标记为脏画布**。脏画布会在画布的任一网格构成成员发送改变时产生。

画布所使用的网格是从附加到画布的CanvasRenderer组件集合中获取的，但其中不会包括子画布中的组件。

计算批处理需要根据深度(depth)对网格进行排序、检查网格的重叠、共享材质等情况。这个操作是多线程的，因此在不用的CPU架构上性能差异很大，尤其是在移动版Soc芯片（通常CPU核心数少）和现代桌面CPU（通常有4个或更多核心）之间。

#### 重建过程（Graphics）
***重建过程中进行了Graphic组件中的Layout和网格的重新计算***，这一过程在 CanvasUpdateRegistry 类中执行。CanvasUpdateRegistry是一个C#类，它的源代码可以在Unity’s Bitbucket上查看。

在 CanvasUpdateRegistry 值得注意的方法是 PerformUpdate 。这个方法会在画布组件调用 WillRenderCanvases 事件时被调用。这个事件每帧调用一次。

- PerformUpdate 会进行3步处理：

1. 脏Layout组件需要通过 ICanvasElement.Rebuild 方法重建它们的布局(layout)。

2. 所有已注册的裁剪组件（例如Mask）都需要剔除全部被裁减的组件，由ClippingRegistry.Cull方法完成。

3. 脏的Graphic组件需要重建它们的图形元素。

- Layout和Graphic的重建过程会被拆分成多个部分。Layout重建分3步完成（PreLayout，Layout和PostLayout），Graphic重建分2步完成（PreRender和LatePreRender）。

##### Layout重建
必须根据Layout层级顺序计算那些包含在Layout中的组件的位置和尺寸。在Game Object层级中，离根节点近的Layout有可能会改变嵌套在在它里面的Layout的位置和尺寸，所以它需要被先计算。

为此，UI系统依据Layout在层级中的深度对脏Layout列表中的Layout进行排序，高层的（例如，父Transform更少）的项会被移动到列表的前面。

排序后的Layout组件列表接下来要重建布局。这时被Layout组件控制的UI元素的位置和尺寸会发生改变。有关Layout如何影响每个元素的位置的详细叙述，请查看Unity手册中的[UI Auto Layout]( https://docs.unity3d.com/Packages/com.unity.ugui@1.0/manual/UIAutoLayout.html )。

##### Graphic重建
当Graphic组件重建时，UI系统将控制传递给ICanvasElement接口的Rebuild方法。Graphic类实现了这一方法并且在Rebuild过程的PreRender阶段执行两个不同的重建步骤。

如果顶点数据被标记为脏数据（例如，组件的RectTransform改变尺寸），网格会重建。
如果材质数据被标记为脏数据（例如，组件的材质或纹理改变），所附加的CanvasRenderer的材质会被更新。
Graphic重建不通过任何特定顺序的图形组件列表进行，也不需要进行任何排序操作。



## UI优化 填充率，画布和输入

#### 修复填充率问题

有两种操作能够减轻GPU片元(fragment)管线的压力：

- 降低片元着色器复杂度。具体内容请看下文的“UI着色器与低端设备”一节。
- 降低必须进行采样的像素数量。

因为UI着色器一般都会符合标准，所以最常见的问题是过多使用填充率。引起这种问题的最常见原因是，UI大量重叠并且/或者有多个UI元素占据屏幕的重要位置。这两种问题都能够导致极高的重绘。

为了缓解填充率的过渡使用和降低重绘，可以考虑下列的可能有用的补救措施。

#### 清除不可见UI

最简单的做法是直接禁用(disable)那些对玩家不可见的UI元素。最常见的情况是打开了带有不透明背景的全屏UI，在这种情况下，所有在全屏UI底层的UI元素都可以被禁用。

禁用UI元素的最简单的方式是禁用根GameObject或者含有UI元素的那个GameObject。还有一个替代方案是禁用画布。

最后，确保不要通过将UI元素的alpha值设为0这种方式来隐藏UI元素，因为这样仍然会将元素发送到GPU并且可能花费宝贵的渲染时间。如果UI元素不需要Graphic组件，可以直接将Graphic组件移除，这时射线仍然可以工作。

#### 简化UI结构

保证UI对象数量尽可能的少对于减少UI重建和渲染时间具有重要意义。尽可能多的进行烘焙，例如，不要通过混合GameObject来改变色调，应该使用材质属性代替。另外，不要仅把游戏对象当作文件夹使用（划分场景内容）。

> [?1]:原文：Try to bake things as much as you can. For example, don’t use a blended GameObject just to change the hue to an element, do this via material properties instead. Also, don’t create game objects acting like folders and having no other purpose than organizing your Scenes.

#### 禁用不可见的相机输出

如果打开了带有不透明背景的全屏UI，位于世界空间(world-space)的相机仍会渲染UI后面的标准3D场景。渲染器并不知道全屏UI会遮盖整个3D场景。

因此，在打开了全屏UI时，关闭被遮挡的世界空间相机，消除对3D世界的无用渲染，能够帮助降低GPU压力。

如果UI没有覆盖整个3D场景，可以将场景一次性渲染到纹理上然后使用这张贴图来取代持续渲染。这样没法看到3D场景中的动画内容，但大多数时候这中代价可以接受。

*注意*：如果画布被设为 *Screen Space - Overlay* ，那么它的绘制将与场景中的活动(active)相机数目无关。

#### 被大面积遮挡的相机

很多“全屏”UI实际上并没有遮挡整个3D世界，而是留下了一小块可见的世界空间。在这种情况下，仅将可见的这部分世界空间捕获到RenderTexture可能是最佳的做法。如果把可见的场景内容“缓存”到RenderTexture中，那么实际的世界空间相机就可以被禁用，然后将缓存的RenderTexture绘制到UI屏幕后方，来提供一个伪造的3D世界画面。

#### 基于组合的UI

设计师经常会将UI元素进行组合和分层最终创建一个整合的UI，这种做法很简单，容易迭代，但并不是一个好的做法，因为Unity的UI使用了透明渲染队列。

考虑这样一种情况，一个带有背景的简单UI，其中有一个带有文字的Button。因为透明队列中的对象会从后向前(back-to-front)排列，GPU必须先对背景纹理进行采样，然后对Button纹理进行采样，最后再对文本纹理进行采样，总共要采样3次。随着UI复杂度的增加，背景上会放置越来越多的装饰元素，采样次数就会快速增长。

如果发现有大型UI导致填充率瓶颈，最好的解决办法就是把那些装饰性/不变的元素合并到一张专门的UI精灵图(sprite)中，这样可以降低重叠元素的数量，不过这样做会增加工作量和纹理集大小。

通过创建专用精灵图来减少重叠元素的方法也可以用于四元素(sub-element)。比如，有一个商店页面，其中有个一滚动列表，列表中含有很多窗格显示商品，每个商品UI都有一个外框，一个背景，一些用于表示价格、名字以及其他信息的图标。商店UI需要一张背景图，但是由于商品会在商店的背景上滚动，所以没法将商品元素合并到商店背景纹理中。但是可以将外框、价格、名字和其他元素合并到商品的背景图中。这样做可能会节省很多填充率，具体取决于图标的尺寸和数量。

合并UI有几个缺点，专用的元素无法被重用，并且需要额外的美术资源。额外添加的大型纹理也可能导致内存开销显著增加，尤其是在UI纹理不能按需加载和卸载时。

#### UI着色器与低端设备

Unity UI系统所使用的内置着色器包含了对遮罩、裁剪以及其他很多复杂操作的支持。因为这些额外的复杂功能，在低端设备（例如iPhone 4）上UI着色器的性能要比更简单的Unity 2D着色器差很多。

如果为低端设备开发的应用用不到遮罩、裁剪等“奇特的”功能，可以创建自定义的着色器，来去除那些不需要的功能。

#### UI画布重建

要显示任何UI内容，UI系统都必须要为屏幕上的每个UI元素构建用于表示它们的几何结构。这个过程包括运行动态布局代码、生成用于表示UI中的文字的多边形、尽量多的将几何体合并到单个网格以降低DrawCall。这是个分多步完成的操作，在前面介绍了它的细节。

有两个导致画布重建性能问题的主要原因：

- 如果画布上需要绘制的UI元素数量很多，那么计算批处理会产生很大开销。因为对UI元素进行排序和分析的开销随UI元素数量增长的速度要大于线性增长。
- 如果画布被频繁的标记为脏画布，那么在刷新那些变化内容很少的画布时可能花费过多的时间。

随着画布上的元素数量的增长，这两种问题都会变得越来越严重。

*重要提示：在画布上无论有什么可绘制的UI元素发生了变化，画布都必须重新运行批处理构建过程。*这一过程会重新分析画布上的每个可绘制元素，无论它有没有发生变化。注意，“变化”是指任意的UI对象外观改变，包括将精灵图赋给SpriteRenderer、改变位置和缩放、将文本合并到网格等。

#### 子节点顺序

Unity中的UI从后向前进行构建，对象在Hierarchy中的顺序决定它们的排序顺序，先出现的对象会排在后出现的对象的后面。批处理过程会从上到下的遍历Hierarchy，收集所有使用相同材质、相同纹理并且没有中间层的对象。**“中间层”是指带有不同材质的绘图对象，它的边界与两个可另行批处理(otherwise-batchable)对象重叠并且位于两个可批处理对象之间。** *中间层会强制破坏本来的批处理* 。

- 例子： Canvs - A/A/A       绘制一次
- Canvas- A/B/A                   绘制三次

> [?2]:原文：An “intermediate layer” is a graphical object with a different material, whose bounding box overlaps two otherwise-batchable objects and is placed in the hierarchy between the two batchable objects.

在[Unity UI分析工具](https://unity3d.com/cn/learn/tutorials/topics/best-practices/unity-ui-profiling-tools)一节讨论过，UI Profiler和Frame Debugger能够检查UI中间层。可另行批处理(otherwise-drawable)是指一个可绘制对象将自身插入到两个可批处理对象之间的情况。

这种问题经常在文本(Text)和多个精灵图贴近时发生：文本的外边框不可见地和附近的精灵图重叠在了一起，因为很多文字符号的多边形是透明的。有两种方法可以解决这个问题：

- 重新排列可绘制元素，避免让不可批处理对象插入到可批处理对象之间，也就是说，将不可批处理对象移动到可批处理对象的上方或下方。
- 调整对象位置，清除不可见的重叠区域。

这两种操作都可以通过Unity编辑器的Frame Debugger来实现。只需要查看Frame Debugger中Draw Call的数量，就可以找到能够最小化因重叠元素而产生的Draw Call的元素位置和顺序。

#### 拆分画布

***不考虑非常复杂的UI时***，拆分画布通常是个不错的做法，无论是将元素移动到子画布还是兄弟画布。

当UI的特定部分必须独立于其他UI来控制绘制深度，保证永远在其他层的上面会下面时（例如，引导箭头），最后使用兄弟画布。

其他大多数情况时使用子画布更加方便，因为子画布能够从父画布继承显示设置。

虽然将UI细分到很多子画布看起来像是最佳的做法，但要记得，画布系统同样不会为不同画布中的元素合并批处理。设计高效UI需要在最小化重建开销和最小化无用批处理之间权衡。

#### 一般原则

因为画布会在其中的任意组件发生变化时进行重新批处理，所以最好将有用的(non-trivial)画布分成至少两部分。进一步将，最好将那些同时变化的元素放到同一画布上。例如，进度条和倒计时UI，它们都依靠相同的底层数据，因此会同时更新，所以它们应该放在同一画布上。

在一张画布上，放置所有不会发生变化的静态元素，例如背景和标题。它们只会在画布首次显示时进行一次批处理，之后便不再需要重新批出里。

在另一张画布上，放置所有动态元素——频繁发生变化的元素。这样可以确保这张画布重新批处理主要的脏元素。如果动态元素的数量增长到非常巨大，有必要再将动态元素分为频繁变化元素集（比如，进度条、计时器和动画）和偶尔变化元素集。

这样设计UI后，实践过程会比较困难，尤其是在将UI操控分装进预制体时。很多UI选择将复杂的控制分离到子画布中来取代细分画布。

在Unity 5.2中，大部分批处理代码都进行过重写，与Unity 4.0、5.0和5.1相比，性能有显著的提升。另外，在有不止一个内核的处理的的设备上，UI系统会把大部分处理过程转移到工作线程中。通常，Unity 5.2中不需要将UI细分到十几个画布中，很对UI只使用两三个画布就能在移动设备上具有良好的性能。

在这篇[博客](https://blogs.unity3d.com/cn/2015/09/07/making-the-ui-backend-faster/)中可以找到更多在Unity 5.2中进行的优化信息。

### Unity UI中的输入和射线

默认情况下，Unity使用[GraphicRaycaster](https://docs.unity3d.com/ScriptReference/UI.GraphicRaycaster.html)组件处理输入事件，例如触摸事件和鼠标悬停事件。通常由StandaloneInputManager组件处理输入，如其名称所描述的，StandaloneInputManager是一个“通用”的输入管理系统，鼠标和触摸都可以处理。

### 移动设备上不正确的鼠标输入检测（5.3）

在Unity 5.4之前，只要当前没有可用的触摸输入，每个附加了GraphicRaycaster组件的活动画布都会每帧执行一次射线投射来检测鼠标位置，而不管程序运行在哪种平台。即使是在没有鼠标的iOS和Android设备上，也会查询鼠标位置并尝试发现哪个UI在鼠标位置来判断是否需要发送悬停事件。

这样做是在浪费CPU时间，并且被证实消耗了Unity应用至少5%的CPU帧时间。

这一问题在Unity 5.4中得到了解决。 从5.4开始，没有鼠标的设备不会检测鼠标位置，并且不会执行不必要的射线检测。

如果正在使用Unity 5.4之前的版本，强烈建议为移动设备开发专用的输入管理类。可以简单的从Unity UI源代码中复制Unity的StandaloneInputManager类，然后注释掉对ProcessMouseEvent方法的所有调用。

### 射线优化

GraphicRaycaster的实现相当直接——遍历所有“Raycast Target”属性被设置为true的Graphic组件。对于每个RaycastTarget，Raycaster会执行一组测试。如果RaycastTarget通过了对其进行的所有测试，那么它会被加入到命中(hit)列表。

#### 射线实现细节

测试内容是：

- RaycastTarget是否是活动的、已启用和以绘制（比如，拥有几何结构）？
- 输入点是否位于RaycastTarget的RectTransform上？
- RaycastTarget是否带有[ICanvasRaycastFilter](https://docs.unity3d.com/ScriptReference/ICanvasRaycastFilter.html)组件，或者是否是ICanvasRaycastFilter的任意深度的子节点，并且RaycastFilter组件允许Raycast？

被命中RaycastTarget列表接下来会根据深度进行排序、过滤反面(reversed)目标，并过滤掉在相机后面渲染的元素（例如，在屏幕上不可见）。

如果GraphicRaycaster设置了相应的 *Blocking Objects* 属性，它还可能向3D或2D物理系统中投射射线。（在脚本中，这个属性名为[blockingObjects](https://docs.unity3d.com/ScriptReference/UI.GraphicRaycaster-blockingObjects.html)）。

如果启用了2D或3D的阻塞对象(blocking objects)，那么所有绘制在2D或3D对象之下的并且位于射线阻塞物理层(raycast-blocking Physics Layer)的RaycastTarget也都会从命中列表中移除。

最后，得到了射线返回的碰撞列表。

#### 射线优化提示

鉴于所有的RaycastTarget必须由GraphicRaycaster进行测试，最好只给那些必须接收鼠标事件的UI元素启用“Raycast Target”属性。RaycastTarget列表越短，需要遍历的层级内容就越少，每次Raycast就会越快。

对于拥有多个可绘制UI对象并且必须相应鼠标事件的UI控件，例如会同时改变背景和文字颜色的按钮，最好在这个UI控件的根节点放置单个RaycastTarget。当这个RaycastTarget收到鼠标事件时，它可以把事件转发给每个下属控件。

#### 层级深度和射线过滤

当搜索RaycastFilter时，每个GraphicRaycast都会遍历整个Transform层级，这一操作的开销随层级深度线性增长。在层级中找到的每个附加到Transform的组件都必须进行测试，来检测它们是否实现了ICanvasRaycastFilter，因此，这不是一个小开销的操作。

有几种标准UI组件使用了ICanvasRaycastFilter，例如[CanvasGroup](http://docs.unity3d.com/ScriptReference/CanvasGroup.html)、[Image](http://docs.unity3d.com/ScriptReference/UI.Image.html)、[Mask](http://docs.unity3d.com/ScriptReference/UI.Mask.html)和[RectMask2D](http://docs.unity3d.com/ScriptReference/UI.RectMask2D.html)，没办法简单地消除对这些组建的遍历。

#### 子画布和重写排序(OverrideSorting)属性

子画布中地[overrideSorting](https://docs.unity3d.com/ScriptReference/Canvas-overrideSorting.html)属性会导致GraphicRaycast测试停止遍历Transform层级。如果启用它不会引起排序或射线检测问题，那么应该用其减少射线检测的层级遍历开销。

#### 禁用画布

在显示或隐藏UI中不连续的部分时，常见的做法是在UI的根节点启用或禁用GameObject，这样可以确保被禁用的UI组件不会收到输入回调或Unity回调。

但是，这样做会导致画布丢弃它的VBO数据。重新启用画布需要画布（及其子画布）执行重建和重新批处理过程。如果这一操作很频繁，CPU占用可能会导致程序帧率低。

一个可行的解决办法是，将需要显示/隐藏的UI放置到它们专用的画布或子画布上，然后只启用或禁用这个画布组件。这样可以使UI的网格不进行绘制，但它们仍然会驻留在内存中，并且其原始批处理会被保留。进一步的，在这一UI层级中不会有[OnEnable](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnEnable.html)和[OnDisable](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnDisable.html)回调。

- 需要注意的是，这样做并不会禁用被隐藏的UI上的任何MonoBehaviour，这些MonoBehaviour仍然会收到Unity的生命周期回调，比如Update。

如果要避免这一问题，以这种方式实现隐藏的UI上的MonoBehaviour不应该直接实现Unity的生命周期回调，而应该去接收它们的UI根节点的自定义的“CallbackManager”的回调。当UI被显示和隐藏是，这个“CallbackManager”应该收到通知，并决定是否传播生命周期事件。

####分配事件相机

如果Canvas的渲染模式为 *World Space* 或者 *Screen Space - Camera* 并且使用了Unity内置的InputManager，一定要为其设置合适的EventManager/RenderCamera属性。在脚本中，这两个属性都通过[worldCamera](https://docs.unity3d.com/ScriptReference/Canvas-worldCamera.html)属性来设置。

如果没有设置这个属性，UI系统会通过在Tag为Main Camera的GameObject上寻找Camera组件来查找主相机。这一查找操作在每个World Space或Camera Space画布上至少发生一次。由于[ GameObject.FindWithTag](https://docs.unity3d.com/ScriptReference/GameObject.FindWithTag.html)的查找速度很慢，强烈建议在初始化时为World Space和Camera Space画布设置相机。

在Overlay画布上不存在这一问题。

#### UGUI源码

https://bitbucket.org/Unity-Technologies/ui/

可以修改UI系统的C#源代码并编译成DLL覆盖Unity中附带的UI系统DLL来实现自定义优化内容。