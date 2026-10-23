# Исследование данных

> Лекция 4. Exploratory Data Analysis.

## Цель занятия

Научиться «понимать» данные до построения моделей: оценивать структуру,
качество и распределения, находить закономерности и аномалии визуально.

## 1. Обзор данных

```python
df.head()         # первые строки
df.info()         # типы, объём, пропуски
df.describe()     # статистики числовых колонок
df.describe(include="object")   # для категориальных
df.shape          # размер
```

## 2. Базовая проверка данных

- **формат** — соответствие типов ожидаемым (числа как числа, даты как даты);
- **физичность** — значения в допустимых границах (возраст $\ge 0$, цена $> 0$);
- **логичность** — согласованность между колонками (дата заказа после даты
  доставки).

```python
df["age"].describe()            # поиск нефизичных минимумов/максимумов
(df["age"] < 0).sum()           # счётчик отрицательных возрастов
df[df["age"] < 0]               # просмотр подозрительных строк
```

## 3. Сводные таблицы

```python
# среднее значение по группам
df.pivot_table(values="fare", index="pclass", columns="sex", aggfunc="mean")

# простое агрегирование
df.groupby("pclass")["fare"].agg(["count", "mean", "median"])
```

## 4. Гистограммы и распределения

Гистограмма показывает **частоту** попадания значений в интервалы (бины).

```python
df["age"].hist(bins=30)
df["age"].plot(kind="kde")       # оценка плотности
```

## 5. Диаграмма размаха (boxplot) и квантили

Квантиль $q_p$ — значение, ниже которого лежит доля $p$ наблюдений.

- медиана = $q_{0.5}$;
- первый квартиль $Q_1 = q_{0.25}$, третий $Q_3 = q_{0.75}$;
- межквартильный размах IQR $= Q_3 - Q_1$;
- «усы» boxplot — в пределах $1.5 \cdot \text{IQR}$; дальше — выбросы.

```python
df["age"].quantile([0.25, 0.5, 0.75])
sns.boxplot(x="pclass", y="fare", data=df)   # ящики по группам
```

## 6. Построение графиков (seaborn, matplotlib)

| Тип | Функция | Назначение |
|-----|---------|------------|
| гистограмма | `sns.histplot` / `df.hist` | распределение одной переменной |
| ящик с усами | `sns.boxplot` | распределение + выбросы |
| рассеяние | `sns.scatterplot` | связь двух числовых |
| счётчики | `sns.countplot` | частоты категорий |
| пары | `sns.pairplot` | матрица графиков |
| линия | `sns.lineplot` | динамика/тренд |

```python
sns.scatterplot(data=df, x="age", y="fare", hue="survived")
sns.pairplot(df[["age", "fare", "pclass"]], hue="survived")
```

## 7. Тепловые карты

Визуализация корреляционной матрицы (раздел 5 даёт теорию корреляции).

```python
corr = df.select_dtypes("number").corr()   # корреляция числовых колонок
sns.heatmap(corr, annot=True, cmap="coolwarm")
```

Тёплые цвета — положительная связь, холодные — отрицательная.

## Резюме

- EDA: сначала `info`/`describe`, затем проверка качества значений.
- Сводные таблицы `pivot_table` выявляют зависимости между группами.
- Гистограммы и boxplot показывают распределение и выбросы; `scatterplot` —
  связь переменных; `heatmap` — корреляции.

```{code} python
:linenos:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch


# ---------- 1. Загрузка данных ----------
df = pd.read_csv("~/mldata/titanic.csv")

# ---------- 2. Текстовая сводка ----------
def missing_report(df: pd.DataFrame) -> pd.DataFrame:
    """Возвращает таблицу: тип, число непустых, число пропусков, доля, уникальных."""
    rep = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "non_null": df.notnull().sum(),
        "missing": df.isnull().sum(),
        "percent": (df.isnull().mean() * 100).round(2),
        "unique": df.nunique()
    })
    return rep.sort_values("percent", ascending=False)


report = missing_report(df)
print(report)
print("\nВсего строк:", len(df))
print("Столбцов с пропусками:", (report["missing"] > 0).sum())


# ---------- 3. Визуализация ----------
miss_mask = df.isnull()                     # булев DataFrame: True = пропуск
cols_with_na = miss_mask.columns[miss_mask.any()].tolist()
missing_counts = miss_mask.sum().sort_values(ascending=False)
missing_pct = (miss_mask.mean() * 100).sort_values(ascending=False)

# Оставим для bar-панелей только столбцы, где пропуски реально есть
counts_plot = missing_counts[missing_counts > 0]
pct_plot = missing_pct[missing_pct > 0]

fig = plt.figure(figsize=(16, 8))
gs = fig.add_gridspec(2, 2, width_ratios=[3, 2], height_ratios=[1, 1])

# --- Панель 1: карта пропусков (столбцы x строки) ---
ax1 = fig.add_subplot(gs[:, 0])
cmap = ListedColormap(["#2e7d32", "#c62828"])   # зелёный = есть данные, красный = пропуск
ax1.imshow(
    miss_mask.to_numpy(),
    aspect="auto",
    cmap=cmap,
    interpolation="nearest",
    vmin=0, vmax=1
)
ax1.set_xticks(range(df.shape[1]))
ax1.set_xticklabels(df.columns, rotation=90)
ax1.set_yticks([])
ax1.set_title("Карта пропусков: строки × столбцы")
ax1.legend(
    handles=[Patch(color="#2e7d32", label="есть значение"),
             Patch(color="#c62828", label="пропуск")],
    loc="upper right", bbox_to_anchor=(1.0, 1.0), frameon=True
)

# --- Панель 2: доля пропусков по столбцам ---
ax2 = fig.add_subplot(gs[0, 1])
bars = ax2.barh(pct_plot.index[::-1], pct_plot.values[::-1], color="#c62828")
ax2.set_xlabel("Доля пропусков, %")
ax2.set_title("Доля пропусков по столбцам")
ax2.set_xlim(0, 100)
for bar, v in zip(bars, pct_plot.values[::-1]):
    ax2.text(v + 1, bar.get_y() + bar.get_height() / 2,
             f"{v:.1f}%", va="center", fontsize=9)

# --- Панель 3: абсолютное число пропусков ---
ax3 = fig.add_subplot(gs[1, 1])
bars = ax3.barh(counts_plot.index[::-1], counts_plot.values[::-1], color="#5c6bc0")
ax3.set_xlabel("Число пропусков, шт.")
ax3.set_title("Абсолютное число пропусков")
for bar, v in zip(bars, counts_plot.values[::-1]):
    ax3.text(v + 3, bar.get_y() + bar.get_height() / 2,
             f"{int(v)}", va="center", fontsize=9)

plt.tight_layout()
plt.show()
```
