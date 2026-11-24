# Herding Teaching Demo — Bilingual Verbal Script
**City University of Macau · ~20 minutes · English ＋ 中文（对照）**

Key terms / 关键术语：**\(G/B\)** = true state 真实状态（好/坏）; **\(g/b\)** = private signal 私人信号; **Line up / Drop** = action 行动（排队/离开）; **information cascade** = 信息级联（信息瀑布）; **herding** = 羊群效应.

---

## 1 · Opening 开场（~45 sec）

**EN:** “Hi everyone, I’m Ke Cheng Hsu from HKUST. Today I want to talk about herding when information isn’t perfect. We’ll start with something super everyday — queuing — then look at a few examples to build intuition, and finally use one simple model to teach Bayes’ rule. The big question is: why does following the crowd make sense for each person, and yet can still be bad for the group?”

**中：** 「大家好，我是来自香港科技大学的 Ke Cheng Hsu。今天想跟大家聊一个很日常、但背后很有意思的话题：信息不完整的时候，我们为什么会跟着人群走，也就是大家常说的“羊群效应”。我们先从生活里的排队讲起，再看几个例子，最后用一个简单的模型，带大家算一算贝叶斯规则。你会看到：对每个人来说，跟风可能都是理性的；可对一群人来说，结果未必是好事。」

---

## 2 · Margaret’s 玛嘉烈蛋挞（~2 min）

**EN:** “Margaret’s Café e Nata — it’s hidden in an alley near Sintra Square, and there’s always this long, winding queue. Honestly? I can’t really tell how it’s different from a normal egg tart. Maybe the first few people just lined up because they were bored. Then everyone else saw the queue and thought, ‘Oh, it must be good.’ I did exactly the same thing: I saw the crowd, joined for twenty minutes, and in the end it didn’t even taste that good. And that’s the puzzle, right? I had my own eyes and my own tongue — and I still got talked into the queue by the crowd.”

**中：** 「玛嘉烈蛋挞藏在新马路附近的一条小巷里，门口永远排长队。说实话，我吃不出它跟普通蛋挞有多大区别。很可能最早排队的那几个人只是闲得无聊，后面的人一看队伍这么长，就自动把它当成“好吃”的证据。我也一样：看到那么多人排，就跟着排了二十分钟，结果吃完觉得也就那样。这里就有个有意思的问题：我明明有自己的眼睛、自己的舌头，为什么最后还是被人群“劝”进了队伍？」

---

## 3 · Other examples 其他例子（~2–2.5 min）

**EN:** “Let me give you two richer stories.

First, NVIDIA’s recent slide. There was all this gossip around Jensen Huang — people call him 老黄 — the 小一小二小三 rumors. But ask the basic question: did NVIDIA’s fundamentals actually change? AI demand, earnings, guidance — mostly the same. If you trust your own analysis, the price shouldn’t move that much. But here’s what happens: the first investors sell, the price dips, and later investors see the drop and think, ‘Maybe they know something I don’t.’ If that thought beats their own read on fundamentals, they sell too. Each wave of selling pushes the price lower, and that gives the next person an even stronger reason to follow. The fall feeds on itself.

Second, a bank run. You hear a rumor that a bank is in trouble. You might not believe it. But you walk by the branch and see a long line of people withdrawing. You think, ‘Maybe they know something I don’t.’ So you line up and withdraw too. Every extra withdrawal makes the line look scarier, and gives the next person a stronger reason to run. Even if the rumor was false, the run itself can bring the bank down.

And homework copying — same logic, just smaller. The best student finishes first. The second-best compares answers and just copies. The third person — even if their own answer was right — sees two matching answers and switches to match. Each step looks reasonable on its own. Together, they form an information cascade — a 信息瀑布.”

**中：** 「讲两个更完整的例子。

