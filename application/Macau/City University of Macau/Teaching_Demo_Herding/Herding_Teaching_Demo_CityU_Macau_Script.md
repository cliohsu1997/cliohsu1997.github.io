# Herding Teaching Demo — Bilingual Verbal Script
**City University of Macau · ~20 minutes · English ＋ 中文（对照）**

Key terms / 关键术语：**\(G/B\)** = true state 真实状态（好/坏）; **\(g/b\)** = private signal 私人信号; **Line up / Drop** = action 行动（排队/离开）; **information cascade** = 信息级联（信息瀑布）; **herding** = 羊群效应.

---

## 1 · Title 开场（~45 sec）

**EN:** “Hi everyone, I’m Ke Cheng Hsu from HKUST. Today I want to talk about herding under imperfect information. We’ll start with something from daily life — queuing — and then look at a few more examples to build some intuition. After that, I’ll teach you Bayes’ rule with a restaurant example, and walk through Person 1, 2, and 3. The goal is to see why following the crowd can be rational for each individual — but not necessarily good for the group as a whole. In the end, we’ll use a small example to drive that point home.”

**中：** 「大家好，我是香港科技大学的许克丞。今天我想讲「不完美信息下的羊群效应」。我们会先从大家生活中的排队说起，再看几个例子，给大家一个比较直觉的解释。接着我会用一个餐厅的例子教大家贝叶斯定理，跟着第一个、第二个、第三个人走一遍。目标是讲清楚一件事：为什么跟风有时候对每一个人来讲是理性的，但对整个群体来讲并不是一件好事。最后我们会用一个小例子，把这个道理再说透。」

---

## 2 · Margaret’s 玛嘉烈蛋挞（~2 min）

**EN:** “Margaret’s Café e Nata, hidden in an alley near Sintra Square — there’s always a long winding queue. To be honest, I don’t see how it really differs from a usual egg tart. Maybe the first few people just lined up out of boredom; then everyone else saw the queue and read it as proof of quality. I did the same: I saw so many people lining up that I joined for twenty minutes — and eventually it didn’t even taste good. That’s the puzzle: I used my own eyes and tongue, yet the crowd still talked me into the queue.”

**中：** 「玛嘉烈蛋挞藏在新马路附近的一条小巷里，门口永远排长龙。说实话，我吃不出它跟一般蛋挞有什么差别。说不定最早那几个人只是闲着无聊才去排，结果后面的人看到队伍，就把它当成了品质的证明。我也一样：看到那么多人排队，就跟着排了二十分钟——结果吃下去觉得也不怎么样。问题就在这里：我明明有自己的眼睛和舌头，最后还是被人群劝进了队伍。」

---

## 3 · Other examples 其他例子（~2–2.5 min）

**EN:** “Two richer stories.

First, NVIDIA’s recent slide. There was gossip around Jensen Huang — the Chinese internet nickname 老黄, the 小一小二小三 rumors. But ask: did NVIDIA’s fundamentals actually change? AI demand, earnings, guidance — largely the same. If you trust your own analysis, not much should move the price. Still, when the first investors sell and the price dips, later investors see the drop and infer that others may know something they don’t. If that inference outweighs their own read on fundamentals, they sell too. Each wave of selling pushes the price lower, giving the next investor an even stronger reason to follow — the price fall feeds on itself.

Second, a bank run. You hear a rumor that a bank is in trouble. You might not believe it yourself, but you see a long line of people withdrawing at the branch. You think: maybe they know something I don’t. So you queue up and withdraw too. Each extra withdrawal makes the line look even more alarming, and gives the next person a stronger reason to run. Even if the rumor was false, the run itself can bring the bank down.

And homework copying, the same logic in miniature: the student with the best grade finishes first; the second-best compares answers with the best and adopts them; the third person — even if their own answer was originally correct — sees two agreeing answers and switches to match. Each step is locally reasonable; together they form an **information cascade** — the 信息瀑布.”

**中：** 「讲两个更完整的例子。

第一个，最近英伟达的下跌。当时围绕黄仁勋——华人圈叫他老黄——传着小一小二小三的说法。但先问一句：英伟达的基本面真的变了吗？AI 需求、财报、业绩指引，基本上都没变。如果你相信自己的分析，股价其实不该动这么多。可是当第一批投资者卖出、价格开始跌，后面的人看到下跌，就会想：别人是不是知道什么我不知道的事？一旦这种想法压过了自己对基本面的判断，他们也会跟着卖。每一波卖出都把价格压得更低，又给下一个人更强的理由跟进——跌势就这样自我加强。

第二个，银行挤兑。你听到传言说某家银行出了问题。你自己未必信，但你看到分行门口排了一长串人在提款。你会想：他们是不是知道什么我不知道的事？于是你也去排队把钱取出来。每多一个人提款，队伍看起来就越吓人，又给下一个人更强的理由去挤兑。就算最初的传言是假的，挤兑本身也可能把银行拖垮。

抄作业也是一样的道理，只是规模更小：成绩最好的同学先写完；第二名拿来跟第一名对答案，干脆照抄；第三个人——就算自己原本写对了——看到两份一样的答案，也把自己的改成一样。每一步单独看都说得通，但合在一起，就是一条**信息瀑布**，也就是信息级联。」

