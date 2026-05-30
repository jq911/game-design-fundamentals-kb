---
title: 2.2.1 核心机制
---

<!-- chapter-pager:start -->

<div class="chapter-pager chapter-pager--top">
<a class="chapter-pager__button chapter-pager__button--prev" href=".."><span class="chapter-pager__label">上一页</span></a>
<a class="chapter-pager__button chapter-pager__button--next" href="../02-02-02-user-interface"><span class="chapter-pager__label">下一页</span></a>
</div>

<!-- chapter-pager:end -->

# 2.2.1 核心机制

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 2 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
> 关键词：核心机制、用户界面、表示层、交互模型、视角

## 原书内容整理

游戏设计者的一个任务就是把游戏中的一般规则转化为能被算法实现的符号化和数学模型。这个模型叫作游戏的核心机制，它比规则更具体。例如，一般规则可能会说“毛虫比蜗牛爬得快”，但是核心机制能精确地表述每分钟快多少厘米。程序员把核心机制转化为算法并且编写出实现算法的软件。本书不叙述技术设计或程序编写，但是会关注于这一过程的第一部分，创建核心机制。整个过程将在第14章中叙述。核心机制是所有游戏的中心，因为它们能产生游戏的可玩性。它们定义了游戏所给出的挑战，以及对应于这些挑战玩家能采取的动作。核心机制还确定了玩家行为对游戏世界所产生的影响。这一机制还阐述了达到游戏胜利的条件，以及胜利或失败后所产生的结果。核心机制的性质之一是它的现实主义（realism）的程度。普通游戏是为了娱乐玩家而创建的，即便它要在一定程度上体现出真实性，它也会做出一些妥协和让步，使游戏变得更好玩、更有趣。例如，真实的军队需要很多普通的供职人员来确保军队有足够的武器和所需的供给。而在游戏中，单个玩家要管理一切，所以为了避免玩家不堪重负，设计者把后勤从模型中抽取出来——也就是说，从核心机制中提取出来了。玩家只需简单地假定士兵不需要食物，不需要睡眠，而且他们的弹药也从来不会用光。所有的游戏在抽象与表象间转换。《吃豆人》是纯粹的抽象游戏，它不是任何真实事物的模拟。它的定位是虚构的，它的规则是任意的。《大奖赛传奇》是一款具有很高表象性的游戏：在气流偏导器被发明之前，它精确地模拟了之前驾驶赛车的极度危险性。尽管没有一款游戏是完全写实的，但是我们使用游戏的可变特性来作为写实的程度。在很早以前，我们使用抽象和表象这两个术语来描述游戏的现实主义范围。在决定游戏的概念时，你也决定了游戏的现实主义程度。你做出的决定确定了核心机制的复杂性。

<!-- chapter-pager:start -->

<div class="chapter-pager chapter-pager--bottom">
<a class="chapter-pager__button chapter-pager__button--prev" href=".."><span class="chapter-pager__label">上一页</span></a>
<a class="chapter-pager__button chapter-pager__button--next" href="../02-02-02-user-interface"><span class="chapter-pager__label">下一页</span></a>
</div>

<!-- chapter-pager:end -->

## 我的批注区

-