第一个，最近英伟达股价那波下跌。当时网上围绕黄仁勋——大家叫他老黄——传着“小一小二小三”的八卦。但先问一句：英伟达的基本面真的变了吗？AI 需求、财报、业绩指引，大格局其实没怎么变。如果你只信自己的分析，股价不该因为八卦跌这么多。可问题是，第一批人一卖，价格一跌，后面的人看到下跌就会想：是不是别人知道什么我不知道的？如果这个念头压过了他自己的判断，他也会卖。每多一波卖出，价格就更低；价格越低，下一个人跟风的理由就越强。跌势就这么自己喂自己。

第二个，银行挤兑。你听到一个传言，说某家银行要出事。你心里未必信。但你走到分行门口，看见一条长队都在取钱。你马上会想：他们是不是知道点什么？于是你也去排队。每多一个人取钱，队伍看起来就更吓人，后面的人就更不敢不取。哪怕一开始的传言是假的，挤兑本身也可能把银行拖垮。

抄作业也一样，只是规模小一点。班里第一名先写完；第二名跟第一名对答案，一看不一样，干脆改成第一名的；第三个人本来可能写对了，但一看两个人答案一样，也开始怀疑自己，最后也改成一样的。你单看每一步，都挺合理；可合在一起，就是一条信息瀑布，也就是信息级联。」

---

## 4 · What is herding 什么是羊群效应（~1.5 min）

**EN:** “So what’s the common pattern? It’s following the crowd. You have one piece of information you know yourself — but you also see what other people do. And sometimes you follow the crowd even when your own information points the other way. Why? Because other people’s choices carry information too. When signals aren’t precise, early information can be wrong, so early actions can be wrong. And later people infer the earlier people’s information from those actions — and the error gets passed down the line. In the examples: the first people in line may have had no real reason; the first NVDA sellers may have overestimated the impact of the gossip; the first bank-run withdrawers may have overreacted to a rumor. But their actions still moved everyone after them.”

**中：** 「这三个故事背后其实是同一个模式：从众。你手里只有一条自己知道的信息，但你还能看到别人怎么选。有时候，哪怕你自己的信息指向另一边，你还是会跟着人群走。为什么？因为别人的选择本身也带信息。信号不准的时候，最早那批人的信息可能是错的，行动也可能是错的；后面的人却从这些行动里反推“他们大概知道什么”，于是错误就一路传下去。放回例子里：最早排蛋挞的可能只是无聊，最早卖英伟达的可能高估了八卦对股价的影响，最早去银行提款的可能对一个谣言反应过度——但他们的行动，照样影响了后面所有人。」

---

## 5 · Setup 设定（~1.5 min）

**EN:** “Okay, let’s simplify. One restaurant. The true state is either Good or Bad — prior one half each. People arrive one by one. Each person gets a private signal, \(g\) or \(b\), and the signal is 70% accurate. So: probability of \(g\) given \(G\) is 0.7; probability of \(b\) given \(G\) is 0.3; probability of \(g\) given \(B\) is 0.3; probability of \(b\) given \(B\) is 0.7.

And here’s the key assumption: signals are conditionally independent given the state. In plain English: once you know whether the restaurant is Good or Bad, what signal A gets doesn’t affect what signal B gets. They only look related because they’re both about the same state.

Actions? Just two: Line up or Drop. The rule is simple: if the probability of Good is above one half, Line up; if it’s below one half, Drop; if it’s exactly one half, flip a coin — each with probability one half. Our goal is to follow Person 1, Person 2, and Person 3 — and watch Person 3 throw away his own signal.”

**中：** 「我们先把场景简化。只有一家餐厅，状态要么好、要么坏，事先各一半概率。人一个一个来，每个人都会拿到一个私人信号：\(g\) 或者 \(b\)，准确率七成。也就是：餐厅真好时，七成的人拿到 \(g\)；餐厅真坏时，七成的人拿到 \(b\)。

这里有个关键假设：给定餐厅的真实状态，每个人拿到的信号是条件独立的。翻成大白话就是：餐厅好还是坏一旦定了，A 拿到什么信号，不会影响 B 拿到什么信号；他们看起来相关，只是因为大家在猜同一个状态。

