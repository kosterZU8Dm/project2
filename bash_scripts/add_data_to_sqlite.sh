#!/bin/bash

export DJANGO_SETTINGS_MODULE="project2.settings"
export PYTHONPATH="/mnt/c/Users/ADMIN/Desktop/projects/project2/project2"

# title="Название поста"
# content="Содержание поста"
read -p "Введите название поста: " title
# -p используется для вывода приглашения
read -p "Введите содержание поста: " content
author_id=1
# created_at="2024-01-29 12:00:00"

python manage.py shell <<EOF
from blog.models import Post, User
from django.utils import timezone

author = User.objects.get(id=$author_id)
post = Post.objects.create(title="$title", content="$content", author=author, created_at=timezone.now())

print("Post added with ID:", post.id)
EOF