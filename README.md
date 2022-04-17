#Тестовое задание для Junior Backend Developer (Django)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

Проект доступен по [адресу](http://51.250.70.145/)

Админка
```
 Логин -  admin
 Пароль - Kresent101
  ```

## Примеры запросов

####Регистрация пользователя
Запрос (POST /api/users/)
 ```
{
  "email": "vpupkin@yandex.ru",
  "username": "vasya.pupkin",
  "first_name": "Вася",
  "last_name": "Пупкин",
  "password": "User1234"
}
   ```
Ответ 
 ```
 {
    "email": "vpupkin@yandex.ru",
    "id": 2,
    "username": "vasya.pupkin",
    "first_name": "Вася",
    "last_name": "Пупкин"
}
 ```

####Получить токен авторизации
Запрос(POST /api/auth/token/login/)
 ```
{
  "password": "User1234",
  "email": "vpupkin@yandex.ru"
}
 ```
Ответ
 ``
{
    "auth_token": "7395b333d058c4801985e490696cd3b5936b5bd8"
}
 ``

####Cписок постов
Запрос(GET /api/posts)

Ответ
```
"count": 3,
    "next": null,
    "previous": null,
    "results": [
     
        {
            "id": 2,
            "author": {
                "email": "vpupkin@yandex.ru",
                "id": 2,
                "username": "vasya.pupkin",
                "first_name": "Вася",
                "last_name": "Пупкин"
            },
            "name": "Rick and Morty #2",
            "text": "Wubba lubba dub dub"
        },
        {
            "id": 1,
            "author": {
                "email": "vpupkin@yandex.ru",
                "id": 2,
                "username": "vasya.pupkin",
                "first_name": "Вася",
                "last_name": "Пупкин"
            },
            "name": "Rick and Morty #1",
            "text": "Послушай, Морти, я не хочу тебя расстраивать, но то, что люди называют любовью — это просто химическая реакция, принуждающая животных размножаться. Поначалу это сильное чувство, Морти, но потом оно медленно слабеет, оставляя тебя в неудавшемся браке без копейки в кармане. Так было у меня, так будет у твоих родителей. Разорви порочный круг, Морти, будь выше этого, займись наукой."
        }
    ]
}