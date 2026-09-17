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

## Разработка в VSCode DevContainers

Откройте проект в VSCode и выберите «Reopen in Container» или запустите команду "Dev Containers: Rebuild and Reopen in Container»".
Будет собран образ, проект смонтирован в `/book`, а сервер Jupyter Book автоматически запустится на порту 3000.
Изменения в `*.md` и `*.ipynb` подхватываются сразу -- перезапускать контейнер не нужно.