每个人只有两个动作：排队，或者离开。规则也简单：如果觉得“好”的概率大于一半，就排队；小于一半，就离开；刚好一半，就抛硬币、各一半概率。接下来我们跟着前三个人走一遍，重点看第三个人：他为什么会把自己手里的信号直接丢掉。」

---

## 6 · Person 1 第一个人（~2 min）

**EN:** “Here’s the picture: area equals probability. The left half is \(G\), the right half is \(B\). The \(g\) regions cover 70% of the Good side and 30% of the Bad side.

Person 1 only has his own signal \(g\). Bayes’ rule: the probability of \(G\) given \(g\) is the Good slice over the whole \(g\) area — \(0.35\) over \(0.35+0.15\), which is \(0.7\). That’s above one half, so he Lines up. And remember: everyone else only sees his action, not his raw signal.”

**中：** 「先看这张图：面积就是概率。左半边是 \(G\)，右半边是 \(B\)；画出来的 \(g\) 区域盖住好边的七成、坏边的三成。

第一个人手上只有自己的信号 \(g\)。用贝叶斯规则算：\(\Pr(G\mid g)\) 就是 \(g\) 这块里面属于好边的比例——\(0.35\) 除以 \(0.35+0.15\)，等于 \(0.7\)。大于二分之一，所以他去排队。重点是：后面的人只看得见他的行动，看不见他拿到的信号。」

---

## 7 · Person 2 第二个人（~2 min）

**EN:** “Person 2 sees Person 1 Line up. That tells him \(s_1=g\). Now two cases.

Case one: Person 2 also gets \(s_2=g\). Two good clues — posterior above one half — he Lines up.

Case two: Person 2 gets \(s_2=b\). Now he has one good clue and one bad clue, equally strong. The joint probability under \(G\) is \(0.7\times 0.3=0.21\). The joint under \(B\) is \(0.3\times 0.7=0.21\) — that’s conditional independence at work. They’re equal, so the posterior is exactly one half. He’s indifferent — Line up or Drop with probability one half each.”

**中：** 「第二个人看到第一个人排队——这一下就等于告诉他 \(s_1=g\)。分两种情形。

如果他自己拿到 \(s_2=g\)：两条好线索，事后概率大于二分之一，直接排队。

如果他拿到的是 \(s_2=b\)：一条好线索配一条坏线索，力道一样大。算一下：在 \(G\) 之下的联合概率是 \(0.7\times 0.3=0.21\)，在 \(B\) 之下是 \(0.3\times 0.7=0.21\)——靠的就是条件独立。两边一模一样，所以事后概率刚好二分之一。他排不排都行——排队或离开各一半概率。」

---

## 8 · Person 3 — set up Bayes 写出事后概率（~2 min）

**EN:** “Now here’s the story. Two people are already lining up in front of me, and I draw a bad signal \(b\). Do I wait in line, or leave? That depends on the probability of \(G\) given \(\mathrm{LU},\mathrm{LU},b\).

So write Bayes with the actions and my signal. Numerator: probability of \(\mathrm{LU},\mathrm{LU},b\) given \(G\), times the prior. Denominator: that plus the same thing under \(B\).

And here’s the important warning: do not just replace ‘Line up’ with \(g\). Line up is an action; \(g\) is a signal. Remember, Person 2 sometimes Lines up even with \(b\). So next we need the conditional probabilities: probability of \(\mathrm{LU},\mathrm{LU},b\) given \(G\), and the same given \(B\).”

**中：** 「现在进入正题：前面已经有两个人在排队，而我自己拿到的是坏信号 \(b\)。我该跟着排，还是转身走？答案取决于 \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\)。

写贝叶斯公式，条件要用“行动加上我的信号”：分子是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\)，分母是这一项再加上 \(B\) 之下同样的一项。

