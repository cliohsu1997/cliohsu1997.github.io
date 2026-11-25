# Herding under Imperfect Information — Full Script (Final)
**City University of Macau · ~20 minutes · English ＋ 中文（对照）**

Key terms / 关键术语：**\(G/B\)** = true state 真实状态（好吃/不好吃）; **\(g/b\)** = private signal 私人信号; **Line up / Drop** = action 行动（排队/离开）; **information cascade** = 信息级联（信息瀑布）; **herding** = 羊群效应; **Bayesian updating** = 贝叶斯更新.

---

## 1 · Opening 开场（~45 sec）

**EN:** “Hi everyone, I'm Ke Cheng Hsu from HKUST. Today I want to talk about herding when information isn't perfect. What does that mean — 'information isn't perfect'? It means nobody knows the true state of things for sure: whether the restaurant is really good, whether the bank is really safe, or whether the stock is really worth holding. Each of us only gets a noisy private signal — a hint, not the truth — and we can't see what others privately know; we only see what they do. So every decision is made under incomplete information. We'll start with something really everyday — queuing — then look at a few examples to build intuition, and finally use one simple model to walk through Bayesian updating. The big question is: why does following the crowd make sense for each person, and yet can still be bad for the group?”

**中：** 「大家好，我是来自香港科技大学的 Ke Cheng Hsu。今天想和大家聊一个特别日常、背后却很有意思的话题：当信息不完整的时候，我们为什么会跟着人群走——也就是大家常说的“羊群效应”。那什么叫“信息不完整”？就是说，没有人能确切知道事情的真实状态：这家餐厅到底好不好、这家银行到底安不安全、这只股票到底值不值得拿。我们每个人手里只有一条带噪声的私人信号——它只是个线索，不是真相；而且我们也看不到别人私下知道什么，只能看到他们怎么做。所以每一个决定，都是在信息不完整的情况下做出的。我们先从排队这种生活场景讲起，再看几个例子建立直觉，最后用一个简单的模型，来带大家理解贝叶斯更新，还有——为什么对每个人来说，跟风都是理性的，但放在一群人身上，结果却未必是好事？」

---

## 2 · Margaret's 玛嘉烈蛋挞（~2 min）

**EN:** “Margaret's Café e Nata is a well-known egg-tart shop here in Macau — tucked in an alley just off the main road, with a long line outside all day. Honestly? To me it looks no different from an ordinary egg tart. And plenty of people who've tried it say the same: too sweet, too oily — they'd rather have Lord Stow's, or one of those no-name little shops. The queue is basically guidebook hype. My guess? The first few people lined up just because they had nothing better to do; then everyone after them sees how long the line is and thinks, 'Well, it must be good.' Same for me — I saw the crowd, jumped in, and stood there for twenty minutes. Took a bite and thought… nothing special. So here's the real question: with no line, I probably wouldn't have bought one at all — I didn't even think it was worth it myself. So why did the line still outweigh my own judgment?”

**中：** 「玛嘉烈蛋挞是澳门一家很有名的蛋挞店，藏在新马路拐进去的一条小巷子里，门口永远排着一支长队。说实话，我觉得它看起来跟普通蛋挞没有太大差别。很多吃过的人也说它又甜又油，还不如安德鲁蛋挞，或者那些不知名的小店——排队基本上就是被旅游攻略炒起来的。我猜最早那几个人可能也是闲着没事、随便排一排；后面的人一看队伍这么长，就觉得“那肯定好吃”。我也一样，一看人这么多，就跟着排了二十分钟。结果咬一口，发现……也没什么特别的。所以真正的问题是：要是门口没有这条长队，我大概率不会买——我明明自己觉得不值，可为什么最后这条队伍还是压过了我自己的判断？」

---

## 3 · Other examples 其他例子（~2–2.5 min）

**EN:** “Let me give you two more — the same thing keeps happening all around us.

