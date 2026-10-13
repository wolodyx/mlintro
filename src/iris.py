# Загружаем данные.
from sklearn.datasets import load_iris
iris_dataset = load_iris()

# Исследуем объект `iris_dataset`.
print(iris_dataset.keys())
iris_dataset['target_names'] # Обращение к ключу через оператор индексации
iris_dataset.feature_names   # Обращение к ключу через атрибут.

# Выводим набор данных средствами Pandas.
import pandas as pd
df = pd.DataFrame(iris_dataset.data, columns=iris_dataset.feature_names)
df['target'] = iris_dataset.target
print(df)

