from django.test import TestCase
from django.urls import reverse
from .models import Post
from .forms import PostForm

class CreatePostViewTest(TestCase):

    def setUp(self):
        pass

    def test_get_create_post(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/create_post.html')
        self.assertIsInstance(response.context['form'], PostForm)

    def test_post_create_post_invalid(self):
        response = self.client.post(reverse('create_post'), {'title': '', 'content': ''})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/create_post.html')
        self.assertFalse(Post.objects.filter(title='', content='').exists())
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)