---

## 4 · What is herding 什么是羊群效应（~1.5 min）

**EN:** “The pattern behind all three stories is the same — following the crowd: you only have one piece of information that you know yourself, but you also see how others choose — and sometimes you follow the crowd even when your own information points the other way. Why? Other people’s choices carry information. When signals are imprecise, early information can be wrong, so early actions can be wrong — and later people infer the earlier people’s information from those actions, passing the error all the way down. In the examples: the first few in line may have had no real reason, the first NVDA sellers may have overestimated the impact of Jensen Huang’s scandal on the stock price, and the first bank-run withdrawers may have overreacted to a rumor — yet their actions still moved everyone after them.”

**中：** 「这三个故事背后都是同一个模式——从众。你只有一条自己知道的信息，但你也看到别人怎么选；有时候你会跟着别人走，哪怕你自己的信息跟他们说的是相反的。为什么？因为别人的选择本身就带着信息。当信号不够精确时，最早的信息可能是错的，最早的行动也就跟着错——而后面的人从这些行动里反推前面人的信息，就把这个错误一路传下去。放回刚才的例子：最早排蛋挞的可能只是无聊，最早卖英伟达的可能高估了黄仁勋出轨对股价的影响，最早去银行提款的可能对一个谣言反应过度——但他们的行动照样影响了后面所有人。」

---

## 5 · Setup 设定（~1.5 min）

**EN:** “One restaurant: state Good or Bad, prior one half each. People arrive one by one; each gets a private signal \(g\) or \(b\), 70% accurate: \(\Pr(g\mid G)=0.7\), \(\Pr(b\mid G)=0.3\), \(\Pr(g\mid B)=0.3\), \(\Pr(b\mid B)=0.7\).

Signals are *conditionally independent given the state* — meaning once you know the restaurant is Good or Bad, what signal A draws does not affect what signal B draws; they only move together through the common state.

Actions: Line up or Drop. Break-even: Line up if \(\Pr(G\mid\text{info})>1/2\), Drop if \(<1/2\); if \(=1/2\), choose each with probability \(1/2\). Goal: Person 1–3; watch Person 3 discard his own signal.”

**中：** 「设定很简单：一家餐厅，真实状态是好或坏，事前各二分之一。大家一个接一个到，每人拿到一个私人信号 \(g\) 或 \(b\)，准确率七成：\(\Pr(g\mid G)=0.7\)、\(\Pr(b\mid G)=0.3\)、\(\Pr(g\mid B)=0.3\)、\(\Pr(b\mid B)=0.7\)。

这些信号是「给定状态下条件独立」——意思是：一旦餐厅是好是坏已经定了，A 拿到什么信号完全不影响 B 拿到什么；他们只是因为同一个状态才看起来相关。

行动只有两个：排队，或离开。规则是：看好概率大于二分之一就排，小于就离开，刚好二分之一就各丢一半硬币。目标是跟着第一、第二、第三个人走一遍——看第三个人怎么干脆丢掉自己的信号。」

---

## 6 · Person 1 第一个人（~2 min）

**EN:** “The picture: area equals probability. Left half is \(G\), right half \(B\); the \(g\) regions cover 70% of the Good side and 30% of the Bad side.

Person 1 only has his own signal \(g\). Bayes: \(\Pr(G\mid g)\) is the Good slice over the whole \(g\) area — \(0.35 / (0.35+0.15) = 0.7\). Above one half, so he Lines up. Everyone else only sees his *action*, not his raw signal.”

**中：** 「先看这张图：面积就是概率。左半边是 \(G\)，右半边是 \(B\)；画出来的 \(g\) 区域盖住好边的七成、坏边的三成。

第一个人手上只有自己的信号 \(g\)。用贝氏算：\(\Pr(G\mid g)\) 就是 \(g\) 这块里面属于好边的比例——\(0.35\) 除以 \(0.35+0.15\)，等于 \(0.7\)。大于二分之一，所以他去排队。重点是：后面的人只看得见他的**行动**，看不见他拿到的信号。」

---

## 7 · Person 2 第二个人（~2 min）

**EN:** “Person 2 sees Person 1 Line up — that reveals \(s_1=g\). Two cases.

Case \(s_2=g\): two good clues, posterior above one half, Line up.

Case \(s_2=b\): one good clue and one bad clue of the same strength. Joint under \(G\) is \(0.7\cdot0.3=0.21\), joint under \(B\) is \(0.3\cdot0.7=0.21\) — by conditional independence. Equal, so the posterior is exactly one half. He is indifferent — Line up or Drop with probability one half each.”

**中：** 「第二个人看到第一个人排队——这一下就等于告诉他 \(s_1=g\)。分两种情形。

如果他自己拿到 \(s_2=g\)：两条好线索，看好概率大于二分之一，直接排队。

如果他拿到的是 \(s_2=b\)：一条好线索配一条坏线索，力道一样大。算一下：在 \(G\) 之下的联合概率是 \(0.7\times0.3=0.21\)，在 \(B\) 之下是 \(0.3\times0.7=0.21\)——靠的就是条件独立。两边一模一样，所以看好概率刚好二分之一。他排不排都行——排队或离开各一半概率。」

