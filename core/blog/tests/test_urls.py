from django.test import TestCase, SimpleTestCase
from django.urls import resolve,reverse

from ..views import postListView
# Create your tests here.

class TestUrl(TestCase):

    def test_blog_index_resolve(self):
        url = reverse("blog:home")
        self.assertEquals(resolve(url).func.view_class,postListView)



    