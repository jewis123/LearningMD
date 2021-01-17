### 介绍

Snapdragon Profiler是在Windows，Mac和Linux平台上运行的性能分析软件。

- 可分析板块：CPU，GPU，DSP，内存，电源，热量和网络数据。

**四大主要功能**

- 实时性能数据：通过Process下双击选择指定项目，就能在右侧时间线界面实时查看记录。

- 时间线抓取分析：目的是抓取一段时间内的性能指标数据，在时间线上双击性能指标在右侧能够显示一些详细数据。
- 采样抓取分析：以固定间隔抓取分析性能指标数据。
- 快照分析：分析一帧的渲染流程、渲染资产。

[上手资料](https://zhuanlan.zhihu.com/p/32937281), 文章内容更正：

文中所说的Vulkan快照相关的问题，在v2018.3+就开始支持了,  并在v2020.3版本相对稳定。

[发布日志](https://developer.qualcomm.com/software/snapdragon-profiler/release-notes)

### 设备需求

GPU: 晓龙806+

安卓: 6.0+

### 应用笔记

[应用笔记](https://developer.qualcomm.com/software/snapdragon-profiler/app-notes)

**关注点：**

- FPS：平均帧率；帧率谷峰等

- CPU负载（一帧内执行的指令数，主要对函数耗时分析）：

  游戏逻辑、剔除算法、CacheMissing、CPU调度（线程争用）等

- GPU负载（一帧内执行的shader指令数，通过截帧分析）：

  DrallCall数、shader复杂度、纹理采样、透明物件、OverDraw、RenderState切换频率、GPUActivity(GPU/CPU交互)等

- 显存（GMEM）：GMEM Load、GMEM Store等

- 内存：资源规格、泄漏、碎片、GC等

- 网络：弱网、流量等

### 分析流程

- 检查性能指标，查找异常点
- 深挖热点成因
- 对症下药

### 实战记录