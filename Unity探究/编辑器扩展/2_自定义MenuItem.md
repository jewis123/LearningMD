[TOC]



#### 介绍

Unity编辑器允许添加外观和行为与内置菜单相似的自定义菜单。这对于添加常用的功能非常有用，这些功能通常需要通过编辑器UI直接访问。在本文中，我将介绍如何创建Unity编辑器中的新菜单项，并尝试为每个描述的主题提供真实的示例用法。

#### Menu item得一般创建流程

> 1.引用UnityEditor命名空间
> 2.添加[MenuItem(XXX路径)]
> 3.创建静态方法（当点击menu item 后这个方法就会被调用）

长这样：
```
using UnityEngine;
using UnityEditor;
 
public class MenuItems
{
    [MenuItem("Tools/Clear PlayerPrefs")]   //会在菜单栏增加Tools选项卡
    private static void NewMenuOption()
    {
        PlayerPrefs.DeleteAll();
    }
}
```
当然了这里的MenuItem特性路径有几个内置好的情况
>* Assets ：item将会在 “Assets” 菜单下被找到, 或者在项目视图右击
>* Assets/Create ： items将被在“Assets/Create”下被找到
>* CONTEXT/xxxComponentName： items 将在组建面板上右击时被找到

#### 添加热键

 *    ’%‘ – CTRL
 *    ‘#’ – Shift
 *    ‘&’ – Alt
 *    ‘LEFT/RIGHT/UP/DOWN’ – 方向箭
 *    ’F1…F2‘ – F 键
 *    ‘HOME, END, PGUP, PGDN’
 *    注意：使用热键如果重叠将只能执行第一个调用
    长这样：
```
	[MenuItem("Tools/New Option %#a")]
    private static void NewMenuOption()
    {
        Debug.Log(1111);
    }

    // Add a new menu item with hotkey CTRL-G

    [MenuItem("Tools/Item %g")]
    private static void NewNestedOption()
    {
        Debug.Log(2222);
    }
```
![](https://upload-images.jianshu.io/upload_images/3806085-0144e439ca48b7a8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### menu item 第二个参数：验证
有些情况下，我们希望menu item 只在特定情况下能交互，这时我们需要enable/disable menu item。
这种情况下，要用validation，即验证。
validation方法是一种静态方法，需要满足如下条件：

> * 用menu attribute 修饰 
> * menu路径 必须和他要验证的menu相同 
> * 必须返回一个bool值来决定是否要激活 menu item
>   长这样：
```
	[MenuItem("Assets/ProcessTexture")]
    private static void DoSomethingWithTexture()
    {
        Debug.Log(" validation");
    }

    // 跟上第二个参数true，将静态方法设置成验证函数
    [MenuItem("Assets/ProcessTexture", true)]
    private static bool NewMenuOptionValidation()
    {
        // 设置什么情况下消失/显现(the menu item will be disabled otherwise).
        return Selection.activeObject.GetType() == typeof(Texture2D);
    }
```
#### menu item 第三个参数：优先级
可以给自定义的menu item设置优先级，让他显示在醒目的位置

```
[MenuItem("Assets/PriorityItem", false,100)]  //值越大越靠后
```



#### 相关类
**MenuCommand**
这个类可以传递上下文信息，可以用来修改组件数据

```
    [MenuItem("CONTEXT/Rigidbody/MassSet")]
    static void MassSet(MenuCommand command)
    {
        //这一句就是具体含义
        Rigidbody body = (Rigidbody)command.context;
        body.mass = 5;
        Debug.Log("Changed Rigidbody's Mass to " + body.mass + " from Context Menu...");
    }
```
**ContextMenuItem**
给自定义组件下的变量设置menu item，函数必须是非静态的
```
[ContextMenuItem("Randomize Name", "Randomize")]     //在面板属性条目上右击调出menu item
    public string Scenename;
private void Randomize()
    {
        Scenename = "Some Random Name";
    }
```
**ContextMenu**
自定义上下文菜单，函数是非静态的,用来设置组件变量是极好的

```
[ContextMenu("ContextMenu Func")]
    void DoSomething()
    {
        experience = 10000;
    }
```

详细参考[官方文档](https://unity3d.com/cn/learn/tutorials/topics/interface-essentials/unity-editor-extensions-menu-items?playlist=17117)

**注：**所有配套案例可在EditorExtensionDemo仓库中查看。

