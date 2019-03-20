[TOC]

### 安装

- 硬件安装

​       推荐B站观看。

- 软件安装

  软件需要装Steam以及SteamVR套件。通过包装盒里的U盘可以快速安装。

  这里需要注意的是，我们要先把硬件设备插上电脑，然后再安装软件，否则可能会出现不可知问题。

  在安装软件的过程中，SteamVR会把房间设置也一并设置掉，所以要先提前准备好空间。当然也可以先跳过房间设置。

- 插件安装

  这里我们的环境为Unity3D，在AssetStore下载SteamVR即可。商店中还有例如Vive Input Utility 或者 VRTK之类的都是辅助插件，如果你下的是SteamVR v2.0+那么你可以不用那些了。

  也可到github release页下载：https://github.com/ValveSoftware/steamvr_unity_plugin/releases

- 导入插件

  从商店导入插件后，会有弹窗让你初始化设置，这里用它推荐的就好，后续有需求可以通过菜单栏进入插件窗口修改。打开Steam Input窗口，点击Sava and Generate。生成输入代码。

  一切都没问题后，可以打开InteractionSystem/Sample/InteractionException场景熟悉VIVE可实现的交互操作。

### 目录结构（部分）

```
SteamVR
    /*这个目录下的脚本都是用来定制SteamVR插件中某些脚本在Unity中的Inspector界面及功能的*/
    ——Editor　　　　　　　　　　　　　
        /*定制SteamVR_Camera.cs这个脚本在Inspector中的显示效果*/
        SteamVR_Editor.cs
        
        /*定制SteamVR_RenderModel.cs脚本在Inspector中的功能*/
        SteamVR_RenderModelEditor.cs
       
        /*上面提到的弹出的SteamVR_Settings对话框里面的选项就在这儿定制*/
        SteamVR_Settings.cs　
      
        /*定制SteamVR_SkyBox.cs在Inspector中显示的属性*/           
        SteamVR_SkyboxEditor.cs　
        
        /*用来检查插件的更新*/　　
        SteamVR_Update.cs　
       
    /*这个文件夹下面放着一些工具脚本*/　　　　　 　　
    ——Extras　　　　
        /*这个脚本用来检测物体是否被用户所凝视*/　　　　　　　　　
        SteamVR_GazeTracker.cs 　
        
        /*通过手柄指向来产生一条激光束*/       
        SteamVR_LeaserPointer.cs　　
        
        /*用来瞬移的脚本*/
        SteamVR_Teleporter.cs　　
        
        /*示例场景中扔物体的脚本*/
        SteamVR_TestThrow.cs　　　　
        
        /*示例场景中跟踪相机的脚本*/
        SteamVR_TestTrackedCamera.cs　　
        
        /*控制器(手柄)集成脚本*/
        SteamVR_trackedController.cs　
        
    /*存放实现交互的底层代码*/
    ——Input
      /*存放事件脚本，使Vive能与UI交互*/
     ——BehaviourUnityEvents
     /*存放按键绑定时的一系列自定义窗口属性绘制器*/
     ——Editor
     /*存放默认绑定信息*/
     ——ExampleJSon
    
    /*存放Vive交互的示例文件夹，在这里可以浏览到最常用的交互方式，以及一个总场景*/
    ——InterationSystem
    
    /*存放Steam设置信息，按键绑定信息，Shader，外部摄像机等资源*/
    ——Resources
    
    /*自动生成的文件夹，用来与OpenVR交互*/
    ——Plugins
         /*SteamVR C#调用openvr底层c++的接口,自动生成**/
         openvr_api
        
    /*存放SteamVR预制体*/　　
    ——Prefabs
        /*相机预制体*/　
        [CameraRig]
        /*状态相关的overlay显示预制体*/　
        [Status]
        /*SteamVR_Render预制体*/　
        [SteamVR]
    /*一些自带的shader*/　
    ——Resources
    ——Scenes
    /*SteamVR核心脚本*/　
    ——Scripts
        /*SteamVR的封装类*/
        SteamVR.cs
        /*SteamVR的核心相机类*/
        SteamVR_Camera.cs
        /*SteamVR相机翻转*/
        SteamVR_CameraFlip.cs
        /*SteamVR相机网格隐藏*/
        SteamVR_CameraMask.cs
        /*控制器封装类*/
        SteamVR_Controller.cs
        /*控制器管理类*/
        SteamVR_ControllerManager.cs
        /*声音控制类*/
        SteamVR_Ears.cs
        /*外部相机*/
        SteamVR_ExternalCamera.cs
        /*场景进行渐显或者渐隐的类*/
        SteamVR_Fade.cs
        /*跟踪设备的扫描范围*/
        SteamVR_Frustum.cs
        /*绘制pc上的伴随窗口*/
        SteamVR_GameView.cs
        /*关节反身运动*/
        SteamVR_IK.cs
        /*场景切换类*/
        SteamVR_LoadLevel.cs
        /*菜单类*/
        SteamVR_Menu.cs
        /*overly封装类*/
        SteamVR_Overlay.cs
        /*运动区域*/
        SteamVR_PlayArea.cs
        /*Vive渲染流程控制的核心类*/
        SteamVR_Render.cs
        /*设置天空盒*/
        SteamVR_Skybox.cs
        /*做球形投影的类*/
        SteamVR_SphericalProjection.cs
        /*通过overlay显示统计信息*/
        SteamVR_Stats.cs
        /*根据不同状态渐变显示不同的信息*/
        SteamVR_Status.cs
        /*根据不同状态渐变显示不同文本信息*/
        SteamVR_StatusText.cs
        /*控制器测试脚本*/
        SteamVR_TestController.cs
        /*头盔上的前置相机*/
        SteamVR_TrackedCamera.cs
        /*跟踪设备管理类*/
        SteamVR_TrackedObject.cs
        /*5.x版本以前更新设备位置的脚本*/
        SteamVR_UpdatePoses.cs
        /*工具类，包括事件系统，Transform等等*/
        SteamVR_Utils.cs

```

