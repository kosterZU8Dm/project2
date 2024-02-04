import os
import django
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..'))
sys.path.append(parent_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '..project2.settings')
# указывает Django, какие настройки использовать
django.setup()
# вызов инициализирует конфигурацию Django

from django.contrib.auth.models import User

def create_user():
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    email = input('Введите адрес электронной почты: ')
    first_name = input('Введите имя (необязательно): ')
    last_name = input('Введите фамилию (необязательно): ')

    try:
        user = User.objects.create_user(username=username, password=password, email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        print(f'Пользователь {username} успешно создан.')
    except Exception as e:
        print(f'Ошибка при создании пользователя: {e}')

if __name__ == '__main__':
    create_user()