这里要特别注意：不能把“排队”直接换成 \(g\)。排队是行动，\(g\) 是信号——尤其第二个人就算拿到 \(b\) 也有机会排队。接下来要算的就是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) 和 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\) 这两个条件概率。」

---

## 9 · Person 3 — conditional probabilities 条件概率（~2.5 min）

**EN:** “Why can we split it into a product? Because the earlier Line-ups depend only on \(s_1\) and \(s_2\). Given the state, those signals are independent of Person 3’s \(b\). So \(b\) is conditionally independent of the two Line-ups: probability of \((\mathrm{LU},\mathrm{LU},b)\) equals probability of \((\mathrm{LU},\mathrm{LU})\) times probability of \(b\).

Under \(G\): Person 1 Lines up only if \(s_1=g\), probability 0.7. Given that, Person 2 Lines up for sure if \(s_2=g\) — probability 0.7 — or with probability one half if \(s_2=b\) — probability 0.3. So we get \(0.7(0.7+0.3\cdot\tfrac12)=0.595\). Multiply by probability of \(b\) given \(G\), which is 0.3, and we get \(0.1785\).

Under \(B\): same logic, flipped probabilities. Person 1 Lines up only if \(s_1=g\), probability 0.3. Person 2 Lines up for sure if \(s_2=g\) — 0.3 — or half the time if \(s_2=b\) — 0.7. That gives \(0.195\). Multiply by probability of \(b\) given \(B\), which is 0.7, and we get \(0.1365\).”

**中：** 「为什么可以拆成两个概率相乘？前面两个人排不排队，只取决于 \(s_1\) 和 \(s_2\)。给定状态之后，这两个信号跟第三个人的 \(b\) 彼此独立，所以 \(b\) 跟“两人排队”条件独立：联合概率等于“两人排队”的概率乘上 \(b\) 的概率。

在 \(G\) 之下：第一个人只有拿到 \(s_1=g\) 才会排，概率 0.7。在这个前提下，第二个人拿到 \(s_2=g\)（概率 0.7）一定排；拿到 \(s_2=b\)（概率 0.3）则以一半概率排。合起来是 \(0.7(0.7+0.3\cdot\tfrac12)=0.595\)，再乘上 \(\Pr(b\mid G)=0.3\)，得到 \(0.1785\)。

在 \(B\) 之下：逻辑完全一样，只是信号概率对调——第一个人只有 \(s_1=g\) 才排（概率 0.3）；第二个人 \(s_2=g\)（0.3）必排、\(s_2=b\)（0.7）一半排。算出来是 \(0.195\)，乘上 \(\Pr(b\mid B)=0.7\)，得到 \(0.1365\)。」

---

## 10 · Person 3 — combine, decide, and why he “discards” his signal 合并决定并解释为何丢掉信号（~3.5 min）

**EN:** “Priors are equal, so just plug in: \(0.1785\cdot\tfrac12\) over \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\). That’s about 0.57 — above one half.

So Person 3 still Lines up. He throws away his own bad signal. But let’s slow down here, because this is the key step — and ‘throws away’ doesn’t mean he literally forgets it.

Person 3 draws \(b\). If he were alone — no other information — what would he do? With only \(b\), the probability of Good is 0.3. Below one half — he would Drop. His own signal says: leave.

But he’s not alone. He sees two people Line up. What do those two Line-ups actually tell him?

Person 1’s Line-up is fairly clean: Person 1 must have gotten \(g\). Person 2’s Line-up is noisier: Person 2 Lines up for sure with \(g\), but also half the time with \(b\) after a coin flip. So two Line-ups are strong evidence, but not perfect evidence.

Compare the two pieces of evidence directly. The two Line-ups are about \(0.595\) likely under Good and \(0.195\) likely under Bad — a likelihood ratio of about \(3.05\) in favor of Good. His own \(b\) has likelihood ratio \(0.3/0.7\approx 0.43\) in favor of Bad. Multiply them: \(3.05\times 0.43\approx 1.31\) in favor of Good. That gives a posterior of about \(1.31/(1+1.31)\approx 0.57\).

