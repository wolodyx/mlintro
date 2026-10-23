# Основы Matplotlib

С визуализацией связан процесс исследования данных.
Существует много инструментов визуализации данных, но Matplotlib -- это самый популярный из них.

В примерах ниже импортирования Matplotlib будут пропускаться.
Поэтому заранее сделайте это.
Общепринято импортировать библиотеку с псевдонимом `plt`:
``` python
import matplotlib.pyplot as plt
```


## Терминология

<!--
Код ниже создает рисунок для иллюстрации составных частей Figure.
``` {code} python
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

np.random.seed(20261023)
X = np.linspace(0.5, 3.5, 100)
Y1 = 3 + np.cos(X)
Y2 = 1 + np.cos(1 + X / 0.75) / 2
Y3 = np.random.uniform(Y1, Y2, len(X))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)

def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.2f" % x

ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(1.000))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))
ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.tick_params(which='major', width=1.0, length=10)
ax.tick_params(which='minor', width=1.0, length=5, labelsize=10, labelcolor='0.25')

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.plot(X, Y1, c=(0.25, 0.25, 1.00), lw=2, label="Blue signal", zorder=10)
ax.plot(X, Y2, c=(1.00, 0.25, 0.25), lw=2, label="Red signal")
ax.plot(X, Y3, linewidth=0, marker='o', markerfacecolor='w', markeredgecolor='k')

ax.set_title("Структура рисунка Matplotlib", fontsize=20, verticalalignment='bottom')
ax.set_xlabel("Подпись оси X")
ax.set_ylabel("Подпись оси Y")

ax.legend()

plt.show()
```
-->

Для понимания Matplotlib следует различать понятия рисунка и графика.
**Рисунок** в Matplotlib -- это верхнеуровневый контейнер, который содержит результаты построения и влияющие на внешний вид атрибуты.
Внутри рисунка располагается один или несколько **графиков** со своими системами координат, данными, подписями осей и делений, заголовком и легендой.

``` {figure} ./excalidraw/matplotlib-figure.excalidraw.png
```

В программном коде рисунок и график представлены классами `Figure` и `Axes`.
Через методы этих классов можно воздействовать на наполнение и оформление связанных с ним графических объектов.
Создание графиков начинается с вызова функции [`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html).
Она возвращает кортеж из двух переменных -- рисунка и графика.
Мы можем вложить в рисунок несколько графиков, если зададим аргументы `nrows` и `ncols`.
В этом случае второй элемент в возвращаемом кортеже будет представлять список графиков.
После оформления графиков функция [`matplotlib.pyplot.show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html) отобразит их на экране.

```python
fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(9,5))
plt.show()
```

``` {figure} ./excalidraw/matplotlib-example1.png
```

В последнем случае `ax` возвращается как двумерный массив Numpy объектов `Axes`.
Оператор индексации (например, `ax[0,0]`) позволяет обратиться к одному объекту-графику.
Если одно из измерений единичное (например, `nrows=1` или `ncols=1`), то `ax` имеет тип одномерного массива и для обращения нужен только один индекс (например, `ax[0]`).

Что мы можем сделать с рисунком `fig`?
Задать:
* заголовок: `fig.suptitle('Заголовок рисунка')`;
* размер: `fig.set_size_inches(9, 5)`;
* цвет фона: `fig.set_facecolor('gray')`;

Повлиять на содержимое графика можно методами `Axes`.
Можно нарисовать линейный график (`plot`), диаграмму рассеяния (`scatter`), тепловую карту(`imshow`) и многие другие типы графиков.
Типы графиков:
* столбчатая диаграмма, [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html);
* гистограмма, [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html);
* линейный график, [`matplotlib.axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html);
* диаграмма рассеяния, [`matplotlib.axes.Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html);
* тепловая карта, [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html);


## Линейный график

**Линейный график** -- это график, на котором точки данных соединены линиями.
Его используют, чтобы показать изменение величины:
* во времени;
* вдоль числовой оси;
* в зависимости от другой переменной.

