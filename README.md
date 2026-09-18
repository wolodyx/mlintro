# Электронный учебник "Введение в машинное обучение"

## Запуск в Docker

Собрать и запустить локальный сервер (с горячей перезагрузкой):

```bash
docker compose up --build
```

Книга доступна по адресу http://localhost:3000.

Только собрать книгу в статический HTML (`_build/html`):

```bash
docker compose run --rm book jupyter-book build --html
```

Остановить сервер:

```bash
docker compose down
```

Контейнер работает под пользователем `book`, у которого UID/GID совпадают с
пользователем хост-машины (по умолчанию `1000`), поэтому созданные файлы
(например, `_build`) принадлежат вам, а не `root`. Если ваш UID/GID отличаются,
задайте их перед запуском:

```bash
export UID=$(id -u) GID=$(id -g)
docker compose up --build
```

## Разработка в VSCode DevContainers

Откройте проект в VSCode и выберите «Reopen in Container» или запустите команду "Dev Containers: Rebuild and Reopen in Container»".
Будет собран образ, проект смонтирован в `/book`, а сервер Jupyter Book автоматически запустится на порту 3000.
Изменения в `*.md` и `*.ipynb` подхватываются сразу -- перезапускать контейнер не нужно.

## Локальный запуск Jupyter Notebook

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```
