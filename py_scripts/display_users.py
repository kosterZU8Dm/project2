import os
import django
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..'))
sys.path.append(parent_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project2.settings')
django.setup()

from django.contrib.auth.models import User

def display_all_users():
    users = User.objects.all()

    print("Список пользователей:")
    for user in users:
        print(f"Имя пользователя: {user.username}, Email: {user.email}, Имя: {user.first_name}, Фамилия: {user.last_name}")

if __name__ == '__main__':
    display_all_users()
