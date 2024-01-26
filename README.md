# scheme of project2:
project2/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       └── post_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── project2/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── .gitignore
├── db.sqlite3
└── README.md
---
# superuser creation
```
python3 manage.py createsuperuser
```
---
# run local server
```
python3 manage.py runserver
```
---
# about migrations
1. python3 manage.py makemigrations\
создает файлы миграции на основе изменений, внесенных в модели данных
2. python3 manage.py migrate\
применяет все созданные миграции к базе данных