So the public evidence for Good is strong enough to outweigh his private bad signal. He still Lines up.

And here’s the subtle point: he doesn’t delete \(b\) from his mind. His \(b\) does lower his belief — without any signal, two Line-ups would put him at about \(0.75\); with \(b\), he’s at about \(0.57\). But \(0.57\) is still above one half, so his action looks the same as if he had ignored \(b\). That’s what we mean by ‘discarding his own signal’: he overrides it in his decision.

That’s also why this is the start of the information cascade. Person 3’s Line-up no longer reveals a good private signal. It reveals something weaker: ‘I saw two Line-ups, and even my bad signal wasn’t enough to make me leave.’ To Person 4, that looks like another confirmation. The public record becomes less informative, and the early error gets passed down.”

**中：** 「事前各二分之一，代进去算：\(0.1785\cdot\tfrac12\) 除以 \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\)，大约是 0.57——大于二分之一。

所以第三个人还是去排队——他干脆丢掉自己的坏信号。但我们在这里慢一点，因为这是关键的一步；而且“丢掉”不是说他真的把信号忘了。

第三个人拿到的是坏信号 \(b\)。如果他是一个人，没有任何其他信息，他会怎么做？只有 \(b\) 的时候，餐厅是好的概率是 0.3，低于一半，所以他应该离开。他自己的信号是叫他走的。

但他不是一个人。他看到前面两个人都在排队。那这两个“排队”到底告诉了他什么？

第一个人的排队，信息比较干净：第一个人一定是拿到了 \(g\)。第二个人的排队就有点噪声：他拿到 \(g\) 一定排；但拿到 \(b\) 的时候，他也有一半概率抛硬币去排。所以两个排队不等于两个确定的好信号，它们是强证据，但不是完美证据。

现在把两边的证据放在一起比。两个排队在“好”之下概率大约是 0.595，在“坏”之下是 0.195，似然比大约 3.05，偏向“好”。他自己的 \(b\) 似然比是 \(0.3/0.7\)，大约 0.43，偏向“坏”。乘起来：\(3.05\times 0.43\approx 1.31\)，还是偏向“好”。换成事后概率，大约 \(1.31/(1+1.31)\approx 0.57\)。

所以，公开证据强到压过了他的私人坏信号。他还是去排队。

这里有个很细但很重要的点：他不是真的把 \(b\) 从脑子里删掉。\(b\) 确实把他的信念拉低了——如果没有自己的信号，两个排队会让他觉得“好”的概率大约 0.75；有了 \(b\)，只剩大约 0.57。但 0.57 仍然大于一半，所以他的行动看起来就像他完全忽略了自己的信号。这就是我们说的“丢掉自己的信号”：不是信念上完全不算，而是决策上把它压过去了。

这也正是信息级联的起点。第三个人的排队，已经不再透露“我拿到一个好信号”。它透露的是更弱的东西：“我看到两个人排队，连我自己的坏信号都没能让我走。”到第四个人眼里，这又像是一个确认。公共记录变得越来越没有信息量，最早的那个错误就这样一路传下去。」

---

## 11 · Takeaways 结语（~2 min）

**EN:** “So here’s the takeaway. If everyone just used their own signal and we aggregated everything, private information would keep entering the public record. But in a cascade, choices are sequential. Early actions become public clues, and later people can rationally ignore their own signals. Following the crowd can be rational for each person — but bad for the group.

And it’s the same logic as Margaret’s queue, NVIDIA’s slide, the bank run — and homework copying. Questions?”

**中：** 「如果每个人都只用自己的信号，我们再把结果加总，私人信息就会不断累积进公共记录。但在信息级联里，选择是一个接一个的：早期的行动变成公开线索，后来的人就可能理性地忽略自己的信号。跟风对每一个人可能是理性的，对整个群体却不见得是好事。

玛嘉烈的长队、英伟达的下跌、银行挤兑、还有抄作业——背后是同一套逻辑。有问题吗？」
