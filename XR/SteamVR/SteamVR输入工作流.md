### 简介

这是一个介绍自定义动作集的案例，具有完整工作流。

### 添加ActionSet

1. 点击SteamVR Input菜单按钮，打开动作集设置界面。

2. 点击动作集 + 号按钮，添加动作集，我们命名这个动作集为“Planting”

3. 给动作集添加Action输入列表，这里我们添加一个Boolean类型的输入action，因为种值是一个非真即假的动作。我们不希望这个动作受到约束，因为它对我们的应用程序并不重要，所以Required我们选择suggested。然后注明本地化提示符（Localized String）

   ![TIM截图20190319220153](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319220153.png)

4. 点击open binding UI，对话框选yes。

5. 确保SteamVR和手柄为开启状态，点击Current Binding区域下的View。页面会显示没有绑定的Action数目，及哪些action没有被绑定。

   ![TIM截图20190319220844](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319220844.png)

6. 选择物理手柄交互部分作为绑定对象，点击旁边给的 + 号，添加绑定。这里我选择将Trigger做为Button与plant动作相互绑定。

   ![TIM截图20190319221117](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319221117.png)

​       ![TIM截图20190319221144](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319221144.png)

7. 点击下方" Replace Default Binding  "按钮，这将使用这些新更改自动替换项目根文件夹中的关联绑定文件。

8. 点击左上角“返回”，然后点击Official Binding 中你刚刚做过更新的区域的 View 按钮，进入后点击左下角Select this Binding替换。如果他提示你有本地修改没有保存，你可选择discard，因为我们刚刚的修改已经导出了。

   查看结果：![TIM截图20190319223323](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319223323.png)

9. 使用刚刚定义的动作集：

   - 在Hand组件下添加插件预制Planting组件，设置使用的action

     ![TIM截图20190319224415](C:\Users\43432\Desktop\LearningMD\XR\SteamVR\截图\TIM截图20190319224415.png)

10. 因为我们使用的新动作集，所以要把[SteamVR]对象中的SteamVR_ActivateActionSetOnLoad组件中的ActionSet调整对刚刚新建的Planting动作集。

11. 运行场景查看效果。

另注：

- 实际操作中发现Hand脚本中要指定Player引用，所以这个脚本是有限制的，至少得指定父级Player组件。

- 如果想要在运行时激活多个ActionSet,可以添加SteamVRActiveActionSetOnLoad组件让其加载指定动作集，非推荐做法，容易发生按键冲突。

### Planting组件分析

**摘要：**



```C#
using Valve.VR.InteractionSystem;

//定义SteamVR_Action_Boolean类型的动作变量，并且指定动作集和动作映射
public SteamVR_Action_Boolean plantAction = SteamVR_Input.GetAction<SteamVR_Action_Boolean>("Planting", "Plant");  //动作集Planting，动作Plant。大小写敏感。
```

```C#
		private void OnEnable(){
		    。。。
		    //注册状态改变监听
		    //OnPlantActionChange：委托
		    //HandType:左右手类型
			plantAction.AddOnChangeListener(OnPlantActionChange, hand.handType);
        }

        private void OnDisable()
        {
        	//注销监听
            if (plantAction != null)
                plantAction.RemoveOnChangeListener(OnPlantActionChange, hand.handType);
        }
		
		//定义委托
        private void OnPlantActionChange(SteamVR_Action_Boolean actionIn, SteamVR_Input_Sources inputSource, bool newValue)
        {
            if (newValue)
            {
                Plant();
            }
        }
```

**探究：**

接下来我们看一下SteamVR_Action_Boolean.cs中有些什么内容。

- delegate委托，用来定义外部回调格式，与之匹配的是Listener。
- event类型变量：定义了很多针对sourceMap容器的状态改变事件，sourceMap容器中存放是输入源的事件。
- void类型的各种Listener,它们将外部事件存入sourceMap容器，当状态改变时，执行事件。
- bool型的Getter，适合我们做逻辑判断

