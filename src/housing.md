---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  name: python3
  display_name: Python 3
---

# Цены на жилье в Калифорнии

## Ставим задачу

Набор данных "California Housing" содержит часть данных переписи населения США за 1990 года по Калифорнии.

|  Признак   |   Расшифровка    | Что означает |
|------------|------------------|--------------|
|   MedInc   | Median Income    | Медианный доход домохозяйств в блок-группе (в десятках тысяч долларов) |
|  HouseAge  | House Age        | Медианный возраст домов в блок-группе (в годах) |
|  AveRooms  | Average Rooms    | Среднее количество комнат на одно домохозяйство |
|  AveBedrms | Average Bedrooms | Среднее количество спален на одно домохозяйство |
| Population | Population       | Общая численность населения блок-группы |
|  AveOccup  | Average Occupancy| Среднее число членов домохозяйства (средняя заполняемость) |
|  Latitude  | Latitude         | Широта блок-группы (географическая координата) |
| Longitude  | Longitude        | Долгота блок-группы (географическая координата) |


## Загружаем данные

```{code-cell} python
from sklearn.datasets import fetch_california_housing
X_housing, y_housing = fetch_california_housing(return_X_y=True, as_frame=True)
```

```{code-cell} python
X_housing.head()
```

```{code-cell} python
X_housing.info()
```


## Исследуем данные

```{code-cell} python
X_housing.describe()
```

```{code-cell} python
import matplotlib.pyplot as plt
X_housing.hist(bins=50, layout=(4,2), figsize=(10,20))
plt.tight_layout()
```


## Разделяем данные

## Обучаем модель

## Получаем прогнозы

## Оцениваем качество

## Выводы

## Вопросы для самоконтроля
