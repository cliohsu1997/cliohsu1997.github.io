# Herding under Imperfect Information — Full Script (Final)
**City University of Macau · ~20 minutes · English ＋ 中文（对照）**

Key terms / 关键术语：**\(G/B\)** = true state 真实状态（好吃/不好吃）; **\(g/b\)** = private signal 私人信号; **Line up / Drop** = action 行动（排队/离开）; **information cascade** = 信息级联（信息瀑布）; **herding** = 羊群效应; **Bayesian updating** = 贝叶斯更新.

---

## 1 · Opening 开场 · 第1页

大家好，我是香港科技大学的徐可振。今天想跟大家聊一个咱们都经历过、但可能没细想过的事儿，就是从众，也叫羊群效应。简单说就是，当你不太确定、或者信息不够的时候，很容易跟着前面的人做一样的决定。这里有个很关键的假设：你能看见前人的选择，所以你会默认他们掌握了某些你不知道的信息，然后把自己的判断和这些信息混在一起，做决定。那为什么强调是一个一个按顺序来，而不是大家一起投票呢？我举个闺蜜的例子。

假设你朋友谈恋爱了，问你们几个：这男的值不值得嫁。要是她挨个问，闺蜜A说好，闺蜜B也说好，到你这儿，就算你亲眼看见那男的跟别的女生牵手逛街，你可能也会想，哎呀会不会是我看错了，前面俩人都说好，那我也说好呗。结果她一听，觉得这男的可以嫁。可要是她把你们拉个群，让大家同时私下发意见，你看不到别人说什么，那你看到牵手，就会直接讲出来：“他前两天还跟别的女生手牵手逛街呢。”信息就能真正汇总起来。所以这个例子的意思是：顺序决策里，前人的行动会影响后面的人，真实信息反而被盖住了；同时决策，才更能把大家的私人信息整合好。

---

## 2 · Examples 例子 · 第2页

同样的事，其实一直在我们身边发生。我举几个例子。

第一个，玛嘉烈蛋挞。澳门很有名的一家店，就在新马路拐进去的一个巷子里，门口永远排着长队。说实话，那蛋挞跟肯德基的看起来也没什么分别——好吃不好吃这件事，光看是看不出来的。可我站在门口，看见前面的人在排队，心里就想：是不是有什么我没吃出来的、特别的地方，才让这么多人一起排？最后我还是狠下心，排了二十分钟。一吃，还不如肯德基。那问题就来了：我为什么会排？因为我看见前面的人在排队，就默认他们一定知道一些我不知道的事，比如这蛋挞到底好不好吃。这个从别人行为里推断出来的信息，最后压过了我自己的判断——我明明觉得它跟肯德基没啥区别。这就是羊群效应最关键的地方：别人的行动，成了我的信息来源。

第二个，英伟达前阵子那波暴跌，起因是一条传言，说老黄的“小三”是间谍。先问一句，你卖，真的是因为相信这条传言、觉得它对基本面有影响吗？英伟达基本面变了吗？AI需求、财报、业绩指引，这些大的东西基本都没动。如果你自己都不信这个传言，那至少在当时，基本面并没有实质变化，你会觉得这就是一波情绪。可现实是，第一批人一卖，价格一跌，后面的人一看跌了，心里就开始犯嘀咕：是不是有人知道什么我不知道的？是不是我低估了，比如换个CEO对公司的影响？这个念头一旦压过自己的判断，他也跟着卖。每多一波卖出，价格就再低一点；价格越低，下一个人跟风的理由就越硬。跌势就这么自己喂自己。

第三个，银行挤兑。你听到一个传言，说某家银行要出事，你未必信。可你走到分行门口，看见一长队人在取钱，你也会想：他们是不是知道点什么？于是你也去排。每多一个人取钱，队伍看起来就更吓人，后面的人就更不敢不取。哪怕一开始的传言是假的，挤兑本身也可能把银行拖垮。

再小一点的，抄作业。班里第一名先写完，但答案是错的；第二名对一下答案，也没多想，照着抄了，一样是错的；第三个人本来写对了，可一看前面两个人答案一模一样，心里先虚了，最后还是改成了跟他们一样的错答案。