First, NVIDIA's recent crash — it started with a rumor that Jensen Huang — Lao Huang, as people call him — had a mistress named Huang Le, who was a spy. But ask the basic question: are you really selling because you think his mistress being a spy changes the fundamentals? Did NVIDIA's fundamentals change? AI demand, earnings, guidance — the big things barely moved. If you yourself don't even believe the rumor, then, with the fundamentals basically unchanged, you'd say this is just sentiment. But here's what actually happens. The first investors sell, the price dips, and the next wave sees the drop and thinks, 'Maybe they know something I don't — maybe I'm underestimating something, like the impact of a CEO change.' Once that thought beats their own judgment, they sell too. Each wave of selling pushes the price lower — and that gives the next person an even stronger reason to follow. The fall feeds on itself.

Second, a bank run. You hear a rumor that a bank is in trouble. You might not believe it. But you walk by the branch and see a long line of people withdrawing. You think, 'Maybe they know something I don't.' So you line up and withdraw too. Every extra withdrawal makes the line look scarier, and gives the next person a stronger reason to run. Even if the rumor was false, the run itself can bring the bank down.

And homework copying — same logic, just smaller. The best student finishes first — but gets the answer wrong. The second-best checks answers and just copies — also wrong. The third person, whose own answer was actually right, sees two matching answers, loses confidence, and switches to the wrong one. Each step looks reasonable on its own. Together, they form an information cascade — a 信息瀑布.”

**中：** 「再讲两个例子——同样的例子，其实不断发生在我们生活里。

第一个，英伟达前阵子那波暴跌，起因就是一条传言——老黄（黄仁勋）的“小三”黄乐是间谍。但先问一句：你卖，真的是因为觉得老黄的小三是间谍、这对基本面有什么影响吗？英伟达的基本面变了吗？AI 需求、财报、业绩指引，这些大的东西基本上都没怎么动。如果你自己根本不信这个传言，照理来说，你会觉得这其实只是情绪的问题——在基本面没怎么变的情况下。可现实是：第一批人一卖，价格一跌，后面的人一看跌了，心里就犯嘀咕——是不是有人知道什么我不知道的事？是不是我低估了，比如换 CEO 对公司的影响？类似这样的念头一旦压过自己的判断，他也跟着卖。每多一波卖出，价格就再低一点；价格越低，下一个人跟风的理由就越硬。跌势就这么自己喂自己。

第二个，银行挤兑。你听到一个传言，说某家银行要出事。你未必信。可你走到分行门口，看见一长队人都在取钱，你也会想：他们是不是知道点什么？于是你也去排队。每多一个人取钱，队伍看起来就更吓人，后面的人就更不敢不取。哪怕一开始的传言是假的，挤兑本身也可能把银行拖垮。

抄作业也一样，只是规模小一点。班里第一名先写完——但答案是错的；第二名对一下答案，也没多想，直接照着抄了——同样是错的；第三个人本来写对了，可一看前面两个人的答案一模一样，心里先虚了，最后还是改成了跟他们一样的错答案。单看每一步，都挺合理；可合在一起，就成了一条信息瀑布，也就是信息级联。」

---

## 4 · What is herding 什么是羊群效应（~1.5 min）

**EN:** “So what's the common pattern? It's following the crowd. You've got one piece of information — your own — but you also see what everyone else does. And sometimes you follow the crowd even when your own information points the other way. Why? Because other people's choices carry information too. When signals aren't precise, early information can be wrong — so early actions can be wrong. And later people infer the earlier people's information from those actions — and the error gets passed down the line. Look at the examples: the first people in line may have had no real reason; the first NVDA sellers may have overreacted to the gossip; the first bank-run withdrawers may have overreacted to a rumor. But their actions still moved everyone after them.”

**中：** 「这些故事背后，其实是同一个模式：从众。你手里只有一条信息——就是你自己知道的那些；与此同时，你还能看到别人怎么选。有时候，哪怕自己的信号指向相反的方向，你还是会跟着人群走。为什么？因为别人的选择本身也带着信息。信号不准确的时候，最早那批人的信息可能是错的，行动也可能是错的；后面的人却从这些行动里反推“他们大概知道些什么”，错误就这样一路传了下去。放回例子里看：最早排蛋挞的人可能只是无聊；最早抛英伟达的人可能高估了八卦的分量；最早去银行取钱的人可能对一个谣言反应过度——但他们的行动，照样影响了后面的所有人。」

---

## 5 · Setup 设定（~1.5 min）

