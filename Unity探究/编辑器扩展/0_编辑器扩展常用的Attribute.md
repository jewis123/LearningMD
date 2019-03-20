##Attribute
Attribute是C#的功能，在Unity中可以使用Attribute来给变量和方法增加新的特性或者功能。先看一些能更改你脚本在Inspector上显示效果的Attribute，这篇文章也可以用作手册查看，不定期补充。

#####-变量级别。
1.**[Serializefield]**：如果想要给一个unity特有的私有变量手动赋值时使用。
2.**[Header("XXXX")]**：unity脚本中的变量在Inspector面板中时顺序排列的，如果想在特定的变量上加一个说明时可以使用。
3.**[HideInInspector]**：如果想让某个公有变量不在Inspector面板中显示时使用。
4.**[Range（float min,float max）]**：如果想让你的数值变量由滑动条改变时使用。
5.**[MultilineAttribute] / [TextArea]**：如果想让你的字符串成文可输入的多行文本时使用 。
6.**[Space(float)]**：在变量间设置间隔。
7.**[Tooltip("XXXX")]**：当鼠标悬停在变量名上时会出现XXX的提示。
8.**[FormerlySerializedAs("XXX")]**：总以XXX的命名来序列化变量，即使变量现有名称改变，也不会丢失序列化信息。

#####**-函数级别。**
   1.**[MenuItem ("XX/XXXX")]**：在Editor中创建菜单项，点击后执行该方法，可以利用该属性做很多扩展功能。 需要方法为static。你可以在菜单栏中找到你自定义的菜单项。
    2.**[ContextMenu(function name)]**：可以将函数添加到contextMenu下。就是组件右上角小齿轮那里。可以放参数Reset之类一键操作的函数。

#####**-类级别。**
   1.**[RequireComponent( typeof (XXX))]**：如果在写脚本的时候，需要XXX组件而不想手动添加时使用。
    2.**[AddComponentMenu("XX/XXXX")]**：加在脚本class程序块之上，意为将XXXX脚本放在XX的级联菜单下。在Inspector中点击AddComponent按钮就可以发现自定义的级联菜单
    3.**[DisallowMultipleComponent]**：可以避免在同一个物体上添加相同脚本。
    4.**[ExecuteInEditMode]**：使得脚本在Editor模式下也能执行。
    5.**[RequireComponent（typeof(XXX)）]**：当该脚本被添加到一个GameObject上的时候，如果这个GameObject不含有依赖的Component，会自动添加该Component。且该Componet不可被移除。
    6.**[SelectionBase]**：当你希望在点击子物体时在Hierarchy选中根物体时使用。
    7.**[CanEditMultipleObjects]** ：当你希望你的脚本能够被多选操作时使用。这需要引用UnityEditor命名空间。
    8.**[CustumEditor(typeof(XXX))]**：这可以使脚本转变成你的自定义的XXX组件。需要是你的脚本继承自Editor。
    
以上都是很常用的Attributes, 如需更多，看[Unity文档](https://docs.unity3d.com/ScriptReference/index.html)中的UnityEngine和UnityEditor类下的Attribute分类。