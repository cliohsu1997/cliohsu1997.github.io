# Verbal script — Herding
**City University of Macau · ~20 minutes · English (colloquial)**

Notation up front: **\(G/B\)** = true state (Good/Bad), **\(g/b\)** = private signal (good clue / bad clue), **Line up / Drop** = action.

---

## 1 · Title (~45 sec)

“Hi, I’m Ke Cheng Hsu from HKUST. Today we’ll talk about herding under imperfect information. Plan: start with a Macau queue you all know, a couple more everyday examples, then what herding is, Bayes with a restaurant, and finally Person 1, 2, 3 to see why following the crowd can be rational — and still go wrong.”

---

## 2 · Margaret’s (~2 min)

“Margaret’s Café e Nata, the egg tart place near Sintra Square — there’s always a long winding queue. Many people say the tarts are actually too sweet or oily compared to Lord Stow’s, and the line is mostly guidebook fame.

My own version: after I tried it, I felt so-so; my friend felt the same. I like egg tarts, but not enough to stand there for twenty minutes. I only lined up because I saw so many people lining up, so I thought it must be amazing.”

---

## 3 · Other examples (~2 min)

“Same thing elsewhere. SBF and FTX — people piled in because others seemed to get rich; once trust broke, everyone ran for the exit. The recent NVDA crush — the stock rose on AI enthusiasm; when sentiment flipped, everyone sold together. Labubu toys — people want them because they’re everywhere online; popularity itself looks like a quality signal.

And homework copying: the best econ student finishes first; the second-best checks answers with the best; the third person — even if their own answer was originally correct — may still switch to match the first two. That’s exactly the cascade we’ll build.”

---

## 4 · What is herding (~1.5 min)

“You have your own private clue, but you also see what others chose — and sometimes you follow the crowd even when your clue says the opposite. Why? Other people’s choices carry information. When signals are imprecise, early information can be wrong, so the early action can be wrong — and later people infer that wrong information from those actions.”

---

## 5 · Setup (~1.5 min)

“One restaurant: state is Good or Bad, prior one half each. People arrive one by one. Each gets a private signal, \(g\) or \(b\), that’s 70% accurate — \(\Pr(g\mid G)=0.7\), \(\Pr(b\mid B)=0.7\).

Signals are *conditionally independent given the state* — meaning once you know the restaurant is Good or Bad, what signal person A draws tells you nothing extra about person B’s signal; they only move together through the common state.

Actions: Line up or Drop. Break-even: Line up if the posterior on \(G\) is above one half, Drop if below; exactly one half, coin flip. Goal: Person 1–3, and watch Person 3 discard his own signal.”

---

## 6 · Person 1 (~2 min)

“The picture: area equals probability. Left half is \(G\), right half \(B\); the \(g\) regions cover 70% of the Good side and 30% of the Bad side.

Person 1 only has his own signal \(g\). Bayes: \(\Pr(G\mid g)\) is the Good slice over the whole \(g\) area — \(0.35 / (0.35+0.15) = 0.7\). Above one half, so he Lines up. Everyone else only sees his *action*, not his signal.”

---

## 7 · Person 2 (~2 min)

“Person 2 sees Person 1 Line up — that reveals \(s_1=g\). Two cases.

Case \(s_2=g\): two good clues, posterior above one half, Line up.

Case \(s_2=b\): one good clue and one bad clue of the same strength. Write Bayes: joint under \(G\) is \(0.7\cdot0.3=0.21\), joint under \(B\) is \(0.3\cdot0.7=0.21\) — by conditional independence. Equal, so the posterior is exactly one half. He’s indifferent — Line up or Drop with probability one half each.”

---

## 8 · Person 3 — write the posterior (~2 min)

“Now the story: two people are lining up in front of me, and I draw a bad signal \(b\). Should I wait in line or leave? That depends on \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\).

Write Bayes with the *actions and my signal*: numerator \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\), denominator that plus the same under \(B\).

Important: do **not** replace Line up by \(g\). Line up is an action; \(g\) is a signal — especially since Person 2 sometimes Lines up even with \(b\). Next we need the conditional probabilities \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) and \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\).”

---

## 9 · Person 3 — conditional probabilities (~2.5 min)

“Why can we split the product? The earlier Line-ups depend only on \(s_1\) and \(s_2\). Given the state, those signals are independent of Person 3’s \(b\), so \(b\) is conditionally independent of the two Line-ups: probability of (LU, LU, \(b\)) equals probability of (LU, LU) times probability of \(b\).

Now walk through Person 1 and 2 under each state.

Under \(G\): Person 1 Lines up only if \(s_1=g\), probability 0.7. Given that, Person 2 Lines up for sure if \(s_2=g\) (0.7), or with probability one half if \(s_2=b\) (0.3). So \(0.7\,(0.7+0.3\cdot\tfrac12)=0.595\), times \(\Pr(b\mid G)=0.3\) gives \(0.1785\).

Under \(B\): same logic with the flipped likelihoods — Person 1 Lines up only if \(s_1=g\) (0.3); Person 2 Lines up for sure if \(s_2=g\) (0.3), or half the time if \(s_2=b\) (0.7). That’s \(0.195\), times \(\Pr(b\mid B)=0.7\) gives \(0.1365\).”

---

## 10 · Person 3 — combine (~2 min)

“Equal priors, so plug in: \(0.1785\cdot\tfrac12\) over \(0.1785\cdot\tfrac12 + 0.1365\cdot\tfrac12\), about 0.57 — above one half.

So Person 3 still Lines up — he discards his own bad signal. That’s the start of the cascade: two public Line-ups outweigh his private clue.”

---

## 11 · Takeaways (~2 min)

“If everyone only used their own signal and we aggregated, private information would keep entering the public record. But in a cascade, choices are sequential: early actions become public clues, so later people can rationally ignore their own signals.

Same logic as Margaret’s queues, SBF/FTX, NVDA, Labubu — and homework copying. Questions?”
