## 工具概念

### 支持的机器学习方法

强化学习，[模仿学习](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Learning-Environment-Design-Agents.md#recording-demonstrations)，神经进化及其他

### 特点

使用PPO/SAC算法进行深度强化学习

可用于随机化的环境

支持多并发训练

可自定义任务

### 工作过程

- 通过Agent理解环境，

  收集环境数据，封装成向量

- 并做出决策

  生成行为向量，让Agent解包向量到对应行为

注意：每个向量值都代表一种实际意义。

- 不断训练，并且通过[Unity Inference Engine](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Unity-Inference-Engine.md)可以选择在CPU上跑还是在GPU上跑。
- 训练结果—Al模型。以本工具自定义的文件格式（.nm）保存

### 支持的机器学习算法

ML-Agent中提供的许多算法都使用某种形式的深度学习，这些深度学习建立在开源库[TensorFlow](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Background-TensorFlow.md)之上 。

### 怎么强化学习

通过Unity模拟出巨量的复杂环境数据 + 深度学习算法 = 完善的AI模型。

## 工具使用

### [安装](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Installation.md)

#### 编码部分

- 设计学习环境
- [实现自定义Agent](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Learning-Environment-Design-Agents.md)：定义代理初始化（重置参数，修改环境等），筛选环境数据，定义奖励，定义行为方式（环境测试），等逻辑（[Agent API](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/API-Reference.md)）。
- 实现自定义”学院“（管理Agent，通过添加委托实现变更学习环境），此步骤非必须。

### 编辑器配置部分

### 配置Agent

#### 配置多Agent同步学习



### [使用可执行文件训练](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Learning-Environment-Executable.md)

前提：

- 将GamePlay打包成可执行程序
- Python端导入`UnityEnvironment`库，调用可执行文件。

好处:

- 分享成果不需要拥有整个项目
- 可以远程训练
- 如果不需要渲染，可以通过Server Build模式加速
- 用编辑器做别的事。

### [工具集样例说明](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Learning-Environment-Examples.md)

1. 从特征向量中学习(3dball)
2. 利用摄像机输入集合CNN学习(girdworld)
3. 使用RNN记忆学习（hallway）

### 机器学习文件参数配置

[文档](https://github.com/Unity-Technologies/ml-agents/blob/release_7_docs/docs/Training-Configuration-File.md)