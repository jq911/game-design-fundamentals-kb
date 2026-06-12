---
title: 12.5 交互模型
---

<!-- chapter-pager:start -->

<div class="chapter-pager chapter-pager--top">
<a class="chapter-pager__button chapter-pager__button--prev" href="../12-04-managing-complexity"><span class="chapter-pager__label">上一页</span></a>
<a class="chapter-pager__button chapter-pager__button--next" href="../12-06-perspectives"><span class="chapter-pager__label">下一页</span></a>
</div>

<!-- chapter-pager:end -->

# 12.5 交互模型

> 来源：原书第 12 章 OCR 整理。扫描/OCR 文本已做基础清洗，仍建议对照原书复核术语和图注。

## 原书内容整理

交互模型在第2章中，我们把交互模型定义为玩家通过输入设备的输入和游戏世界中作为结果的动作之间的关系。你通过决定玩家如何按下控制器按钮和其他现实世界的活动如何通过核心机制为游戏世界中的动作进行解释就创建了游戏的交互模型。各种各样可用的输入设备的功能性的性能，将会影响你的决定，我们会在本章后面的输入设备中详细地讨论输入设备。这里没有篇幅来详细地讨论按钮分配问题，所以你应该玩与你的游戏类型相同的其他游戏来找到比较合适的例子。

在实践中，交互模型可以分为以下几类较为常见的类型。

- 基于化身的模型。这种模型下，玩家的大部分动作都是由控制游戏世界中的一个角

色（化身）组成的。玩家通过他的化身与游戏世界交互，更重要的是，玩家通常只能影响化身当前所在的游戏世界区域。化身类似于人类的身体：我们在世界中要做某些事情时，在物理上必须把我们的身体带到希望做这件事的地方。这并不是说化身一定是人类或者具有人类特点，一个交通工具也可以是化身。所以，为了实现这种模式，很多按钮分配的决定都应该以导航为中心，这一点我们会在12.10一节中讨论。

- 多处存在模型。这种模型下玩家同时可以作用于游戏世界的不同部分。为了实现这

一点，你必须给他一个允许看到各种各样区域的视角，他可以改变这个视角，一般情况下是空中视角。象棋就使用了多处存在交互模型，普通情况下玩家可以按照任意顺序移动他的任意一个棋子（必须可以合法地移动）。实现这种模式需要给玩家提供选择和拿起环境中的物体，或者给单位发布命令的方法。

- 基于团队的交互模型。在这种模型下，一个小组的全部角色通常保持在一起作为一

组，在角色扮演游戏中最经常发现这种模型。在这种模型下，你可能会使用点选式导航和空中视角。

- 竞赛模型。在这种模型中，玩家回答问题并做出决定，就像一个电视游戏秀中的竞

赛那样。这里不需要导航，你只需要简单地把不同的决定选项分配到不同的按键上就可以了。

- 桌面模型。它模仿了一个计算机（或者实际的）桌面，通常情况下只在某些表现办

公室活动的游戏中出现，例如商业模拟。

遵循常见行业习惯的连贯设计都会属于这些熟悉模型中的一种。如果你的游戏确实需要，你可以创建其他的模型，但是如果你这样做了，可能需要设计更详细的教学关卡来让玩家学习其中的控制。

<!-- chapter-pager:start -->

<div class="chapter-pager chapter-pager--bottom">
<a class="chapter-pager__button chapter-pager__button--prev" href="../12-04-managing-complexity"><span class="chapter-pager__label">上一页</span></a>
<a class="chapter-pager__button chapter-pager__button--next" href="../12-06-perspectives"><span class="chapter-pager__label">下一页</span></a>
</div>

<!-- chapter-pager:end -->

## 我的批注区

> 暂无。