---

## 8 · Person 3 — write the posterior 写出事后概率（~2 min）

**EN:** “Now the story: two people are lining up in front of me, and I draw a bad signal \(b\). Should I wait in line or leave? That depends on \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\).

Write Bayes with the *actions and my signal*: numerator \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\), denominator that plus the same under \(B\).

Important: do **not** replace Line up by \(g\). Line up is an action; \(g\) is a signal — especially since Person 2 sometimes Lines up even with \(b\). Next we need the conditional probabilities \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) and \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\).”

**中：** 「现在进入正题：前面已经有两个人在排队，而我自己拿到的是坏信号 \(b\)。我该跟着排，还是转身走？答案取决于 \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\)。

写贝氏，条件要用「行动加上我的信号」：分子是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\)，分母是这一项再加上 \(B\) 之下同样的一项。

这里要特别注意：**不能**把「排队」直接换成 \(g\)。排队是行动，\(g\) 是信号——尤其第二个人就算拿到 \(b\) 也有机会排队。接下来要算的就是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) 和 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\) 这两个条件概率。」

---

## 9 · Person 3 — conditional probabilities 条件概率（~2.5 min）

**EN:** “Why can we split the product? The earlier Line-ups depend only on \(s_1\) and \(s_2\). Given the state, those signals are independent of Person 3’s \(b\), so \(b\) is conditionally independent of the two Line-ups: probability of (LU, LU, \(b\)) equals probability of (LU, LU) times probability of \(b\).

Under \(G\): Person 1 Lines up only if \(s_1=g\), probability 0.7. Given that, Person 2 Lines up for sure if \(s_2=g\) (0.7), or with probability one half if \(s_2=b\) (0.3). So \(0.7\,(0.7+0.3\cdot\tfrac12)=0.595\), times \(\Pr(b\mid G)=0.3\) gives \(0.1785\).

Under \(B\): same logic with flipped likelihoods — Person 1 Lines up only if \(s_1=g\) (0.3); Person 2 Lines up for sure if \(s_2=g\) (0.3), or half the time if \(s_2=b\) (0.7). That is \(0.195\), times \(\Pr(b\mid B)=0.7\) gives \(0.1365\).”

**中：** 「为什么可以拆成两个概率相乘？前面两个人排不排队，只取决于 \(s_1\) 和 \(s_2\)。给定状态之后，这两个信号跟第三个人的 \(b\) 彼此独立，所以 \(b\) 跟「两人排队」条件独立：联合概率等于「两人排队」的概率乘上 \(b\) 的概率。

在 \(G\) 之下：第一个人只有拿到 \(s_1=g\) 才会排，概率 0.7。在这个前提下，第二个人拿到 \(s_2=g\)（概率 0.7）一定排；拿到 \(s_2=b\)（概率 0.3）则以一半概率排。合起来是 \(0.7(0.7+0.3\cdot\tfrac12)=0.595\)，再乘上 \(\Pr(b\mid G)=0.3\)，得到 \(0.1785\)。

在 \(B\) 之下：逻辑完全一样，只是信号概率对调——第一个人只有 \(s_1=g\) 才排（概率 0.3）；第二个人 \(s_2=g\)（0.3）必排、\(s_2=b\)（0.7）一半排。算出来是 \(0.195\)，乘上 \(\Pr(b\mid B)=0.7\)，得到 \(0.1365\)。」

---

## 10 · Person 3 — combine and decide 合并决定（~2 min）

**EN:** “Equal priors, so plug in: \(0.1785\cdot\tfrac12\) over \(0.1785\cdot\tfrac12 + 0.1365\cdot\tfrac12\), about 0.57 — above one half.

So Person 3 still Lines up — he discards his own bad signal. That is the start of the **information cascade**: two public Line-ups outweigh his private clue.”

**中：** 「事前各二分之一，代进去算：\(0.1785\cdot\tfrac12\) 除以 \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\)，大约是 0.57——大于二分之一。

所以第三个人还是去排队——他干脆丢掉自己的坏信号。这就是**信息级联**（信息瀑布）的起点：两个公开的排队行动，压过了他手上的私人线索。」

---

## 11 · Takeaways 结语（~2 min）

**EN:** “If everyone only used their own signal and we aggregated, private information would keep entering the public record. But in a cascade, choices are sequential: early actions become public clues, so later people can rationally ignore their own signals. Following the crowd can be rational for each individual — but bad for the group.

Same logic as Margaret’s queues, NVDA’s slide, the bank run — and homework copying. Questions?”

**中：** 「如果每个人都只用自己的信号，我们再把结果加总，私人信息就会不断累积进公共记录。但在信息级联里，选择是一个接一个的：早期的行动变成公开线索，后来的人就可能理性地忽略自己的信号。跟风对每一个人可能是理性的，对整个群体却不见得是好事。

玛嘉烈的长队、英伟达的下跌、银行挤兑、还有抄作业——背后是同一套逻辑。有问题吗？」
