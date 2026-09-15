# Применение технологий анализа данных и машинного обучения в цифровых сервисах

## Структура репозитория

```
aiuse/
├── README.md              # карта курса и соответствие разделам РПД
├── requirements.txt       # зависимости
├── .gitignore
├── lectures/              # конспекты лекций (Markdown)
│   └── 01-*.md … 16-*.md
├── labs/                  # лабораторные работы (Jupyter Notebook)
│   └── 01-*.ipynb … 16-*.ipynb
└── datasets/
    └── download.py        # загрузка внешних датасетов (в datasets/data/)
```

## Как пользоваться

1. Создать окружение и установить зависимости:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python -m ipykernel install --user --name=aiuse
   ```

2. Скачать внешние датасеты (встроенные `sklearn`/`seaborn` скачивать не нужно):

   ```bash
   python datasets/download.py
   ```

3. Запустить ноутбуки:

   ```bash
   jupyter notebook labs/
   ```

## Карта курса

| № | Раздел | Лекция | Лабораторная | Датасет | Вопрос экзамена |
|---|--------|--------|--------------|---------|-----------------|
| 1 | Базовый Python | `lectures/00-intro-bigdata-ml.md`, `lectures/01-basic-python.md` | `labs/01-basic-python.ipynb` | синтетика | — |
| 2 | Применение библиотеки Pandas | `lectures/02-pandas.md` | `labs/02-pandas.ipynb` | flights/tips (seaborn) | — |
| 3 | Предобработка данных. Визуализация | `lectures/03-preprocessing.md` | `labs/03-preprocessing.ipynb` | Titanic | 1 |
| 4 | Исследовательский анализ данных | `lectures/04-eda.md` | `labs/04-eda.ipynb` | Penguins | 2 |
| 5 | Описательная статистика | `lectures/05-descriptive-stats.md` | `labs/05-descriptive-stats.ipynb` | синтетика | — |
| 6 | Статистические гипотезы | `lectures/06-hypotheses.md` | `labs/06-hypotheses.ipynb` | A/B (синтетика) | 3 |
| 7 | Введение в машинное обучение | `lectures/07-ml-intro.md` | `labs/07-ml-intro.ipynb` | Iris | 4 |
| 8 | scikit-learn: классификация | `lectures/08-classification.md` | `labs/08-classification.ipynb` | Wine | 4 |
| 9 | scikit-learn: регрессия | `lectures/09-regression.md` | `labs/09-regression.ipynb` | Diabetes | 4 |
| 10 | Оптимизация параметров, кроссвалидация | `lectures/10-cross-validation.md` | `labs/10-cross-validation.ipynb` | Heart | — |
| 11 | Временные ряды | `lectures/11-time-series.md` | `labs/11-time-series.ipynb` | Air Passengers | — |
| 12 | Линейная алгебра (numpy) | `lectures/12-linear-algebra.md` | `labs/12-linear-algebra.ipynb` | синтетика | 6 |
| 13 | Градиентный спуск и бустинг | `lectures/13-gradient-descent.md` | `labs/13-gradient-descent.ipynb` | синтетика | 5 |
| 14 | Машинное обучение для текстов | `lectures/14-nlp.md` | `labs/14-nlp.ipynb` | IMDb (CPU) | — |
| 15 | Нейронные сети | `lectures/15-neural-networks.md` | `labs/15-neural-networks.ipynb` | Fashion-MNIST (CPU) | 7, 8 |
| 16 | Обучение без учителя | `lectures/16-unsupervised.md` | `labs/16-unsupervised.ipynb` | Mall Customers | 9, 10 |

## Примечания по окружению

- Всё рассчитано на **CPU** (без GPU).
- Для текстов используется классический пайплайн `CountVectorizer`/`TfidfVectorizer`
  + логистическая регрессия/MLP; BERT упоминается только в теории.
- Нейросети — библиотека Keras, уменьшенная выборка Fashion-MNIST.
- Внешние датасеты не хранятся в репозитории — загружаются скриптом `datasets/download.py` в игнорируемую папку `datasets/data/`.
