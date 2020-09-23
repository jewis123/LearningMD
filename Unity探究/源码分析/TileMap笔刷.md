### 简介

Unity的TileMap笔刷是可以自定义的，这样我们就能根据需求进行自定义了。而笔刷的用途其实就是创建对象到场景，所以可以针对创建的过程进行定制。

所有自定义笔刷都要继承自`GridBushBase`或其子类，通常需要复写的`method`有：

- Paint：创建`item`到指定`TileMap`层
- Erase：移除`TileMap`层上的`item`
- FloodFill：将选定区域填充满`item`
- Rotate:  旋转`Item`
- Flip: 翻转`item`

### 创建笔刷

笔刷实际上是Unity的一种Asset资源，所以我们可以创建笔刷实现复用。创建笔刷有两种方式。

- 右键Create
- 调色盘创建

上述两种本质上都是通过调用`ScriptableObject.CreateInstance<(Your Brush Class>()`实现创建的。

