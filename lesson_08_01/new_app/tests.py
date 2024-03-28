from django.test import TestCase
from .models import Author, Post, Category
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Create your tests here.

class TestMainPage(TestCase):

    def test_main_page(self):
        url = ''

        response = self.client.get(url)

        print(response.context)


class TestPost(TestCase):

    def setUp(self) -> None:
        self.author = Author.objects.create(name='test_author', bio='test_bio', email='test@test.com')
        self.post = Post.objects.create(title='test_post', content='test_content', views=3, author_id=self.author)
        self.category = Category.objects.create(name='test_cat', description='test_desc')
        self.username = 'admin'
        self.password = 'password'
        self.user = User.objects.create_superuser(username=self.username, password=self.password)

    def test_get_posts(self):
        self.client.force_login(self.user)
        url = reverse_lazy('post_list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_get_authors(self):
        self.client.force_login(self.user)
        url = reverse_lazy('post_list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200) # ==
        self.assertIn(self.post, response.context['object_list'])

    def test_create_author(self):
        url = reverse_lazy('post_create')
        data = {
            'title': 'test_title_2',
            'content': 'test_content',
            'views': 3,
            'author_id': self.author.pk,
            'categories': [self.category.pk],
            'status': 'p'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        new_post = Post.objects.filter(title=data['title']).exists()
        self.assertTrue(new_post)
