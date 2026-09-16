# Базовый Python

> Лекция 1. Дисциплина «Применение технологий анализа данных и машинного
> обучения в цифровых сервисах».

> Вводный материал (Big Data, Machine Learning, инструменты, Jupyter) —
> см. [00-intro-bigdata-ml.md](00-intro-bigdata-ml.md).

## Цель занятия

Сформировать базовые навыки программирования на Python, необходимые для
последующей работы с данными: типы и структуры данных, управляющие
конструкции, функции, чтение файлов.

## 1. Экосистема анализа данных

Ключевые библиотеки, используемые в курсе:

| Библиотека | Назначение |
|------------|------------|
| `numpy` | многомерные массивы, линейная алгебра, численные методы |
| `pandas` | табличные данные, `DataFrame`, обработка и агрегация |
| `scipy` | научные вычисления, статистика |
| `matplotlib` / `seaborn` | визуализация |
| `scikit-learn` | алгоритмы машинного обучения |
| `keras` (TensorFlow) | нейронные сети |
| `jupyter` | интерактивная среда разработки |

## 2. Базовые типы данных

```python
x = 42                # int
y = 3.14              # float
name = "data"         # str
flag = True           # bool
none = None           # NoneType
```

## 3. Структуры данных

### Список (`list`) — изменяемая упорядоченная коллекция

```python
values = [1, 2, 3, 4]
values.append(5)          # [1, 2, 3, 4, 5]
values[0]                 # 1
values[-1]                # 5 (последний)
values[1:3]               # [2, 3] (срез)
```

### Кортеж (`tuple`) — неизменяемая коллекция

```python
point = (10, 20)
x, y = point          # распаковка
```

### Словарь (`dict`) — пары «ключ → значение»

```python
person = {"name": "Иван", "age": 30}
person["age"]           # 30
person.get("city", "—") # значение по умолчанию
```

### Множество (`set`) — уникальные неупорядоченные элементы

```python
ids = {1, 2, 2, 3}      # {1, 2, 3}
ids.add(4)
```

## 4. Управляющие конструкции

### Условный оператор

```python
if x > 0:
    sign = "положительное"
elif x < 0:
    sign = "отрицательное"
else:
    sign = "ноль"
```

### Циклы

```python
# for по элементам
for v in values:
    print(v)

# for по индексам
for i in range(len(values)):
    print(i, values[i])

# while
n = 0
while n < 10:
    n += 1
```

### Генераторы списков (list comprehensions)

```python
squares = [x ** 2 for x in range(10)]              # квадраты 0..9
evens   = [x for x in range(20) if x % 2 == 0]     # с условием
```

## 5. Функции

```python
def mean(values):
    """Среднее арифметическое."""
    return sum(values) / len(values)

def describe(values):
    n = len(values)
    m = mean(values)
    return n, m          # возврат нескольких значений (кортеж)

# лямбда-функции
square = lambda x: x ** 2
```

## 6. Работа с файлами

```python
# построчное чтение
with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()

# запись
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
```

## 7. Обработка исключений

```python
try:
    result = 10 / divisor
except ZeroDivisionError:
    result = None
finally:
    print("готово")
```

## 8. Стандартные приёмы при работе с данными

- `sum`, `min`, `max`, `len`, `sorted`, `set`
- `zip` — параллельный обход нескольких последовательностей
- `enumerate` — обход с индексами
- `dict(zip(keys, values))` — построение словаря из двух списков

```python
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))   # {'a': 1, 'b': 2, 'c': 3}
```

## Резюме

- Python — основной инструмент курса; данные представляются структурами
  `list`/`dict`/`set`, обрабатываются циклами, comprehension и функциями.
- Файлы читаются через контекстный менеджер `with`.
- Следующий раздел — табличные данные в `pandas`.