Линейный график строится методом [`matplotlib.axes.Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html).
Он принимает последовательности значений `x` и `y` и соединяет соседние точки в порядке их следования.
Если передать только одну последовательность, то она будет отложена по оси Y, а по оси X будут использованы индексы `0, 1, 2, ...`.
Основные параметры:
* `color` -- цвет линии;
* `linewidth` (`lw`) -- толщина линии;
* `linestyle` (`ls`) -- стиль линии, например `"-"`, `"--"`, `":"` или `"-."`;
* `marker` -- маркер, которым отмечаются точки, например `"o"`, `"s"` или `"^"`;
* `label` -- подпись линии для легенды.

Несколько вызовов `plot` на одном графике позволяют изобразить сразу несколько зависимостей.
Легенда добавляется методом `Axes.legend`, а подписи осей -- методами `Axes.set_xlabel` и `Axes.set_ylabel`.

```{code-cell} python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)", color="#4c72b0", linewidth=2)
ax.plot(x, np.cos(x), label="cos(x)", color="#dd8452", linestyle="--")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Линейный график")
ax.legend()
ax.grid(True)
plt.show()
```

## Столбчатая диаграмма

**Столбчатая диаграмма** показывает значения категорий в виде столбцов.
Длина столбца пропорциональна значению, поэтому такая диаграмма удобна для сравнения категорий между собой.
Столбцы строятся методом [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html), а горизонтальные столбцы -- методом [`matplotlib.axes.Axes.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html).

Основные параметры:
* `x` -- категории или их числовые позиции;
* `height` -- высоты столбцов (для `barh` -- длины);
* `width` -- ширина столбцов;
* `color` -- цвет столбцов;
* `edgecolor` -- цвет границы столбцов;
* `label` -- подпись для легенды.

Если категорий много или их названия длинные, подписи стоит повернуть методом `Axes.set_xticklabels(..., rotation=45)`.
Для сравнения нескольких рядов столбцы сдвигают вдоль оси X и уменьшают их ширину.

```python
categories = ["A", "B", "C", "D"]
values = [12, 7, 15, 9]
fig, ax = plt.subplots()
ax.bar(categories, values, color="#4c72b0", edgecolor="black")
ax.set_xlabel("Категория")
ax.set_ylabel("Значение")
ax.set_title("Столбчатая диаграмма")
plt.show()
```

## Гистограмма

**Гистограмма** показывает распределение числовой величины.
Диапазон значений разбивается на интервалы -- **бины** (bins), и для каждого бина подсчитывается число попавших в него наблюдений.
Высота столбца равна этому числу, поэтому гистограмма позволяет увидеть:
* типичные значения;
* разброс;
* форму распределения;
* наличие нескольких групп или выбросов.

Гистограмма строится методом [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html).
Основные параметры:
* `bins` -- число бинов или их границы;
* `range` -- диапазон значений, который покрывают бины;
* `density` -- при `True` высоты нормируются так, чтобы площадь под гистограммой равнялась единице;
* `cumulative` -- при `True` строится накопленная гистограмма;
* `histtype` -- тип отрисовки, например `"bar"`, `"step"` или `"stepfilled"`;
* `alpha` -- прозрачность столбцов, удобна при наложении нескольких гистограмм.

Число бинов влияет на вид гистограммы: при слишком малом их количестве теряются детали, а при слишком большом появляется шум.
Если выборки имеют разный объём, для сравнения формы распределений лучше задать `density=True`.

```python
import numpy as np

rng = np.random.default_rng(42)
data = rng.normal(loc=0, scale=1, size=1000)
fig, ax = plt.subplots()
ax.hist(data, bins=30, color="#4c72b0", edgecolor="white", alpha=0.8)
ax.set_xlabel("Значение")
ax.set_ylabel("Частота")
ax.set_title("Гистограмма")
plt.show()
```

## Диаграмма рассеяния

