import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

out = Path(__file__).resolve().parent

names = [
    "Seng Cheong\n(water crab congee)",
    "Margaret's\n(egg tarts)",
    "A Lorcha\n(Portuguese)",
]
openrice = [3.0, 3.5, 3.5]
wait_min = [25, 20, 30]

x = np.arange(len(names))
width = 0.36

fig, ax1 = plt.subplots(figsize=(10, 5.2), dpi=160)
ax2 = ax1.twinx()

ax1.bar(x - width / 2, openrice, width, color="#4C78A8", label="OpenRice score (/5)")
ax2.bar(x + width / 2, wait_min, width, color="#F58518", label="Typical wait (minutes)")

ax1.set_ylim(0, 5)
ax2.set_ylim(0, 45)
ax1.set_ylabel("OpenRice overall score (/5)", fontsize=11)
ax2.set_ylabel("Typical reported wait (minutes)", fontsize=11)
ax1.set_xticks(x)
ax1.set_xticklabels(names, fontsize=10)
ax1.axhline(4.0, color="#54A24B", ls="--", lw=1.2, alpha=0.85)
ax1.text(2.05, 4.08, "Strong score ~ 4+", fontsize=9, color="#54A24B")

ax1.set_title(
    "Macau: people still queue even when review scores are only middling",
    fontsize=13,
    pad=10,
)

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc="upper left", frameon=False)

ax1.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)

note = (
    "Illustrative teaching figure from public OpenRice overall ratings "
    "(Seng Cheong 3.0; Margaret's 3.5; A Lorcha 3.5) and commonly reported queues."
)
fig.text(0.02, 0.01, note, fontsize=7.5, color="#444444")

fig.tight_layout(rect=[0, 0.06, 1, 1])
path = out / "macau_restaurant_queue_vs_score.png"
fig.savefig(path, bbox_inches="tight", facecolor="white")
print(path)