### Vive的渲染流程

**渲染循环**

SteamVR_Render.cs是SteamVR图形渲染的核心，该类位于Scripts文件夹中。观察它的OnEnable函数，我们发现Vive在启动渲染时做了这么几件事：

- 启动渲染
- 注册监听
- 获取头盔实例
- 初始化截屏类型

在渲染协程（RenderLoop）中，我们可以发现，VR渲染是在每一帧的最后时刻渲染的，主要是为了*等待所有相机和GUI都渲染完*。总的流程是：**①等待相机和GUI的渲染完成**->**②设置跟踪空间**->**③获取设备位置，通知更新**->**④渲染外部相机**->**⑤渲染左右眼**

![](https://img-blog.csdn.net/20160913194816077)

**左右眼渲染**

通过将VR眼睛的位置和旋转角度传递给相机，将SteamVR_Camera中的纹理设置为实际渲染相机的纹理，然后在渲染左右眼时分别把另外眼睛的mask去掉，最后调用相机渲染。到这里，我们就知道原来VIVE是将一个相机上的图像变形后分别显示再左右眼的显示屏上的。

### 最核心的预制体

- **[CameraRig]预制体**
- **[SteamVR]预制体**
- **[Status]预制体**

在SteamVR插件的Prefabs文件夹下面有三个预制体，CameraRig是相机预制体，使用时直接将这个预制相机作为主相机拖入场景中，我们就能以第一人称看到VR头盔里面的内容。Status是通过overlay显示一些状态信息的预制体。SteamVR是渲染核心预制体，不需要手动添加，会自动创建。

**[Camerarig]**

我们可以看到，在Camerarig下面有一个左右手柄的Controller和一个头部的Camera 。

在手柄Controller和头部的Camera上都有一个**Steam VR_Behaviour_Pose**脚本，此组件简化了Pose操作的使用。将其添加到游戏对象将自动设置该变换的位置和每次更新的旋转以匹配姿势。

在Colltroller对象下有一个Model对象挂了SteamVR_RenderModel组件。

- index：是设备索引，系统自动分配。
- ModelOverride：控制器模型重载，显示不同模型
- Shader：用于模型着色器
- Verbose ：将输出调试日志以告诉您脚本发生了什么
- Create Components：为可用的每个组件创建单独的GameObject。（不明白什么意思）
- Update Dynamically：将各个组件与其物理对应物一起移动。（不明白什么意思）

SteamVR_RenderModel组件需要与将设置其索引的内容放在同一个游戏对象上。在[CameraRig]预制件中，这由SteamVR_Behaviour_Pose脚本完成。

**[SteamVR]**

在【SteamVR、这个预制体只有Stean VR_Render这一个脚本，这个脚本在之前已经介绍了。这个预制体是必须在项目中添加的，即使不手动添加也会自动添加。 

**[Status]**

他下面有两个子物体：_Stats,Overlay

- _Stats：这个是显示统计信息的一个组件（目前仅显示帧率和丢帧数）。它上面还有一个Camera，通过它将GUIText渲染到overlay的纹理上，通过overlay将文字信息显示出来。它的显示效果如下图 
- **Overlay**：这个控件的作用是是一个2D的UI界面叠加到场景上面显示出来

### 辅助类

在Extras目录下，我们能看到SteamVR提供了一些辅助类：凝视追踪、射线指示、扔东西测试、相机追踪测试。同时还包含一些相应的场景。

### 输入系统

SteamVR插件的核心是Actions。SteamVR将Actions分为6种不同类型的输入和一种输出类型：

- Boolean - true or false
- Single - 单个模拟值
- Vector2 - 两个模拟值
- Vector3 - 三个模拟值
- Pose - 位置, 旋转, 速度, 角速度
- Skeleton - 手模型中每根骨骼的方向
- Vibration - 震动

**Boolean** 

Boolean Actions是true或false的值。例如，“Grab”抓是一个常见的动作，无论是真还是假。你要么想要持有某些东西，要么你不想持有东西。使用vive手柄时，这可能意味着将“触发扳机”拉下75％，最终它会分解为真或假值。

**Single**

Single Actions是从0到1的模拟值。使用场景是你需要更多数据而不仅仅是真或假的情况。如果之前您正在读取0到1的值，然后等待它到达某个点（阈值），那么您可以使用Boolean Action完成相同的操作。Single Action的一个例子是SteamVR交互系统案例中遥控车的Throttle值（油门，表现为Trigger下按幅度，按的越下油门越大，其实就是前面说的0~1的模拟值）。

**Vector2**

Vector2类型的Action是两个模拟值X和Y。在SteamVR交互系统中，遥控小车的转向示例很好的展现了此类型的Actions。在Vive 手柄上，它被映射到触摸板。使用遥控车，我们使用y轴确定前进或后退方向，使用x轴确定转弯。

```C#
/*获取手柄作为输入源*/
SteamVR_Input_Sources hand = interactable.attachedToHand.handType;
//通过输入类型为Vector2的ActionSet获取输入源对应的输入数据。
SteamVR_Input.GetAction<SteamVR_Action_Vector2>("buggy", "Steering").GetAxis(hand)；
```

在旁边的控制人物示例中，我们将x / y输入映射到角色移动的方向和大小。

**Vector3**

Vector3类型的Action比较罕见。在SteamVR Home中，这用于滚动，x，y和z是要滚动的页数。

**Pose**

姿势类型的Action是3d空间中位置和旋转的表示。这用于跟踪您的VR控制器。用户可以通过设置控制器上姿势所代表的点来自定义这些绑定。在绑定界面中可以配置作为姿势追踪的参照点，有时候参照点不同，姿势展现的效果更好。

**Skeleton**

骨架类型的Action使用SteamVR骨架输入来获取我们在握住VR控制器时手指方向的最佳估计。这为每个控制器提供了一个标准来获得关节位置和旋转，而不管跟踪保真度如何。具有更高保真度手指跟踪能力的控制器将比没有更高保真度的手指更准确。

**Vibration**

唯一一个输出类型Action，提供触觉震动反馈。

### SteamVR Input窗口

这里是我们自定义的ActionSets,可以设置我们的按键绑定信息，并且规定输入输出类型。窗口中有许多按钮，除了ActionSet下我们定义的操作集合，还包括：高级设置、输入输出Action，Action详情，保存并生成ActionSet配置、打开案件绑定界面。

- Actions下，我们可以添加用到的交互。
- Action Details下，
  - Name、Type：例如SteamVR_Input.GetAction<SteamVR_Action_Vector2>("buggy", "Steering")中的“Steering”和Vector2
  - Required：
  - Localization：
  - Localized String:
- Save and Generate：保存ActionSet，当进度条完成时，它将在项目中创建一个名为SteamVR_Input的文件夹，其中包含所有这些代码文件。可以通过此窗口顶部的 *高级设置*  配置此路径。
- Open Binding UI：打开按键绑定界面。

Action详情之前已经介绍的差不多了，接下来看一下按键绑定界面。

![TIM截图20190319153333](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319153333.png)

![TIM截图20190319154436](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319154436.png)

![TIM截图20190319185644](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319185644.png)

1.表示手柄上的触摸板的配置

2.表示把它当成按钮使用：可选项是手柄输入位置而定，这里说一下容易疑惑的TrackPad和DPad，前者是触摸板（可以接收Vector2和Boolean），后者当成普通游戏手柄方向键那样的“面板”，只接受（前中后左右的点击输入）。

3.-> 4.点击时触发的Action

5.添加更多的交互映射



### 观察运行时输入

点击菜单选项 SteamVR Input Live View。这是由操作集和控制器分隔的所有操作的实时视图。当一个动作的值发生变化时，它会突出显示绿色，然后逐渐消失，为你提供状态变化的强烈视觉指示。动作的黄色背景表示您的代码尚未访问它。一旦您以某种方式访问它们，我们才会开始更新操作。如果按下按钮时没有看到任何反应，检查一下SteamVR是否连接正确，并且看一下控制台是否报错。