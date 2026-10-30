# 🛠️ Настройка рабочей среды

## Подготовка виртуальной машины с Ubuntu

Локальный запуск `Jupyter Notebook`:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Загрузка данных

* [titanic](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
* [titanic3](https://raw.githubusercontent.com/amueller/scipy-2017-sklearn/091d371/notebooks/datasets/titanic3.csv)
* ...

``` python
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1)
titanic = fetch_openml('titanic', version=1)
```
