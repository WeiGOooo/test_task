# yamdb_final
***
Проект YaMDb собирает отзывы пользователей на различные произведения.


### Возможности:
* Устанавливается из контейнера Docker
* Регистрация (по ник-нейму и электронной почте)
* Получение токена (по ник-нейму и коду подтверждения почты)
* Написание отзыва для произведений 
* Оценка произведений по шкале от 1 до 10
* Комментирование отзыва
* Админ может создавать/удалять жанры, категории, произведения
* Админ может назначать модераторов из пользователей
***
### Как запустить проект:

## Установка
1. Установка docker и docker-compose
Инструкция по установке доступна в официальной инструкции

2. Создать файл .env с переменными окружения
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # Имя базы данных
POSTGRES_USER=postgres # Администратор базы данных
POSTGRES_PASSWORD=postgres # Пароль администратора
DB_HOST=db
DB_PORT=5432
SECRET_KEY=SECRET_KEY - секретный ключ шифрования Django

3. Сборка и запуск контейнера
docker-compose up -d --build
4. Миграции
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
5. Сбор статики
docker-compose exec web python manage.py collectstatic --noinput
6. Создание суперпользователя Django
docker-compose exec web python manage.py createsuperuser

Документация доступна по адресу:
http://127.0.0.1/redoc/
***
### Пример работы API:

Запрос для создания поста:
```python
import requests
from pprint import pprint
url = 'http://127.0.0.1/api/v1/categories/'
request = requests.get(url).json()
pprint(request)
```
Ответ от API:
```json
{"count": 3,
 "next": "None",
 "previous": "None",
 "results": [{"name": "Фильм", "slug": "movie"},
             {"name": "Книга", "slug": "book"},
             {"name": "Музыка", "slug": "music"}]}
```
