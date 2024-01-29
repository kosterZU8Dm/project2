# scheme of project2:

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
---
# tests
```
python3 manage.py test blog.tests
```