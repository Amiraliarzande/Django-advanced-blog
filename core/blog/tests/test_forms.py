from django.test import TestCase, SimpleTestCase
from ..models import Category, Post
from ..forms import PostForm
class TestPostForm(TestCase):
    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name='test')
        form = PostForm(data={
            "title":"test",
            "content":"test",
            "category":category_obj,
            "status": True,
        })
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_valid_data(self):
        form = PostForm(data={
        })
        self.assertFalse(form.is_valid())