---
title: 12.1 什么是用户界面
---

<!-- chapter-pager:start -->

<div class="chapter-pager chapter-pager--top">
<a class="chapter-pager__button chapter-pager__button--prev" href=".."><span class="chapter-pager__label">上一页</span></a>
<a class="chapter-pager__button chapter-pager__button--next" href="../12-02-player-centered-interface-design"><span class="chapter-pager__label">下一页</span></a>
</div>

<!-- chapter-pager:end -->

# 12.1 什么是用户界面

> 来源：原书第 12 章 OCR 整理。扫描/OCR 文本已做基础清洗，仍建议对照原书复核术语和图注。

## 原书内容整理

就像我们在图2-1中向你展示的那样，用户界面处于玩家和游戏内部之间。用户界面接收从硬件输入设备上传来的输入，然后在输出设备上的输出。它将玩家的输入——如现实生活中按下键盘（或者其他操作）一根据交互模型（见第1章）转换为游戏世界中的动作，通过对核心机制的操作，在游戏中就能以可见的或可听的方式实现玩家在各个场景中的需求。

这一章中，我们提到的输出指的是UI的视觉元素（visual element）和听觉元素（audio element)，输入指的是控制元素。当游戏给玩家关于活动、游戏世界的状态或者化身的状态（例如，健康或者剩余的金钱）的重要信息时，我们就说它给玩家提供了“反馈”——就是通知玩家他的动作效果。提供这种信息的视觉和听觉元素，我们称为“反馈元素”。

乍一看，似乎本章所使用的术语“用户界面”（UI）和“用户体验”（UE）可以互换。

但其实它们并不一样。“用户体验”是在玩家头脑内发生的；而“用户界面”则是游戏软件的一部分：它介于游戏的核心机制和玩家之间，用来创造玩家的体验。

术语“按钮”不幸地过载了：因为有的时候它指玩家可以按下的输入设备上的物理按钮，而其他的时候指屏幕上的可视元素，这个元素画得看起来像一个按钮，玩家可以使用鼠标进行点击。为了消除两者的歧义，本章中我们将使用控制器按钮来代表输入设备上的物理按钮，而那些屏幕上的且由鼠标触发的按钮，我们称为屏幕按钮。按键指的是计算机键盘上的按键（或者是手机上的内部按键）。术语按键和控制器按钮可以交换使用，因为它们传送相同类型的数据。

菜单和屏幕按钮作为视觉元素出现在屏幕上，但点击或敲打它们会向游戏的内部发送消息，这使得它们也是控制元素。此外，屏幕按钮的外观可响应于点击而改变，使其成为用于给出信息以及用于进行控制的机制。你在使用计算机时的体验应该能帮助你在上下文中了解这些术语。

任何一个关于UI的谈论都会陷入鸡和蛋的问题：我们不能在不提到“能量条”和“标尺”等视觉元素的前提下告诉你怎样设计一个好的用户界面，我们也不能只介绍常用的视觉元素，而不引用它们使用的实例。为了先介绍最关键的信息，我们选择从界面设计的基本原理开始。如果你遇到了对你以前从未听说过的界面元素的引用，可以翻阅本章12.7节，寻找详细解释。

数十种甚至上百种已发行的书籍都在讲述用户界面设计，在这里不打算重复了。我们主要集中在特定的游戏用户界面上，介绍它们怎样和游戏机制进行交互以及怎样为玩家创造娱乐体验。想阅读更多的关于一般UI的知识，参考加瑞特（JesseJamesGarrett）所著的《用户体验要素》（TheElementsofUserExperience）。

提示：在设计核心机制时，应避免将设计要点建立在特定的输入/输出（I/O）器件的性能特征上。要让UI来管理硬件，保持游戏硬件的内部独立。这样你以后将游戏移植到另一台机器上时，就只需重新设计UI，而不必再设计游戏的核心机制。

<!-- chapter-pager:start -->

<div class="chapter-pager chapter-pager--bottom">
<a class="chapter-pager__button chapter-pager__button--prev" href=".."><span class="chapter-pager__label">上一页</span></a>
<a class="chapter-pager__button chapter-pager__button--next" href="../12-02-player-centered-interface-design"><span class="chapter-pager__label">下一页</span></a>
</div>

<!-- chapter-pager:end -->

## 我的批注区

> 暂无。
