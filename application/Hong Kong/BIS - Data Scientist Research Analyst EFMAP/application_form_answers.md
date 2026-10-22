# BIS application form answers (JR100491)

Copy-paste ready. Polish date: 22 Oct 2026.

---

## 1. Technologies and programming languages

*(If yes, could you please detail what kind of technologies and programming languages you have worked with?)*

I primarily use R to build up libraries for structural estimation, simulation, and counterfactual analysis, as well as econometric estimation and figures. I use Python for data collection — web scraping, APIs, and AI-based OCR that converts product images into analyzable text — and for data cleaning. I use Stata for applied econometrics, and C++ for performance-critical computation such as Monte Carlo simulation, iterative equilibrium solving, and optimization. I have also built a MATLAB model of a bank crisis on an interbank lending network, framing crisis intervention as a regulator–creditor negotiation.

---

## 2. Recent BIS publication

*(Identify a recent publication by the BIS that you found insightful. What about it captured your interest? How does it relate to your professional expertise or interests?)*

I found BIS Working Paper No. 1382, “Are stablecoins and bank deposits substitutes?” by Rashad Ahmed and Iñaki Aldasoro, especially insightful because it estimates how strongly stablecoin holdings respond to deposit-rate changes — the degree of substitution between stablecoins and bank deposits. What struck me most is their instrument: it is beautiful. Banks pass federal funds rate changes into deposit rates much more aggressively when rates are already above roughly 3% than when they are below, and the authors use that asymmetric passthrough to isolate deposit-rate moves and address reverse causality. The finding that USDC responds more than USDT, consistent with U.S. institutions being better able to switch between deposits and stablecoins, is also compelling. Reading it from Hong Kong, I wondered whether a similar substitution would show up for USDT if one could isolate balances tied to Hong Kong, where the linked exchange rate means local deposit rates often move with U.S. rates. At the same time, I would want to probe the exclusion restriction carefully: Fed policy can affect stablecoin demand not only through deposit rates, but also by making bonds more attractive relative to zero-yield cash-like assets, and by moving equity markets, which can change investors’ appetite for holding stablecoins versus risky assets. With my background in structural estimation on large datasets, I would be eager to help push this agenda — for example by tightening identification around these alternative channels and, where data allow, quantifying substitution more explicitly in a structural portfolio framework, including Asia-focused cuts such as Hong Kong.

---

## 3. Producing graphs for that publication

*(If asked to produce the graphs for the BIS publication that you identified, how would you approach this task? Please describe how you would apply your skillset to this task.)*

I would start with the paper’s key identification graph: the deposit rate against the federal funds rate, with separate fitted lines below and above about 3.125%, placed next to the same scatter for Treasury bill rates that stay roughly linear.

On data access, I would be explicit about what FRED can and cannot provide. From FRED I can pull the federal funds target midpoint and the 3-month Treasury bill rate (and other controls such as the 10-year yield if needed). FRED does **not** provide the paper’s exact non-maturity deposit-rate series. That series is constructed from RateWatch national bank offer rates on savings and money market deposit accounts (MMDAs) by balance tier, which the authors average into one deposit-rate index (accessed via Haver in the paper). So I would get Fed funds and T-bills from FRED, and build or obtain the deposit rate from those RateWatch tiers — or from the authors’ replication materials if RateWatch/Haver access is limited — rather than treating deposit rates as a single ready-made FRED download.

In R (and Python where helpful for data pulls), I would clean dates, align weekly frequencies, and check for breaks or missing weeks. Then I would draw a scatter of the deposit rate on the federal funds rate, split the sample at their 3.125% cutoff, and overlay two OLS fits for the low-rate and high-rate regimes, with the kink marked clearly; I would put the T-bill scatter beside it so the contrast — a kink for deposits, no kink for bills — is immediate. I would also report the two slopes and a simple test that they differ, so the figure quantifies the asymmetric passthrough that motivates their instrument.

A central issue is how the kink is chosen. The paper imposes 3.125% from the FOMC target range rather than estimating it. After reproducing their split, I would treat the kink location as something to verify: run a structural-break or threshold search on the deposit-rate–on–federal-funds relationship, report the estimated break, and redraw the piecewise fits at that data-driven kink to check whether the asymmetry still lines up with the policy-based cutoff. Finally I would produce a publication-ready figure (clear axes, legend, sample note) and a reproducible script so the graph can be refreshed when the data update. That matches how I already work: clean and merge time-series data carefully, estimate simple regressions transparently, and turn the result into a figure that carries the economic point.

---

## Optional: notice period

*(What is your notice period?)*

No formal notice period. I am completing my Ph.D. and can start from June 2027, or earlier by arrangement.
