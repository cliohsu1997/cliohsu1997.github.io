# Herding Teaching Demo — Bilingual Verbal Script
**City University of Macau · ~20 minutes · English ＋ 中文（对照）**

Key terms / 关键术语：**\(G/B\)** = true state 真实状态（好/坏）; **\(g/b\)** = private signal 私人信号; **Line up / Drop** = action 行动（排队/离开）; **information cascade** = 信息级联（信息瀑布）; **herding** = 羊群效应.

---

## 1 · Title 开场（~45 sec）

**EN:** “Hi, I’m Ke Cheng Hsu from HKUST Economics. Today we’ll talk about herding under imperfect information. Plan: start with a Macau queue you all know, a few everyday examples, what herding means, Bayes with a restaurant, then Person 1, 2, 3 — to see why following the crowd can be rational, and still go wrong.”

**中：** 「大家好，我是香港科技大学经济系的许克丞。今天讲『不完美信息下的羊群效应』。流程：先从大家熟悉的澳门排队说起，再看几个日常例子，解释什么是羊群效应，用一家餐厅讲贝氏定理，最后走一遍第一、第二、第三个人——看为什么跟风有时是理性的，却仍会出错。」

---

## 2 · Margaret’s 玛嘉烈蛋挞（~2 min）

**EN:** “Margaret’s Café e Nata near Sintra Square — there’s always a long winding queue. Many say the tarts are too sweet or oily compared to Lord Stow’s, and the line is mostly guidebook fame. My version: after I tried it, I felt so-so; my friend felt the same. I like egg tarts, but not enough for twenty minutes. I only lined up because I saw so many people lining up — so I thought it must be amazing.”

**中：** 「新马路附近的玛嘉烈蛋挞，永远大排长龙。很多人觉得它比安德鲁甜、又油，队伍多半是旅游书名气。我自己吃过觉得普通，朋友也这么觉得。我喜欢蛋挞，但不值得站二十分钟。我排队只是因为看到很多人在排，就想说一定超好吃。」

---

## 3 · Other examples 其他例子（~2 min）

**EN:** “Same pattern elsewhere. SBF and FTX — people piled in because others seemed to get rich; once trust broke, everyone rushed for the exit. The recent NVDA crush — the stock rose on AI enthusiasm; when sentiment flipped, everyone sold together. Labubu toys — people chase them because they’re everywhere online; popularity itself looks like a quality signal.

And homework copying: the best econ student finishes first; the second-best compares answers with the best; the third — even if their own answer was originally correct — may still switch to match the first two. That is exactly the cascade we’ll build.”

**中：** 「同样的模式到处都是。SBF 和 FTX——大家看别人好像赚钱就涌进去；信任一崩，大家又一起挤兑出逃。最近的 NVDA 大跌——股价因 AI 热潮上去，情绪一翻转，所有人一起卖。Labubu——因为网上到处都是就抢，热门本身看起来像品质保证。

还有抄作业：经济最好的同学先写完；第二名跟第一名对答案；第三个人——就算自己本来写对了——也可能改成跟前两个人一样。这就是我们待会要建立的信息级联。」

---

## 4 · What is herding 什么是羊群效应（~1.5 min）

**EN:** “You have a private clue, but you also see what others chose — and sometimes you follow the crowd even when your own clue says the opposite. Why? Other people’s choices carry information. When signals are imprecise, early information can be wrong, so early actions can be wrong — and later people infer that wrong information from those actions.”

**中：** 「你有自己的私人线索，但你也看到别人怎么选——有时你会跟着人群走，哪怕你的线索说的是另一回事。为什么？因为别人的选择本身带有信息。当信号不精确时，早期信息可能是错的，所以早期行动也可能是错的——而后面的人从这些行动推断信息，就继承了这个错误。」

---

## 5 · Setup 设定（~1.5 min）