你看这几个例子，讲的其实是同一件事。单拎出每一步来看，都不离谱——看见人排队，我就跟着排；看见价格跌，我心里就发慌；看见别人去取钱，我也去取。谁都会这么想，很正常。可问题就在这儿：一个人这么想没事，一千个人都这么想、还一个看着一个，就出事了。前面的人怎么做，后面的人就把它当成线索；后面的人再怎么做，又成了更后面的人的线索。一层一层传下去，越传越离谱，看着看着，就离事实越来越远了。这东西有个名字，叫信息级联。听着挺学术，其实就一句话：大家都在看别人怎么办，看着看着，就离事实越来越远了。

---

## 3 · Setup 设定（~1.5 min）

**EN:** “Okay, let's simplify. One restaurant. The true state is either Good or Bad — one half each, to start. People show up one at a time. Each person gets a private signal, \(g\) or \(b\), and that signal is 70% accurate. So: the probability of \(g\) given \(G\) is 0.7; the probability of \(b\) given \(G\) is 0.3; the probability of \(g\) given \(B\) is 0.3; and the probability of \(b\) given \(B\) is 0.7.

Here's the key assumption: given the state, the signals are conditionally independent. In plain English — once you know whether the restaurant is Good or Bad, the signal A gets has nothing to do with the signal B gets. They only look related because they're both about the same state.

And the actions? Just two: Line up or Drop. The rule is simple: if the probability of Good is above one half, Line up; below one half, Drop; exactly one half, flip a coin — each with probability one half. Our goal is to follow Person 1, Person 2, and Person 3 — and watch Person 3 throw away his own signal.”

**中：** 「我们先把场景简化。只有一家餐厅，真实状态要么是“好吃”，要么是“不好吃”，事先各有一半概率。人一个一个地来，每个人都会拿到一个私人信号：\(g\) 或者 \(b\)，准确率七成。也就是说：餐厅真的好吃时，七成的人拿到 \(g\)；餐厅真的不好吃时，七成的人拿到 \(b\)。

这里有个关键假设：给定真实状态，每个人拿到的信号之间是条件独立的。说人话就是——餐厅到底好吃还是不好吃一旦定下来，A 拿到什么信号，不会影响 B 拿到什么信号；它们看上去相关，只是因为大家都在猜同一件事。

每个人只有两个动作：排队，或者离开。规则很简单：觉得“好吃”的概率大于一半，就排队；小于一半，就离开；正好一半，就抛硬币，各一半概率。接下来，我们跟着前三个人走一遍，重点看第三个人：他为什么会在决策时把自己的信号压过去。」

---

## 4 · Person 1 第一个人（~2 min）

**EN:** “Here's the picture: area equals probability. The left half is \(G\), the right half is \(B\). And the \(g\) regions cover 70% of the Good side and 30% of the Bad side.

Person 1 has only his own signal \(g\). By Bayes' rule, the probability of \(G\) given \(g\) is just the Good slice over the whole \(g\) area — \(0.35\) over \(0.35+0.15\), which comes out to \(0.7\). That's above one half — so he Lines up. And remember: everyone else only sees his action, not his raw signal.”

**中：** 「先看这张图：面积就是概率。左半边是 \(G\)，右半边是 \(B\)；而 \(g\) 这块区域，盖住了“好吃”那边的七成、“不好吃”那边的三成。

第一个人手上只有自己的信号 \(g\)。用贝叶斯规则来算：\(\Pr(G\mid g)\) 就是 \(g\) 这块区域里属于“好吃”那部分的占比——\(0.35\) 除以 \(0.35+0.15\)，等于 \(0.7\)。大于二分之一，所以他去排队。记住：后面的人只看得见他的行动，看不见他拿到的信号。」

---

## 5 · Person 2 第二个人（~2 min）

**EN:** “Person 2 sees Person 1 line up — which tells him \(s_1=g\). Now there are two cases.

Case one: Person 2 also gets \(s_2=g\). Two good clues — posterior above one half — so he Lines up.

Case two: Person 2 gets \(s_2=b\). Now it's one good clue against one bad clue, equally strong. The joint probability under \(G\) is \(0.7\times 0.3=0.21\); under \(B\) it's \(0.3\times 0.7=0.21\) — that's conditional independence at work. Equal, so the posterior is exactly one half. He's indifferent — Line up or Drop, one half each.”

**中：** 「第二个人看到第一个人排了队——这等于告诉他 \(s_1=g\)。分两种情形。

第一种：如果他自己也拿到 \(s_2=g\)，两条正面线索，事后概率大于一半，直接排队。

