# RocketData_Django_test
Платформа торговых сетей с авторизацией по JWT.
Фреймворк: Django+DRF+Celery
База данных: PostgreSQL
###### Доступные адресса запросов:

1. .../api/sale_objects/ (GET, POST)
2. .../api/sale_objects/{id}/ (GET, PUT, PATCH, DEL)
3. .../api/product/ (POST)
4. .../api/product/{id}/ (PUT, PATCH, DEL)
5. .../api/token/ (POST)
6. .../api/token/refresh/ (POST)

### Установка:

```
git clone git@github.com:BaikoIlya/RocketData_Django_test.git
```

```
cd RocketData_Django_test
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в рабочую директорию:

```
cd sales_structure
```

Выполнить миграции и создайте суперпользователя:

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Заполните базу данных тестовыми данными:

```
python data_for_db.py
```

Запустить проект:

```
python3 manage.py runserver
```

Для запуска Сelery запустите Redis в контейнере командой:

```
docker run -d -p 6379:6379 redis
```

Запустите 2 дополнительных терминала:
В первом выпоните команду:
для Windows:
```
celery -A sales_structure worker -l info -P gevent
```
для Linux
```
celery -A sales_structure worker -l info
```
Во втором:
```
celery -A sales_structure beat -l info 
```

### Принцип работы:

Через супер юзера создайте пользователя. Используя username и пароль получите JWT токен.
Обычный пользователь может получить доступ только к объектам в которых он отмечен сотрудником,создавать объекты, а так же может создавать,обновлять и удалять продукты.
Для просмотра всех объектов `api/sale_objects/` c приминении фильтра по стране и продукты пользователь должен быть со статусом `is_stuff=True`
