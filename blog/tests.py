from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Создаем тестовый пост
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user
        )

    def test_post_displayed_on_webpage(self):
        # Имитируем клиента (браузер)
        response = self.client.get('/blog/')  # Замените '/blog/' на ваш URL, где отображаются посты

        # Проверяем, что страница успешно загружена
        self.assertEqual(response.status_code, 200)

        # Проверяем, что содержимое поста отображается на странице
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post content.')
        self.assertContains(response, 'Author: testuser')