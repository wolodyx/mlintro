# Раздел 2. Применение библиотеки Pandas для анализа данных

> Лекция 2. Работа с табличными данными.

## Цель занятия

Освоить базовые операции `pandas`: загрузка данных, выборка и фильтрация,
агрегация, объединение таблиц, преобразование колонок, работа с датами и
перестройка таблиц (pivot/melt).

## 1. Основные объекты: Series и DataFrame

```python
import pandas as pd

# Series — одномерный массив с индексами
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# DataFrame — двумерная таблица
df = pd.DataFrame({
    "name": ["Иван", "Анна", "Пётр"],
    "age":  [30, 25, 40],
})
```

## 2. Чтение и запись данных

```python
df = pd.read_csv("data.csv")                 # CSV
df = pd.read_csv("data.csv", sep=";", encoding="utf-8-sig")
df = pd.read_excel("data.xlsx", sheet_name="Лист1")

df.to_csv("out.csv", index=False)
```

Полезные параметры: `index_col`, `parse_dates`, `usecols`, `nrows`,
`na_values`.

## 3. Обзор данных

```python
df.head()        # первые строки
df.info()        # типы и количество непустых значений
df.describe()    # описательные статистики числовых колонок
df.shape         # (строки, столбцы)
df.columns       # список колонок
df.dtypes        # типы колонок
```

## 4. Выборка и фильтрация

```python
# по метке индекса (loc) и по позиции (iloc)
df.loc[0, "age"]          # элемент
df.loc[:, "name"]         # колонка
df.iloc[0, 1]             # первая строка, вторая колонка
df.iloc[:5]               # первые 5 строк

# фильтрация (boolean indexing)
adults = df[df["age"] >= 18]
mask = (df["age"] >= 18) & (df["name"] != "Пётр")
df[mask]

# query
df.query("age >= 18")
```

## 5. Агрегация: groupby

```python
# группировка + агрегирование
df.groupby("city")["salary"].mean()
df.groupby("city").agg(
    count=("salary", "count"),
    mean=("salary", "mean"),
    max=("salary", "max"),
)
```

## 6. Объединение таблиц

```python
# merge — по ключу (аналог JOIN в SQL)
pd.merge(left, right, on="id")
pd.merge(left, right, left_on="id", right_on="user_id", how="left")

# join — по индексу
left.join(right)

# concat — склейка по строкам/столбцам
pd.concat([a, b], axis=0)   # строки
pd.concat([a, b], axis=1)   # столбцы
```

## 7. Преобразование значений

```python
# apply — функция к колонке/строкам
df["age_group"] = df["age"].apply(lambda x: "взрослый" if x >= 18 else "ребёнок")

# map — замена по словарю
df["sex"] = df["sex"].map({"m": "муж", "f": "жен"})

# категоризация по числовым диапазонам
df["age_bin"] = pd.cut(df["age"], bins=[0, 18, 35, 60, 100],
                       labels=["<18", "18-35", "35-60", "60+"])
df["quartile"] = pd.qcut(df["age"], q=4)
```

## 8. Работа с датой и временем

```python
df["date"] = pd.to_datetime(df["date"])   # приведение к datetime

df["year"]  = df["date"].dt.year
df["month"] = df["date"].dt.month
df["dow"]   = df["date"].dt.dayofweek     # день недели (0 = пн)
df["diff"]  = (df["date"] - df["date"].shift(1)).dt.days

# переиндексация по времени + ресемплинг
df.set_index("date").resample("M").sum()
```

## 9. Перестройка таблиц

```python
# pivot_table — сводная таблица
pd.pivot_table(df, values="sales", index="region", columns="year", aggfunc="sum")

# melt — из широкого формата в длинный
pd.melt(df, id_vars=["id"], var_name="month", value_name="value")

# pivot — из длинного в широкий
df.pivot(index="id", columns="month", values="value")
```

## Резюме

- `pandas` — стандарт для табличных данных; загрузка через `read_csv`.
- Основные операции: `loc`/`iloc`, фильтрация, `groupby`+`agg`, `merge`.
- Преобразования: `apply`, `map`, `pd.cut`; даты — `pd.to_datetime` + `.dt`.
- Перестройка: `pivot_table`, `pivot`, `melt`.