第二种：如果他拿到 \(s_2=b\)，那就是一条正面线索配一条负面线索，力道一样大。算一下：在 \(G\) 之下，联合概率是 \(0.7\times 0.3=0.21\)，在 \(B\) 之下是 \(0.3\times 0.7=0.21\)——这正是条件独立在起作用。两边一样，所以事后概率正好是二分之一。他排不排都行——排队或离开各一半概率。」

---

## 6 · Person 3 — set up Bayes 写出事后概率（~2 min）

**EN:** “Now here's the story. Two people are already lining up in front of me, and I draw a bad signal \(b\). Do I stay, or do I leave? That all depends on the probability of \(G\) given \(\mathrm{LU},\mathrm{LU},b\).

So let's write Bayes' rule with the actions and my signal. Numerator: the probability of \(\mathrm{LU},\mathrm{LU},b\) given \(G\), times the prior. Denominator: that same term, plus the matching one under \(B\).

And here's the important warning: don't just swap 'Line up' for \(g\). Line up is an action; \(g\) is a signal. Remember — Person 2 sometimes lines up even with \(b\). So next we need two conditional probabilities: the probability of \(\mathrm{LU},\mathrm{LU},b\) given \(G\), and the same given \(B\).”

**中：** 「现在进入正题：前面已经有两个人排上了队，而我自己拿到的是负面信号 \(b\)。我是该跟着排，还是转身走？这取决于 \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\)。

用贝叶斯公式时，条件要写成“前面的行动加上我的信号”：分子是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\)，分母是这一项再加上 \(B\) 之下同样的一项。

这里要特别注意：不能把“排队”直接当成 \(g\)。排队是行动，\(g\) 是信号——第二个人就算拿到 \(b\)，也有可能去排队。所以接下来要算的，是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) 和 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\) 这两个条件概率。」

---

## 7 · Person 3 — conditional probabilities 条件概率（~2.5 min）

**EN:** “Why can we split it into a product? Because the earlier Line-ups depend only on \(s_1\) and \(s_2\). Given the state, those signals are independent of Person 3's \(b\). So \(b\) is conditionally independent of the two Line-ups: the probability of \((\mathrm{LU},\mathrm{LU},b)\) equals the probability of \((\mathrm{LU},\mathrm{LU})\) times the probability of \(b\).

Under \(G\): Person 1 lines up only if \(s_1=g\), probability 0.7. Given that, Person 2 lines up for sure if \(s_2=g\) — probability 0.7 — or with probability one half if \(s_2=b\) — probability 0.3. So we get \(0.7(0.7+0.3\cdot\tfrac12)=0.595\). Multiply by the probability of \(b\) given \(G\), which is 0.3, and we get \(0.1785\).

Under \(B\): same logic, with the probabilities flipped. Person 1 lines up only if \(s_1=g\), probability 0.3. Person 2 lines up for sure if \(s_2=g\) — 0.3 — or half the time if \(s_2=b\) — 0.7. That gives \(0.195\). Multiply by the probability of \(b\) given \(B\), which is 0.7, and we get \(0.1365\).”

**中：** 「为什么可以拆成两个概率相乘？因为前面两个人排不排队，只取决于 \(s_1\) 和 \(s_2\)。给定状态之后，这两个信号与第三个人的 \(b\) 彼此独立，所以 \(b\) 与“两人排队”这一事件条件独立：联合概率等于“两人排队”的概率乘上 \(b\) 的概率。

在 \(G\) 之下：第一个人只有拿到 \(s_1=g\) 才会排，概率是 \(0.7\)。在这个前提下，第二个人拿到 \(s_2=g\)（概率 \(0.7\)）一定会排；拿到 \(s_2=b\)（概率 \(0.3\)）则以一半概率排。合起来是 \(0.7(0.7+0.3\cdot\tfrac12)=0.595\)，再乘上 \(\Pr(b\mid G)=0.3\)，得到 \(0.1785\)。

在 \(B\) 之下：逻辑一样，只是信号概率对调——第一个人只有 \(s_1=g\) 才排（概率 \(0.3\)）；第二个人 \(s_2=g\)（\(0.3\)）必排、\(s_2=b\)（\(0.7\)）则以一半概率排。算出来是 \(0.195\)，乘上 \(\Pr(b\mid B)=0.7\)，得到 \(0.1365\)。」

---

## 8 · Person 3 — combine, decide, and why he "discards" his signal 合并决定并解释为何丢掉信号（~3.5 min）