**EN:** “One restaurant: state Good or Bad, prior one half each. People arrive one by one; each gets a private signal \(g\) or \(b\), 70% accurate: \(\Pr(g\mid G)=0.7\), \(\Pr(b\mid G)=0.3\), \(\Pr(g\mid B)=0.3\), \(\Pr(b\mid B)=0.7\).

Signals are *conditionally independent given the state* — meaning once you know the restaurant is Good or Bad, what signal A draws does not affect what signal B draws; they only move together through the common state.

Actions: Line up or Drop. Break-even: Line up if \(\Pr(G\mid\text{info})>1/2\), Drop if \(<1/2\); if \(=1/2\), choose each with probability \(1/2\). Goal: Person 1–3; watch Person 3 discard his own signal.”

**中：** 「一家餐厅，状态是好或坏，事前各二分之一。大家一个个到，各自拿到私人信号 \(g\) 或 \(b\)，准确率七成：\(\Pr(g\mid G)=0.7\)、\(\Pr(b\mid G)=0.3\)、\(\Pr(g\mid B)=0.3\)、\(\Pr(b\mid B)=0.7\)。

信号是『给定状态下条件独立』——意思是：一旦你知道餐厅是好是坏，A 拿到什么信号完全不影响 B 拿到什么；他们只透过共同的状态连动。

行动：排队或离开。损益两平：看好概率大于二分之一就排，小于就离开；刚好二分之一就各半随机。目标：走一遍第一到第三个人，看第三个人怎么丢掉自己的信号。」

---

## 6 · Person 1 第一个人（~2 min）

**EN:** “The picture: area equals probability. Left half is \(G\), right half \(B\); the \(g\) regions cover 70% of the Good side and 30% of the Bad side.

Person 1 only has his own signal \(g\). Bayes: \(\Pr(G\mid g)\) is the Good slice over the whole \(g\) area — \(0.35 / (0.35+0.15) = 0.7\). Above one half, so he Lines up. Everyone else only sees his *action*, not his raw signal.”

**中：** 「看图：面积就是概率。左半是 \(G\)、右半是 \(B\)；\(g\) 区域盖住好边的七成、坏边的三成。

第一个人只有自己的信号 \(g\)。用贝氏：\(\Pr(G\mid g)\) 就是 \(g\) 里面属于好边的比例——\(0.35 / (0.35+0.15)=0.7\)。大于二分之一，所以他排队。其他人只看到他的『行动』，看不到他的信号。」

---

## 7 · Person 2 第二个人（~2 min）

**EN:** “Person 2 sees Person 1 Line up — that reveals \(s_1=g\). Two cases.

Case \(s_2=g\): two good clues, posterior above one half, Line up.

Case \(s_2=b\): one good clue and one bad clue of the same strength. Joint under \(G\) is \(0.7\cdot0.3=0.21\), joint under \(B\) is \(0.3\cdot0.7=0.21\) — by conditional independence. Equal, so the posterior is exactly one half. He is indifferent — Line up or Drop with probability one half each.”

**中：** 「第二个人看到第一个人排队——这就揭露了 \(s_1=g\)。分两种情况。

若 \(s_2=g\)：两个好线索，看好概率大于二分之一，排队。

若 \(s_2=b\)：一个好线索配一个坏线索，强度一样。在 \(G\) 下的联合概率是 \(0.7\times0.3=0.21\)，在 \(B\) 下是 \(0.3\times0.7=0.21\)——靠条件独立。两边相等，所以看好概率刚好二分之一。他无差异——排队或离开各二分之一概率。」

---

## 8 · Person 3 — write the posterior 写出事后概率（~2 min）

**EN:** “Now the story: two people are lining up in front of me, and I draw a bad signal \(b\). Should I wait in line or leave? That depends on \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\).

Write Bayes with the *actions and my signal*: numerator \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\), denominator that plus the same under \(B\).

Important: do **not** replace Line up by \(g\). Line up is an action; \(g\) is a signal — especially since Person 2 sometimes Lines up even with \(b\). Next we need the conditional probabilities \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) and \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\).”

