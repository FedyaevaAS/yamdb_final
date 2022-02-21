# yamdb_final
yamdb_final
Адрес сервера - 51.250.13.21

### Команды для запуска приложения в контейнерах
Собрать и запустить контейнеры:
```
docker-compose up -d --build
```
Выполнить миграции:
```
docker-compose exec web python manage.py migrate
```
Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```
Собрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Остановить контейнеры:
```
docker-compose down -v 
```
### Автор
Федяева Анастасия

![example workflow](https://github.com/FedyaevaAS/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)