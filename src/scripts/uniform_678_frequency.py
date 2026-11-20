import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed=0)

# Общее число испытаний
N_total = 100_000

# Одно большое наблюдение: случайные целые от 0 до 9 включительно
samples = rng.integers(0, 10, size=N_total)

# Индикатор "попадания" в множество {6, 7, 8}
hit = np.isin(samples, [6, 7, 8]).astype(int)

# Накопленная доля попаданий после каждого наблюдения
cum_hits = np.cumsum(hit)
n = np.arange(1, N_total + 1)
freq = cum_hits / n

# Контрольные точки для печати
checkpoints = [10, 100, 1_000, 10_000, 100_000]
for k in checkpoints:
    print(f"n = {k:>7}: доля {{6,7,8}} = {freq[k-1]:.4f}")

fig, ax = plt.subplots(figsize=(9, 5))

ax.plot(n, freq, color="C0", linewidth=1.2, label="накопленная доля {6,7,8}")
ax.axhline(0.3, color="C1", linestyle="--", linewidth=1.5, label="теоретическое 0,3")

# Отметим контрольные точки
for k in checkpoints:
    ax.plot(k, freq[k-1], "o", color="C0", markersize=5)
    ax.annotate(f"{freq[k-1]:.3f}", (k, freq[k-1]),
                textcoords="offset points", xytext=(6, 8), fontsize=8)

ax.set_xscale("log")
ax.set_xlim(1, N_total)
ax.set_ylim(0.15, 0.45)
ax.set_xlabel("число наблюдений")
ax.set_ylabel("доля наблюдений, где выпало 6, 7 или 8")
ax.set_title("Сходимость частоты к вероятности 0,3")
ax.grid(True, which="both", alpha=0.3)
ax.legend(loc="upper right")

plt.tight_layout()

from pathlib import Path
picture_name = Path(__file__).name + '.png'
fig.savefig(picture_name, dpi=300, bbox_inches='tight')