**EN:** “The priors are equal, so we just plug in: \(0.1785\cdot\tfrac12\) over \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\). That comes out to about 0.57 — above one half.

So Person 3 still lines up. He discards his own bad signal — the information in the previous players' actions outweighs his private signal. But let's slow down here, because this is the key step — and 'discards' doesn't mean he literally forgets it.

Person 3 draws \(b\). If he were alone — no other information — what would he do? With only \(b\), the probability of Good is 0.3. Below one half — so he'd drop. His own signal says: leave.

But he's not alone. He sees two people line up. And on the slide you can see what those two Line-ups alone would tell him: \(\Pr(G\mid \mathrm{LU},\mathrm{LU})=0.595/(0.595+0.195)\approx 0.75\). That's strong evidence for Good.

So put the three numbers side by side. His private signal alone: 0.3 — he'd leave. The two Line-ups alone: 0.75 — he'd line up. Both together: 0.57 — still above one half, so he lines up.

And here's the subtle point: he doesn't delete \(b\) from his mind. \(b\) does pull his belief down — from 0.75 to 0.57. But 0.57 is still above one half, so his action looks exactly the same as if he'd ignored \(b\). That's what we mean by 'discarding his own signal': he overrides it in his decision.

And that's why this is the start of the information cascade. Person 3's line-up no longer reveals a good private signal. It reveals something weaker: 'I saw two line-ups, and even my bad signal wasn't enough to make me leave.' To Person 4, that looks like one more confirmation. The public record becomes less and less informative — and the early error keeps getting passed down.”

**中：** 「先验一样，直接代进去：\(0.1785\cdot\tfrac12\) 除以 \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\)，大约是 \(0.57\)——大于二分之一。

所以第三个人还是去排队。他把自己那个负面信号压过去了：从前两个人行动里推出来的信息，盖过了他的私人信号。不过这里我们慢一点，因为这是关键的一步；而且“丢掉”并不是说他真的把信号忘了。

第三个人拿到的是负面信号 \(b\)。要是他一个人、没有别的信息，他会怎么做？只有 \(b\) 的时候，餐厅“好吃”的概率是 \(0.3\)，低于一半，那他应该走。他自己的信号分明是叫他走的。

但他不是一个人。他看到前面两个人都在排队。幻灯片上可以看到，光凭这两个排队，他判断“好吃”的概率是 \(\Pr(G\mid \mathrm{LU},\mathrm{LU})=0.595/(0.595+0.195)\approx 0.75\)——这是很强的“好吃”的证据。

现在把三个数摆在一起：只有私人信号，是 \(0.3\)——他会走；只看两个排队，是 \(0.75\)——他会排；两者加在一起，是 \(0.57\)——仍然大于一半，所以还是排。

这里有个很细、但很重要的点：他并不是真的把 \(b\) 从脑子里删掉。\(b\) 确实把他的信念拉低了——从 \(0.75\) 拉到 \(0.57\)。但 \(0.57\) 仍然大于一半，所以他的行动看起来就像完全忽略了自己的信号。这就是我们说的“丢掉自己的信号”：不是信念上完全不算它，而是在决策上把它压了过去。

这也正是信息级联的起点。第三个人的排队，已经不再透露“我拿到了一个好信号”。它透露的是更弱的东西：“我看到两个人排队，连我自己那个负面信号都没能让我走。”在第四个人眼里，这又像是一次确认。公共记录变得越来越没有信息量，最早的那点错误，就这样一路传了下去。」

---

## 9 · Takeaways 结语（~2 min）

**EN:** “So here's the takeaway. If everyone just used their own signal, and we aggregated all of them, private information would keep feeding into the public record. But in a cascade, choices come one after another. Early actions become public clues — and the people who come later can rationally ignore their own signals. Following the crowd can be rational for each person — and still bad for the group.

And it's the same logic as Margaret's queue, NVIDIA's crash, the bank run — and homework copying. Any questions?”

**中：** 「所以结论是：如果每个人都只用自己手里的信号，我们再把这些结果汇总起来，私人信息就会源源不断地进入公共记录。但在信息级联里，选择是一个接一个发生的：早期的行动变成了公开线索，后来的人也就可能理性地忽略掉自己的信号。跟风，对每个人也许都是理性的，对整个群体却未必是好事。

玛嘉烈的长队、英伟达的暴跌、银行挤兑，还有抄作业——背后都是同一套逻辑。有问题吗？」
