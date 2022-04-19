# blog
 
## Development workflow
Для установки всех зависимостей выполнить `pip install -r requirements.txt`

Для запуска выполнить `python manage.py runserver`

## Запуск Docker-контейнера
1. Запустить файл `docker-compose.yaml`
2. Запустить файл `Dockerfile`

## Методы
1. Создание комментария к посту: http://127.0.0.1:8080/api/v1/post/`номер поста`, Extra Actions - set comment
2. Список комментариев: http://127.0.0.1:8080/api/v1/comments
3. Получение комментариев до 3-го уровня http://127.0.0.1:8080/api/v1/third/post/`номер поста`
