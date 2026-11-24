# Verbal script — Herding  
**City University of Macau · ~20 minutes**

**Notation (say this clearly):**  
- **\(G\) / \(B\)** = actual state (Good / Bad)  
- **\(g\) / \(b\)** = private signal (good clue / bad clue)  
- **Line up / Drop** = action  

---

## Title (~45–60 sec) · ROADMAP SPOKEN ONLY

“I’m Ke Cheng Hsu. Today: herding under imperfect information.

What we’ll cover—not on the slides as a list: everyday examples; what herding means; Bayes with a restaurant example; then Person 1, Person 2, Person 3.

Goal: see why following the crowd can be rational—and still go wrong.”

---

## Slide 1 — Margaret’s (~2 min)

“Margaret’s Café e Nata near Sintra Square: winding queue; many say overly sweet or oily vs Lord Stow’s; line often from guidebook fame.

Personal version: after I had it, I felt so-so; my friend also felt so-so. I like egg tarts, but not enough for twenty minutes. I lined up only because I saw many people lining up, so I thought it must be super good.”

---

## Slide 2 — Other examples (~2 min)

“SBF/FTX; NVDA crush—*spoken only:* Jensen Huang scandal talk as crowd-flipping news; Labubu.

Homework: best econ student finishes first; second-best checks against the best; third may discard their own correct answer and copy the first two—same cascade logic as Person 3.”

---

## Slide 3 — What is herding (~1.5–2 min)

“Private clue plus others’ actions; sometimes follow the crowd against your own clue.

When signals are imprecise, early information can be wrong—so the early action can be wrong. Later people infer previous players’ information from those actions, and can pick up the wrong information.”

---

## Slide 4 — Prior vs posterior (~1.5–2 min)

“Rectangle split into \(G\) and \(B\)—prior one half each. Circle is signal \(g\), labeled on top, sitting more toward \(G\). Inside the circle: \(G\cap g\) on the Good side and \(B\cap g\) on the Bad side. Posterior \(\Pr(G\mid g)\) is the Good slice of the signal circle.”

---

## Slide 5 — Notation (~1.5 min)

“State \(G\)/\(B\) with equal prior one half. Signals \(g\)/\(b\) are 70% accurate and *conditionally independent given the state*—briefly: given Good or Bad, what signal A draws does not change what signal B draws; they only co-move through the common state. Action: Line up or Drop. Goal later: show Person 3 discards his own signal.”

---

## Slide 6 — Venn (~1.5 min)

“Then the picture: \(G\cap g\) and \(B\cap g\) inside signal circle \(g\).”

---

## Slide 7–8 — Bayes (~4 min)

“Write the final formula directly:
\(\Pr(G\mid g)=\Pr(g\mid G)\Pr(G)/[\Pr(g\mid G)\Pr(G)+\Pr(g\mid B)\Pr(B)]\).

Next page: plug in numbers → 0.7. Same idea for signal \(b\) → 0.3.”

---

## Slide 8 — Setup + break-even (~1.5 min)

“Break-even: Line up if posterior on \(G\) is above one half; Drop if below; if exactly one half, coin flip.

Important for later: each person’s decision is based on (i) their own signal and (ii) the actions taken previously—because previous actions are noisy public clues about previous signals.”

---

## Slide 9 — Person 1 (~2 min)

“Only signal \(g\) → \(\Pr(G\mid g)=0.7\) → **Line up**. Others see the action, not the raw signal.”

---

## Slide 10 — Person 2 (~2.5 min)

“Sees Line up ⇒ \(s_1=g\). Two cases for own signal.

Case \(s_2=g\): Line up. Case \(s_2=b\): one joint \(\Pr(s_1=g,s_2=b\mid G)=0.21\) (same under \(B\) by conditional independence); Bayes → one half, indifferent coin flip.

*[Next slide assumes the history we need for Person 3: two Line-ups. Speak that only when you turn the page.]*”

---

## Slide 11 — Person 3: write Bayes with actions (~2 min)

“Story: two consumers are lining up in front of me; I draw a bad signal \(b\). Should I wait in line or leave? That depends on \(\Pr(G\mid \mathrm{LU},\mathrm{LU},b)\).

Write Bayes: numerator \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\Pr(G)\); denominator that plus the same under \(B\).

Do **not** replace Line up by signal \(g\). Line up is an action; \(g\) is a signal. Next we need the conditional probabilities \(\Pr(\mathrm{LU},\mathrm{LU},b\mid G)\) and \(\Pr(\mathrm{LU},\mathrm{LU},b\mid B)\).”

---

## Slide 12 — Conditional probabilities under \(G\) and under \(B\) (~2.5–3 min)

“Slide stays short: product split + two plugged numbers. Say the rest out loud. Call them conditional probabilities, not likelihoods.

Why the product? Earlier Line-ups depend only on \(s_1,s_2\). Given the state, those signals are independent of Person 3’s \(b\), so \(b\) is conditionally independent of \((\mathrm{LU},\mathrm{LU})\).

When state is \(G\): Person 1 Lines up only if \(s_1=g\) (prob \(0.7\)). Then Person 2 Lines up for sure if \(s_2=g\) (prob \(0.7\)), or with probability one half if \(s_2=b\) (prob \(0.3\)). That gives \(0.7(0.7+0.3\cdot\tfrac12)=0.595\), times \(\Pr(b\mid G)=0.3\) → \(0.1785\).

When state is \(B\): same logic with flipped signal probs — Person 1 LU only if \(s_1=g\) (prob \(0.3\)); Person 2 LU for sure if \(s_2=g\) (prob \(0.3\)), or half the time if \(s_2=b\) (prob \(0.7\)) → \(0.195\cdot 0.7=0.1365\).”

---

## Slide 13 — Combine (~2 min)

“Equal priors: posterior \(= 0.1785 / (0.1785+0.1365) \approx 0.57 > 1/2\).

Still **Line up**—Person 3 *discards* his own signal \(b\). That is the cascade: two public Line-ups outweigh his private bad clue.”

---

## Slide 14 — Takeaways (~2 min)

“If everyone decided only on their own signal and we aggregated those independent choices, private information would keep showing up.

In a cascade, information is sequential: you condition on previous actions and your own signal; early Line-ups can make Person 3 rationally ignore \(b\).

Same logic: Margaret’s, SBF/FTX, NVDA, Labubu.

Questions?”