**中：** 「情境：前面两个人都在排队，而我拿到坏信号 \(b\)。该排还是该走？取决于 \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\)。

写贝氏，用『行动加我的信号』：分子是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\)，分母再加上 \(B\) 下的同样一项。

注意：**不要**把排队直接换成 \(g\)。排队是行动，\(g\) 是信号——尤其第二个人有 \(b\) 时也可能排队。接下来要算 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) 和 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\) 这两个条件概率。」

---

## 9 · Person 3 — conditional probabilities 条件概率（~2.5 min）

**EN:** “Why can we split the product? The earlier Line-ups depend only on \(s_1\) and \(s_2\). Given the state, those signals are independent of Person 3’s \(b\), so \(b\) is conditionally independent of the two Line-ups: probability of (LU, LU, \(b\)) equals probability of (LU, LU) times probability of \(b\).

Under \(G\): Person 1 Lines up only if \(s_1=g\), probability 0.7. Given that, Person 2 Lines up for sure if \(s_2=g\) (0.7), or with probability one half if \(s_2=b\) (0.3). So \(0.7\,(0.7+0.3\cdot\tfrac12)=0.595\), times \(\Pr(b\mid G)=0.3\) gives \(0.1785\).

Under \(B\): same logic with flipped likelihoods — Person 1 Lines up only if \(s_1=g\) (0.3); Person 2 Lines up for sure if \(s_2=g\) (0.3), or half the time if \(s_2=b\) (0.7). That is \(0.195\), times \(\Pr(b\mid B)=0.7\) gives \(0.1365\).”

**中：** 「为什么可以拆成乘积？前面两个排队只取决于 \(s_1\) 和 \(s_2\)。给定状态下，这两个信号跟第三个人的 \(b\) 独立，所以 \(b\) 跟（排队、排队）条件独立：概率＝（排队、排队）的概率 × \(b\) 的概率。

在 \(G\) 下：第一个人只有 \(s_1=g\) 才排，概率 0.7。接着第二个人：若 \(s_2=g\)（0.7）必排；若 \(s_2=b\)（0.3）以二分之一概率排。所以 \(0.7(0.7+0.3\cdot\tfrac12)=0.595\)，再乘上 \(\Pr(b\mid G)=0.3\)，得 \(0.1785\)。

在 \(B\) 下：同样逻辑、概率对调——第一个人只有 \(s_1=g\) 才排（0.3）；第二个人 \(s_2=g\)（0.3）必排、\(s_2=b\)（0.7）一半排。得 \(0.195\)，乘 \(\Pr(b\mid B)=0.7\)，是 \(0.1365\)。」

---

## 10 · Person 3 — combine and decide 合并决定（~2 min）

**EN:** “Equal priors, so plug in: \(0.1785\cdot\tfrac12\) over \(0.1785\cdot\tfrac12 + 0.1365\cdot\tfrac12\), about 0.57 — above one half.

So Person 3 still Lines up — he discards his own bad signal. That is the start of the **information cascade**: two public Line-ups outweigh his private clue.”

**中：** 「事前各二分之一，代入：\(0.1785\cdot\tfrac12\) 除以 \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\)，约 0.57——大于二分之一。

所以第三个人还是排队——他丢掉了自己的坏信号。这就是**信息级联**（信息瀑布）的开始：两个公开的排队行动，压过了他的私人线索。」

---

## 11 · Takeaways 结语（~2 min）

**EN:** “If everyone only used their own signal and we aggregated, private information would keep entering the public record. But in a cascade, choices are sequential: early actions become public clues, so later people can rationally ignore their own signals.

Same logic as Margaret’s queues, SBF/FTX, NVDA, Labubu — and homework copying. Questions?”

**中：** 「如果每个人都只用自己的信号、我们再加总，私人信息会一直进入公共记录。但在信息级联里，选择是序贯的：早期行动变成公开线索，后人就可能理性地忽略自己的信号。

同样的逻辑：玛嘉烈的长龙、SBF/FTX、NVDA、Labubu——还有抄作业。有问题吗？」
