from django.test import TestCase, SimpleTestCase
from datetime import datetime
from accounts.models.profiles import Profile
from accounts.models.accounts import User
from ..models import Post

class TestPostModel(TestCase):
    def test_create_post_with_vaild_data(self):
        user = User.objects.create_user(email="amiraliarznade@gmail.com",password="amirali1384")
        profile= Profile.objects.create(
            user=user,
            first_name="ali",
            last_name="arzande",
            desciption="jnlsndl",
        )
        post = Post.objects.create(
            author=profile,
            status=True,
            category=None,
            content="dsbkjs",
            published_at = datetime.now(),
            title="ksdksdnk",
        )
        self.assertEquals(post.content,"dsbkjs")