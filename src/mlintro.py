import numpy as np
import matplotlib.pyplot as plt

def plot_image_grid(X, n, rows = 1, y=None, cmap='gray_r', figsize=None,
                    image_shape=(28, 28)):
    """
    Раскладывает изображения из X в матрицу m на n.
    
    Параметры
    ---------
    X : np.ndarray, shape (N, D) или (N, H, W)
        Массив изображений.
    rows : int
        Количество строк в сетке.
    n : int
        Количество столбцов в сетке.
    y : np.ndarray, optional
        Метки для подписи каждой картинки.
    cmap : str
        Цветовая карта matplotlib.
    figsize : tuple, optional
        Размер фигуры. По умолчанию подбирается автоматически.
    image_shape : tuple
        Форма одного изображения, если X сплющен (по умолчанию (28, 28)).
    
    Возвращает
    ----------
    fig, axes : объекты matplotlib.
    """
    total = rows * n
    count = min(total, len(X))

    if figsize is None:
        figsize = (n * 1.5, rows * 1.5)

    fig, axes = plt.subplots(rows, n, figsize=figsize)

    # Приводим axes к плоскому массиву (на случай m==1 или n==1)
    axes_flat = np.atleast_1d(axes).ravel()

    for i in range(total):
        ax = axes_flat[i]
        if i < count:
            img = X[i]
            # Если изображение сплющено — восстанавливаем форму
            if img.ndim == 1:
                img = img.reshape(image_shape)
            ax.imshow(img, cmap=cmap, interpolation='nearest')
            if y is not None:
                ax.set_title(str(y[i]), fontsize=9)
        ax.axis('off')

    plt.tight_layout()
    plt.show()
