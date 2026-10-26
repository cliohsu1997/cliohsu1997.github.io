# Return policy in e-commerce (about 20 minutes)

Paper: "Designing Return Policy in E-Commerce: A Trade-off between Purchase and Return Efficiency."

Spoken script for the middle of a 30-minute interview. Do not call it a job-market paper. Every number below is already in the CV or the research statement. If someone asks for a moment, an equation, or a figure, go to the slide. Do not make one up.

A straight read is about 11 minutes. Use the other half of the 20 minutes to draw the two losses on the board and to stop when someone asks a question. If you are short on time, skip "How the estimation is organized" and keep the trade-off and the ranking.

---

## 1. The decision

I study return policy for one women's apparel retailer on Taobao.

A shopper buys a piece of clothing without knowing whether it fits. Return rates in these categories are about 20 to 30 percent, so a large share of purchases come back. The seller has to decide, before that uncertainty is resolved, who pays the cost of sending the good back.

There are two rules I see the seller actually use. Under automatic coverage, the seller pays the return shipping fee for every buyer. Under optional coverage, the buyer can purchase that protection, and a buyer who does not purchase it bears the shipping cost of a return. I also study a menu the seller does not currently offer: a lower price, plus a restocking fee of about 10 to 15 percent if the good comes back.

I rank these by the seller's profit, by consumer surplus, and by the sum of the two. The ranking is not the same in every category. That is the result. I will spend the time on why.

## 2. Two margins, not one

It is tempting to say a stricter return rule is better because it stops wasteful returns. Some returns should not happen. The match was fine, and the good came back because return shipping was free. A stricter rule fixes that. Call this the return margin. It is about efficiency after the purchase.

There is a second margin, and it moves in the other direction. If fewer goods come back, the seller keeps more of whatever price was charged. A higher price becomes more attractive. That higher price can shut out a shopper who would have bought and kept the good. The purchase was worth making, and the stricter rule prevented it. Call this the purchase margin. It is about efficiency at the moment of purchase.

A stricter policy can improve the return margin and harm the purchase margin at the same time. A calculation that holds the price fixed will miss the second effect, and it can get the sign of the welfare change wrong. The seller is choosing the price and the return rule together. I need both choices in the model.

Which margin wins depends on how large the margin is, and on how much value is left in a returned good. If the good can be resold, a return is less wasteful, and the case for paying return shipping is stronger. If the margin is thin, a return that should not have happened is expensive, and the case for making the buyer bear that cost is stronger. I estimate these objects by category rather than imposing one answer for all apparel.

## 3. What the shopper and the seller do

Think through one purchase. The shopper sees the price and the return rule, and decides whether to buy. The match is still uncertain at that moment. If coverage is optional, the shopper also decides whether to buy return-shipping insurance. After the good arrives, the match is realized, and the shopper decides whether to keep it or send it back. The cost of that last decision depends on who paid for return shipping, and on whether there is a restocking fee.

The seller sees this coming. A more generous return rule raises the chance the good comes back, which lowers the effective margin. The seller may then raise the price. That price feeds back into who buys. So the return rate, the insurance decision, and the price are not three separate facts. They are one equilibrium.

I treat the seller as a monopolist for this pricing problem. That is the right object for one retailer setting its own price and its own return rule. It is not a model of competition on Taobao, and I will not talk about it as if it were.

## 4. Data

The records run from 2017 to 2023, six apparel categories, about 62 million RMB in revenue for this retailer. I link orders, prices, insurance, and returns. I also scrape product pages and use OCR on product images, so category and attributes are not just whatever the order file happens to contain.

The fact I use for identification, in the economic sense, is that this same seller switches between automatic coverage and optional coverage. I am not comparing a generous store with a strict store. The switch happens inside one retailer. Categories still differ in margins and in how much of a returned good can be salvaged, and I let the estimates differ across those categories. Dresses are the one I will separate in the results, because the ranking there does not look like the others.

Return rates of 20 to 30 percent are high enough that small changes in who pays for a return move profit and welfare. They are also high enough that ignoring returns, and treating every sale as final, is not a harmless simplification.

## 5. How to see the trade-off

If I have a board, I draw two losses, not one welfare number.

The first loss is at the purchase. Someone who should have bought does not, because the price is high or because a strict return rule makes the good too risky to try. That purchase would have created surplus, and it does not happen. I call this the purchase loss.

The second loss is after the purchase. Someone returns a good they should have kept, or the returned good cannot be resold, so the match that was created at purchase is thrown away. I call this the return loss.

A stricter rule shrinks the return loss and can enlarge the purchase loss, because the seller raises the price once returns fall. A more generous rule does the opposite. It shrinks the purchase loss and can enlarge the return loss. The welfare ranking is whichever loss falls by more. That is why I will not summarize the paper as "free returns are good" or "free returns are bad."

"Best feasible welfare" is the best outcome in this model, the benchmark I measure policies against. When I say optional coverage gains 15 to 30 percentage points of that benchmark in thinner-margin categories, I mean it closes that much of the gap to the best outcome, relative to automatic coverage. It is a comparison of rules, on one scale, not a claim that I have implemented the best outcome.

## 6. How the estimation is organized

By category, I recover demand, how uncertain the match is, and how returns respond when the cost of returning changes. The decisions in the estimation are purchase, insurance take-up, and return, with the seller's price responding to the rule. Estimation is by GMM. The policy ranking is checked with the bootstrap, so I am not hanging the conclusion on one point estimate.

The code runs from raw orders to those rankings on AWS and on the HPC cluster, in Python, R, and C++. The Monte Carlo and the optimization sit in C++. I mention that only because the ranking is something I can rerun, not a table that was assembled once.

If you want the moment conditions, I will put them on the board. The content of the exercise is the split I started with: which policies expand purchases that should happen, and which policies cut returns that should not.

## 7. Ranking

Take a high-margin category first, one where a returned good still has salvage value. Automatic coverage brings shoppers in. Some of them return. Because the good can be resold and the margin on a kept sale is large, those extra purchases are worth more than the extra returns cost. Paying return shipping for everyone is the better of the two rules the seller already uses.

Now take a thin-margin category. The same generous rule still brings shoppers in, but a return destroys most of the margin. Optional coverage gives that up at the purchase and gets it back on the returns. The net gain against automatic coverage is about 15 to 30 percentage points of the best feasible welfare, and about 50 percentage points in the thinnest category. The thinnest category is where I most want you to look, because that is where treating the sale as final would be most misleading.

So I do not have a single winning rule. Lenient where the good is valuable and can be resold. Stricter where the margin is thin and a return is mostly lost surplus.

## 8. A menu, and what I would not claim

Neither of the rules the seller actually uses is the best I find for most categories. The counterfactual menu pairs a discounted price with a restocking fee of about 10 to 15 percent. The discount holds on to purchases. The fee holds down returns that should not happen. Outside dresses, that menu reaches about 75 to 78 percent of the best feasible welfare, and it beats both automatic and optional coverage for most categories. Dresses are the exception. I report them separately rather than letting them disappear into an average.

What I would not claim: this is one retailer, in apparel, under monopoly pricing. The percentages are not a recipe for every platform. What I do take as general is the direction of the trade-off. The return rule changes the price the seller wants to charge. A welfare calculation that holds that price fixed can rank the rules the wrong way.

I can take questions on this, or go on to the two shorter papers: unsold books, then search.