**EN:** “Okay, let's simplify. One restaurant. The true state is either Good or Bad — prior one half each. People arrive one by one. Each person gets a private signal, \(g\) or \(b\), and the signal is 70% accurate. So: probability of \(g\) given \(G\) is 0.7; probability of \(b\) given \(G\) is 0.3; probability of \(g\) given \(B\) is 0.3; probability of \(b\) given \(B\) is 0.7.

Here's the key assumption: signals are conditionally independent given the state. In plain English — once you know whether the restaurant is Good or Bad, what signal A gets doesn't affect what signal B gets. They only look related because they're both about the same state.

Actions? Just two: Line up or Drop. The rule is simple: if the probability of Good is above one half, Line up; below one half, Drop; exactly one half, flip a coin — each with probability one half. Our goal is to follow Person 1, Person 2, and Person 3 — and watch Person 3 throw away his own signal.”

**中：** 「我们先把场景简化。只有一家餐厅，真实状态要么是“好吃”，要么是“不好吃”，事先各有一半概率。人一个一个地来，每个人都会拿到一个私人信号：\(g\) 或者 \(b\)，准确率七成。也就是说：餐厅真的好吃时，七成的人拿到 \(g\)；餐厅真的不好吃时，七成的人拿到 \(b\)。

这里有个关键假设：给定真实状态，每个人拿到的信号之间是条件独立的。说人话就是——餐厅到底好吃还是不好吃一旦定下来，A 拿到什么信号，不会影响 B 拿到什么信号；它们看上去相关，只是因为大家都在猜同一件事。

每个人只有两个动作：排队，或者离开。规则很简单：觉得“好吃”的概率大于一半，就排队；小于一半，就离开；正好一半，就抛硬币，各一半概率。接下来，我们跟着前三个人走一遍，重点看第三个人：他为什么会在决策时把自己的信号压过去。」

---

## 6 · Person 1 第一个人（~2 min）

**EN:** “Here's the picture: area equals probability. Left half is \(G\), right half is \(B\). The \(g\) regions cover 70% of the Good side and 30% of the Bad side.

Person 1 only has his own signal \(g\). Bayes' rule: the probability of \(G\) given \(g\) is the Good slice over the whole \(g\) area — \(0.35\) over \(0.35+0.15\), which is \(0.7\). Above one half — so he Lines up. And remember: everyone else only sees his action, not his raw signal.”

**中：** 「先看这张图：面积就是概率。左半边是 \(G\)，右半边是 \(B\)；而 \(g\) 这块区域，盖住了“好吃”那边的七成、“不好吃”那边的三成。

第一个人手上只有自己的信号 \(g\)。用贝叶斯规则来算：\(\Pr(G\mid g)\) 就是 \(g\) 这块区域里属于“好吃”那部分的占比——\(0.35\) 除以 \(0.35+0.15\)，等于 \(0.7\)。大于二分之一，所以他去排队。记住：后面的人只看得见他的行动，看不见他拿到的信号。」

---

## 7 · Person 2 第二个人（~2 min）

**EN:** “Person 2 sees Person 1 Line up. That tells him \(s_1=g\). Two cases.

Case one: Person 2 also gets \(s_2=g\). Two good clues — posterior above one half — he Lines up.

Case two: Person 2 gets \(s_2=b\). Now he has one good clue and one bad clue, equally strong. The joint probability under \(G\) is \(0.7\times 0.3=0.21\). The joint under \(B\) is \(0.3\times 0.7=0.21\) — that's conditional independence at work. Equal, so the posterior is exactly one half. He's indifferent — Line up or Drop with probability one half each.”

**中：** 「第二个人看到第一个人排了队——这等于告诉他 \(s_1=g\)。分两种情形。

第一种：如果他自己也拿到 \(s_2=g\)，两条正面线索，事后概率大于一半，直接排队。

第二种：如果他拿到 \(s_2=b\)，那就是一条正面线索配一条负面线索，力道一样大。算一下：在 \(G\) 之下，联合概率是 \(0.7\times 0.3=0.21\)，在 \(B\) 之下是 \(0.3\times 0.7=0.21\)——这正是条件独立在起作用。两边一样，所以事后概率正好是二分之一。他排不排都行——排队或离开各一半概率。」

---

## 8 · Person 3 — set up Bayes 写出事后概率（~2 min）

