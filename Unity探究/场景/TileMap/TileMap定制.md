### 简介

`Unity`的`TileMap`笔刷是可以自定义的，这样我们就能根据需求进行自定义了。而笔刷的用途其实就是创建对象到场景，所以可以针对创建的过程进行定制。

### 自定义笔刷

所有自定义笔刷都要继承自`GridBushBase`或其子类，这个类主要实现的就是调色盘上方六个工具回应的操作函数。通常需要复写的`method`有：

- `Paint`：创建`item`到指定`TileMap`层
- `Erase`：移除`TileMap`层上的`item`
- `FloodFill`：将选定区域填充满`item`
- `Rotate`:  旋转`Item`
- `Flip`: 翻转`item`

[全部虚函数](https://docs.unity3d.com/2018.4/Documentation/Manual/Tilemap-ScriptableBrushes-GridBrushBase.html)

#### 创建笔刷

创建资产：

​	笔刷实际上是`Unity`的一种`Asset`资源，所以我们可以创建笔刷实现资产复用。创建笔刷有两种方式。

- 右键`Create`
- 调色盘创建

创建实例：

​	通过调用`ScriptableObject.CreateInstance<(Your Brush Class>()`。

#### 定制笔刷编辑器

这个类主要就是调色盘下方笔刷面板的界面显示，在此可以接受用户配置，传递给笔刷类影响绘制逻辑。定制笔刷编辑器需要继承`GridBrushEditorBase`或其子类。

- `OnPaintInspectorGUI`: 提供显示笔刷的配置
- `OnSelectionInspectorGUI`：当选中格子时，绘制格子的配置面板
- `OnPaintSceneGUI`： 提供笔刷在`SceneView`中的行为
- `validTargets`:  定义笔刷可绘制图层

### 自定以瓦片

待补充，还是主要看官方[github 2d-extras](https://github.com/Unity-Technologies/2d-extras)库。

#### 使用特性描述笔刷

完成上述两布，那么自定义笔刷的功能已经完成了， 另外可以通过`[CustomGridBrush]`标签配置一些笔刷在调色盘笔刷列表的项：

- `HideAssetsInstance`: 是否隐藏笔刷实例在调色板窗口的笔刷列表显示
- `HideDefaultInstances` ：是否显示默认笔刷
- `DefaultBrush` ：是否设置为默认笔刷
- `DefaultName` ：设置笔刷名字

### 操作调色盘网格

首先我们要知道的是，调色盘在资产上表现为预制体附带一个asset文件，进入预制体编辑模式，我们看到实际上调色盘也是`Grid+TileMap`的形式。

所以，如果我们想要调色盘网格里程序化的添加内容的话，只需要拿到调色盘的`TileMap`，然后再调用SetTile相关的接口即可（理论上如此，但如果你真的这么做了会发现没起作用）。

在Hack入相关源代码之后发现，实际上的操作远比想想中的复杂。所以只能很苦逼的用反射完全仿写`GridPaintPaletteClipboard`中处理拖拽应用瓦片的代码。

### 问题

1. 笔刷下拉列表是如何收集所有笔刷的？

   `UnityEditor`程序集下有一个`GridPaletteBrushes`，这里面收集了所有`Brush`

2. 怎么理解Palette面板最底下的`Z Position`?

   这个命名比较有迷惑性，它其实是只有在斜45的的TileMap上才有效，为了处理斜45度的层级问题才产生的。其原理是向上偏移绘制一定高度。所以非斜45度的调色盘没必要去设置他。