---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  name: python3
  display_name: Python 3
---

# Распознавание рукописных цифр

> Задача взята из книги О.Жерон "Прикладное машинное обучение с помощью Scikit-Learn и Tensorflow: концепции, инструменты и техники для создания интеллектуальных систем."


## Загружаем данные

``` {code-cell} python
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist.data, mnist.target
```


## Исследуем данные

``` {code-cell} python
import matplotlib.pyplot as plt
some_digit_index = 365
some_digit = X[some_digit_index]
some_digit_image = some_digit.reshape(28, 28)
plt.imshow(some_digit_image, cmap = 'gray_r')
```

``` {code-cell} python
import numpy as np
import matplotlib.pyplot as plt

rows, cols = 10, 10
fig, axes = plt.subplots(rows, cols)

for digit in range(rows):
    idx_digit = np.where(y == chr(48+digit))[0][:cols]
    for c in range(cols):
        ax = axes[digit, c]
        if c < len(idx_digit):
            ax.imshow(X[idx_digit[c]].reshape(28, 28), cmap='gray_r')
        ax.axis('off')

plt.tight_layout()
plt.show()
```


## Готовим обучающий набор

``` {code-cell} python
X_train, X_test, y_train, y_test = X[:60_000], X[60_000:], y[:60_000], y[60_000:]
```

``` {code-cell} python
shuffle_index = np.random.permutation(60_000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
```


## Обучаем двоичный классификатор


## Вопросы для контроля

1. Сбалансированы ли классы цифр? Провертье.