**EN:** “Now here's the story. Two people are already lining up in front of me, and I draw a bad signal \(b\). Do I wait, or leave? That depends on the probability of \(G\) given \(\mathrm{LU},\mathrm{LU},b\).

So write Bayes with the actions and my signal. Numerator: probability of \(\mathrm{LU},\mathrm{LU},b\) given \(G\), times the prior. Denominator: that plus the same thing under \(B\).

And here's the important warning: don't just replace 'Line up' with \(g\). Line up is an action; \(g\) is a signal. Remember — Person 2 sometimes Lines up even with \(b\). So next we need the conditional probabilities: probability of \(\mathrm{LU},\mathrm{LU},b\) given \(G\), and the same given \(B\).”

**中：** 「现在进入正题：前面已经有两个人排上了队，而我自己拿到的是负面信号 \(b\)。我是该跟着排，还是转身走？这取决于 \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\)。

用贝叶斯公式时，条件要写成“前面的行动加上我的信号”：分子是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\)，分母是这一项再加上 \(B\) 之下同样的一项。

这里要特别注意：不能把“排队”直接当成 \(g\)。排队是行动，\(g\) 是信号——第二个人就算拿到 \(b\)，也有可能去排队。所以接下来要算的，是 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) 和 \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\) 这两个条件概率。」

---

## 9 · Person 3 — conditional probabilities 条件概率（~2.5 min）

**EN:** “Why can we split it into a product? Because the earlier Line-ups depend only on \(s_1\) and \(s_2\). Given the state, those signals are independent of Person 3's \(b\). So \(b\) is conditionally independent of the two Line-ups: probability of \((\mathrm{LU},\mathrm{LU},b)\) equals probability of \((\mathrm{LU},\mathrm{LU})\) times probability of \(b\).

Under \(G\): Person 1 Lines up only if \(s_1=g\), probability 0.7. Given that, Person 2 Lines up for sure if \(s_2=g\) — probability 0.7 — or with probability one half if \(s_2=b\) — probability 0.3. So we get \(0.7(0.7+0.3\cdot\tfrac12)=0.595\). Multiply by probability of \(b\) given \(G\), which is 0.3 — and we get \(0.1785\).

Under \(B\): same logic, flipped probabilities. Person 1 Lines up only if \(s_1=g\), probability 0.3. Person 2 Lines up for sure if \(s_2=g\) — 0.3 — or half the time if \(s_2=b\) — 0.7. That gives \(0.195\). Multiply by probability of \(b\) given \(B\), which is 0.7 — and we get \(0.1365\).”

**中：** 「为什么可以拆成两个概率相乘？因为前面两个人排不排队，只取决于 \(s_1\) 和 \(s_2\)。给定状态之后，这两个信号与第三个人的 \(b\) 彼此独立，所以 \(b\) 与“两人排队”这一事件条件独立：联合概率等于“两人排队”的概率乘上 \(b\) 的概率。

在 \(G\) 之下：第一个人只有拿到 \(s_1=g\) 才会排，概率是 \(0.7\)。在这个前提下，第二个人拿到 \(s_2=g\)（概率 \(0.7\)）一定会排；拿到 \(s_2=b\)（概率 \(0.3\)）则以一半概率排。合起来是 \(0.7(0.7+0.3\cdot\tfrac12)=0.595\)，再乘上 \(\Pr(b\mid G)=0.3\)，得到 \(0.1785\)。

在 \(B\) 之下：逻辑一样，只是信号概率对调——第一个人只有 \(s_1=g\) 才排（概率 \(0.3\)）；第二个人 \(s_2=g\)（\(0.3\)）必排、\(s_2=b\)（\(0.7\)）则以一半概率排。算出来是 \(0.195\)，乘上 \(\Pr(b\mid B)=0.7\)，得到 \(0.1365\)。」

---

## 10 · Person 3 — combine, decide, and why he "discards" his signal 合并决定并解释为何丢掉信号（~3.5 min）

**EN:** “Priors are equal, so just plug in: \(0.1785\cdot\tfrac12\) over \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\). That's about 0.57 — above one half.

