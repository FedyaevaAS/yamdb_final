# Проект YaMDb

### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
На основе оценок пользователей формируется рейтинг. 

Реализован автоматический запуск тестов, обновление образов на Docker Hub, автоматический деплой на сервер при пуше в главную ветку main.

### Стек
- Python
- Django
- PostgreSQL
- nginx
- gunicorn
- Docker
- Яндекс.Облако

## Запуск проекта

### Начало работы
Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/FedyaevaAS/yamdb_final
```
```
cd yamdb_final
```
### Запуск проекта локально
- Установите Docker, используя инструкции с официального сайта:
https://www.docker.com/products/docker-desktop/
- Создайте файл .env в директории yamdb_final/infra со следующим содержимым:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    POSTGRES_USER=<логин для подключения к базе данных>
    POSTGRES_PASSWORD=<пароль для подключения к базе данных>
    DB_HOST=<название контейнера>
    DB_PORT=<порт для подключения к БД>
    ```
- Перейдите в директорию yamdb_final/infra и выполните команды для запуска приложения в контейнерах

    - Собрать и запустить контейнеры:
        ```
        docker-compose up -d --build
        ```
    - Выполнить миграции:
        ```
        docker-compose exec web python manage.py migrate
        ```
    - Создать суперпользователя:
        ```
        docker-compose exec web python manage.py createsuperuser
        ```
    - Собрать статику:
        ```
        docker-compose exec web python manage.py collectstatic --no-input
        ```
    - Остановить контейнеры:
        ```
        docker-compose down -v 
        ```
### Запуск проекта на удаленном сервере
- Установите docker на сервер:
    ```
    sudo apt install docker.io
    ```
- Установите docker-compose на сервер:
    ```
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    ```
- Отредактируйте файл nginx.conf, вписав в server_name IP сервера
- Скопируйте файлы docker-compose.yml и nginx.conf из репозитория на сервер:
    ```
    scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
    scp nginx.conf <username>@<host>:/home/<username>/nginx.conf
    ```
- Запустите контейнеры теми же командами, что и при локальном запуске, добавив в начале ```sudo```. Например, команда сборки и запуска контейнеров:
    ```
    sudo docker-compose up -d --build
    ```

## Доступные страницы:
Если проект развернут на удаленном сервере, то вместо 127.0.0.1 используйте адрес сервера
- http://127.0.0.1/redoc/
- http://127.0.0.1/api/v1/
- http://127.0.0.1/admin/

### Настройка Workflow
Добавьте в Secrets, Action на GitHub переменные окружения:
```
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
POSTGRES_USER=<логин для подключения к базе данных>
POSTGRES_PASSWORD=<пароль для подключения к базе данных>
DB_HOST=<название контейнера>
DB_PORT=<порт для подключения к БД>

DOCKER_PASSWORD=<пароль от DockerHub>
DOCKER_USERNAME=<имя пользователя>

SECRET_KEY=<секретный ключ проекта django>

USER=<username для подключения к серверу>
HOST=<IP сервера>
PASSPHRASE=<пароль для сервера, если он установлен>
SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

TELEGRAM_TO=<ID чата, в который придет сообщение>
TELEGRAM_TOKEN=<токен вашего бота>
```
### Автор
Федяева Анастасия

![example workflow](https://github.com/FedyaevaAS/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
