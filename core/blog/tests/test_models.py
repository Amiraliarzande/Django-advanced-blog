from django.test import TestCase, SimpleTestCase
from datetime import datetime
from accounts.models.profiles import Profile
from accounts.models.accounts import User
from ..models import Post

class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="amiraliarznade@gmail.com",password="amirali1384")
        self.profile= Profile.objects.create(
            user=self.user,
            first_name="ali",
            last_name="arzande",
            desciption="jnlsndl",
        )

    def test_create_post_with_vaild_data(self):

        post = Post.objects.create(
            author=self.profile,
            status=True,
            category=None,
            content="dsbkjs",
            published_at = datetime.now(),
            title="ksdksdnk",
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())