So Person 3 still Lines up. He discards his own bad signal — the information from the previous players' actions outweighs his private signal. But let's slow down here, because this is the key step — and 'discards' doesn't mean he literally forgets it.

Person 3 draws \(b\). If he were alone — no other information — what would he do? With only \(b\), the probability of Good is 0.3. Below one half — he would Drop. His own signal says: leave.

But he's not alone. He sees two people Line up. And on the slide you can see what those two Line-ups alone would tell him: \(\Pr(G\mid \mathrm{LU},\mathrm{LU})=0.595/(0.595+0.195)\approx 0.75\). That's strong evidence for Good.

So put the three numbers side by side. Only his private signal: 0.3 — he'd leave. Only the two Line-ups: 0.75 — he'd line up. Both together: 0.57 — still above one half, so he lines up.

And here's the subtle point: he doesn't delete \(b\) from his mind. \(b\) does lower his belief — from 0.75 down to 0.57. But 0.57 is still above one half, so his action looks the same as if he had ignored \(b\). That's what we mean by 'discarding his own signal': he overrides it in his decision.

And that's why this is the start of the information cascade. Person 3's Line-up no longer reveals a good private signal. It reveals something weaker: 'I saw two Line-ups, and even my bad signal wasn't enough to make me leave.' To Person 4, that looks like another confirmation. The public record becomes less informative — and the early error gets passed down.”

**中：** 「先验一样，直接代进去：\(0.1785\cdot\tfrac12\) 除以 \(0.1785\cdot\tfrac12+0.1365\cdot\tfrac12\)，大约是 \(0.57\)——大于二分之一。

所以第三个人还是去排队。他把自己那个负面信号压过去了：从前两个人行动里推出来的信息，盖过了他的私人信号。不过这里我们慢一点，因为这是关键的一步；而且“丢掉”并不是说他真的把信号忘了。

第三个人拿到的是负面信号 \(b\)。要是他一个人、没有别的信息，他会怎么做？只有 \(b\) 的时候，餐厅“好吃”的概率是 \(0.3\)，低于一半，那他应该走。他自己的信号分明是叫他走的。

但他不是一个人。他看到前面两个人都在排队。幻灯片上可以看到，光凭这两个排队，他判断“好吃”的概率是 \(\Pr(G\mid \mathrm{LU},\mathrm{LU})=0.595/(0.595+0.195)\approx 0.75\)——这是很强的“好吃”的证据。

现在把三个数摆在一起：只有私人信号，是 \(0.3\)——他会走；只看两个排队，是 \(0.75\)——他会排；两者加在一起，是 \(0.57\)——仍然大于一半，所以还是排。

这里有个很细、但很重要的点：他并不是真的把 \(b\) 从脑子里删掉。\(b\) 确实把他的信念拉低了——从 \(0.75\) 拉到 \(0.57\)。但 \(0.57\) 仍然大于一半，所以他的行动看起来就像完全忽略了自己的信号。这就是我们说的“丢掉自己的信号”：不是信念上完全不算它，而是在决策上把它压了过去。

这也正是信息级联的起点。第三个人的排队，已经不再透露“我拿到了一个好信号”。它透露的是更弱的东西：“我看到两个人排队，连我自己那个负面信号都没能让我走。”在第四个人眼里，这又像是一次确认。公共记录变得越来越没有信息量，最早的那点错误，就这样一路传了下去。」

---

## 11 · Takeaways 结语（~2 min）

**EN:** “So here's the takeaway. If everyone just used their own signal and we aggregated everything, private information would keep entering the public record. But in a cascade, choices are sequential. Early actions become public clues — and later people can rationally ignore their own signals. Following the crowd can be rational for each person — but bad for the group.

And it's the same logic as Margaret's queue, NVIDIA's crash, the bank run — and homework copying. Questions?”

**中：** 「所以结论是：如果每个人都只用自己手里的信号，我们再把这些结果汇总起来，私人信息就会源源不断地进入公共记录。但在信息级联里，选择是一个接一个发生的：早期的行动变成了公开线索，后来的人也就可能理性地忽略掉自己的信号。跟风，对每个人也许都是理性的，对整个群体却未必是好事。

玛嘉烈的长队、英伟达的暴跌、银行挤兑，还有抄作业——背后都是同一套逻辑。有问题吗？」