**Диаграмма рассеяния** (scatter plot) изображает наблюдения точками на плоскости.
Координаты точки -- это значения двух признаков, поэтому диаграмма позволяет увидеть связь между переменными:
* направление связи -- положительная или отрицательная;
* силу связи;
* нелинейность;
* группы наблюдений и выбросы.

Диаграмма рассеяния строится методом [`matplotlib.axes.Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html).
Основные параметры:
* `x`, `y` -- значения признаков;
* `s` -- размер точек;
* `c` -- цвет точек или массив значений, который раскрашивается через цветовую карту;
* `cmap` -- цветовая карта, если `c` задан числовым массивом;
* `alpha` -- прозрачность точек, помогает при сильном перекрытии;
* `marker` -- форма маркера;
* `label` -- подпись для легенды.

В отличие от линейного графика, `scatter` не соединяет точки линиями и не зависит от порядка наблюдений.
Если цвет точек кодирует третий признак, к графику добавляют цветовую шкалу через `Figure.colorbar`.

```python
import numpy as np

rng = np.random.default_rng(42)
x = rng.normal(size=200)
y = 2 * x + rng.normal(scale=0.5, size=200)
fig, ax = plt.subplots()
ax.scatter(x, y, s=40, color="#4c72b0", alpha=0.7, edgecolor="black")
ax.set_xlabel("Признак X")
ax.set_ylabel("Признак Y")
ax.set_title("Диаграмма рассеяния")
plt.show()
```

## Тепловая карта

**Тепловая карта** (heatmap) -- это график, на котором числовым ячейкам двумерного массива сопоставлены цвета.
Интенсивность цвета зависит от значения в этой ячейке.
Тепловые карты помогают увидеть структуру массива с высоты.
Ее используют, чтобы увидеть:
* пропуски в данных;
* корреляцию признаков;
* матрицу ошибок классификатора.

**Цветовая карта** (colormap) -- правило, которое преобразует числовое значение в цвет.
Matplotlib предоставляет множество готовых цветовых карт, доступных по имени:
* `"viridis"` -- карта по умолчанию, читаемая даже в чёрно-белом виде и для людей с нарушением цветовосприятия;
* `"gray"` -- оттенки серого;
* `"coolwarm"` -- расходящаяся карта от холодного синего к тёплому красному, удобна для величин с нулём посередине (например, корреляций);
* `"RdBu"` -- красно-синяя расходящаяся карта;
* `"Blues"` -- последовательная карта, нарастающая насыщенность одного цвета.

Полный список доступных карт выводит команда `matplotlib.colormaps`.
``` python
>>> print(plt.colormaps)
ColormapRegistry; available colormaps:
'magma', 'inferno', 'plasma', 'viridis', 'cividis', 'twilight', 'twilight_shifted', 'turbo', 'berlin', 'managua', 'vanimo', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'prism', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'winter', 'Accent', 'okabe_ito', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c', 'grey', 'gist_grey', 'gist_yerg', 'Grays', 'magma_r', 'inferno_r', 'plasma_r', 'viridis_r', 'cividis_r', 'twilight_r', 'twilight_shifted_r', 'turbo_r', 'berlin_r', 'managua_r', 'vanimo_r', 'Blues_r', 'BrBG_r', 'BuGn_r', 'BuPu_r', 'CMRmap_r', 'GnBu_r', 'Greens_r', 'Greys_r', 'OrRd_r', 'Oranges_r', 'PRGn_r', 'PiYG_r', 'PuBu_r', 'PuBuGn_r', 'PuOr_r', 'PuRd_r', 'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r', 'RdYlBu_r', 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 'YlGn_r', 'YlGnBu_r', 'YlOrBr_r', 'YlOrRd_r', 'afmhot_r', 'autumn_r', 'binary_r', 'bone_r', 'brg_r', 'bwr_r', 'cool_r', 'coolwarm_r', 'copper_r', 'cubehelix_r', 'flag_r', 'gist_earth_r', 'gist_gray_r', 'gist_heat_r', 'gist_ncar_r', 'gist_rainbow_r', 'gist_stern_r', 'gist_yarg_r', 'gnuplot_r', 'gnuplot2_r', 'gray_r', 'hot_r', 'hsv_r', 'jet_r', 'nipy_spectral_r', 'ocean_r', 'pink_r', 'prism_r', 'rainbow_r', 'seismic_r', 'spring_r', 'summer_r', 'terrain_r', 'winter_r', 'Accent_r', 'okabe_ito_r', 'Dark2_r', 'Paired_r', 'Pastel1_r', 'Pastel2_r', 'Set1_r', 'Set2_r', 'Set3_r', 'tab10_r', 'tab20_r', 'tab20b_r', 'tab20c_r', 'grey_r', 'gist_grey_r', 'gist_yerg_r', 'Grays_r'
```

Чтобы понять, какое значение какому цвету соответствует, к тепловой карте добавляют **цветовую шкалу** (color bar).
Она создаётся методом `Figure.colorbar`, которому передают объект изображения, возвращённый `imshow`:

Отрисовкой двумерного массива в растровое изображение занимается функция `matplotlib.pyplot.imshow`.
Она принимает следующие параметры:
* `X` -- двумерный массив значений;
* `cmap` -- строка или объект `Colormap`, задающая правило, которое сопоставляет скалярные значения с цветами;
* `aspect` -- соотношение сторон ячейки; значение `"auto"` растягивает ячейки так, чтобы они заполнили область осей, значение `"equal"` делает ячейки квадратными;
* `interpolation` -- строка со способом интерполяции между пикселями; `"nearest"` рисует соседние пиксели без сглаживания, что хорошо для категориальных данных, а `"bilinear"` -- сглаживает;
* `vmin`, `vmax` -- минимальное и максимальное значение, которые соответствуют краям цветовой шкалы. Если их не задать, границы берутся из самих данных.

```python
fig, ax = plt.subplots(figsize=(8, 6))
image = ax.imshow(matrix, cmap="coolwarm", aspect="auto")
fig.colorbar(image, ax=ax, label="Значение")
ax.set_xlabel("Признак")
ax.set_ylabel("Признак")
plt.show()
```

### Визуализация пропусков в данных

Одна из типичных задач при исследовании данных -- поиск пропусков.
Значения `NaN` нельзя изобразить напрямую, поэтому сначала их превращают в булеву маску: `df.isnull()` возвращает таблицу той же формы, где `True` стоит на месте пропуска, а `False` -- на месте заполненной ячейки.
Такая маска -- готовый двумерный массив для `imshow`, где два значения кодируются двумя цветами:
``` {code} python
fig, ax = plt.subplots()
ax.imshow(df.isnull().to_numpy(), aspect="auto", cmap="viridis", interpolation="nearest")
ax.set_yticks([])
ax.set_xticks(range(df.shape[1]))
ax.set_xticklabels(df.columns, rotation=90)
plt.tight_layout()
plt.show()
```

``` {figure} ./excalidraw/matplotlib-missingdata-titanic.png
```

Если данных мало, пропуски можно отобразить на обычной маске в оттенках серого и подписать все ячейки:

``` python
import numpy as np
data = np.array([
    [1.0, 2.0, np.nan],
    [np.nan, 5.0, 6.0],
    [7.0, 8.0, 9.0],
])
mask = np.isnan(data)
fig, ax = plt.subplots()
ax.imshow(mask, cmap="gray_r", aspect="equal")
ax.set_xticks(range(data.shape[1]))
ax.set_yticks(range(data.shape[0]))
plt.show()
```

Здесь карта `"gray_r"` раскрашивает пропуски чёрным на белом фоне: белые ячейки -- заполненные значения, чёрные -- пропуски.

``` {figure} ./excalidraw/matplotlib-missingdata.png
```


## Вопросы для самоконтроля

1. 