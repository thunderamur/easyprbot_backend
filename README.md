# Сервис событий

Сделать сервис событий. Сервис должен быть реализован как SPA-приложение.

Пользователь создает событие (встреча, звонок и т.д.) с заголовком, содержанием и датой проведения. Пользователь должен иметь возможность совершать CRUD-операции над своими событиями. Искать по заголовку и фильтровать по дате (события за последние месяц, неделю, день) 
За час до проведения события, сервис отправляет напоминание по e-mail автору.

#### Технологии: ####

Python3, Django, DRF, vuejs, postgresql

## Запуск проекта для разработки
1. Устанавливаем:
    ```
    docker-compose, virtualenv, python3-wheel
    ```
1. В корне проекта запускаем сборку
    ```
    docker-compose build
    ```
1. Запускаем контейнеры
    ```
    docker-compose up
    ```
1. Создаем виртуальное окружение python3. И далее работаем только в нем.
1. Для загрузки переменных окружения нужно добавить в конец bin/activate виртуального окружения:
    ```bash
    # Load env file
    set -a
    . <project_path>/config/dev.env
    set +a
    ```
1. Устанавливаем зависимости в проект
    ```
    pip install -r requirements.in
    pip install -r requirements.dev.in
    ```
1. В /etc/hosts добавим db
    ```
    127.0.0.1	localhost db
    ```
1. Создаем и применяем миграции
    ```
    ./manage.py migrate
    ```
1. Собираем статику
    ```
   docker-compose exec -it django /bin/sh
   ./manage.py collectstatic
    ```
1. Создаем суперпользователя
    ```
    docker-compose exec django ./manage.py createsuperuser
    ```
1. Добавляем в cron хоста вызов функции отправки уведомлений
    ```
    docker-compose exec django ./manage.py make_notify
    ```
1. Загружаем фикстуры
    ```
    ./manage.py loaddata fixtures/*
    ```

## Сброс миграций
```shell script
bash utils/reset_migrations.sh
```
