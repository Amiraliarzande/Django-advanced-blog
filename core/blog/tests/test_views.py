from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from datetime import datetime
from accounts.models.accounts import User
from accounts.models.profiles import Profile
from blog.models import Post

class test_post_view(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="amiraliarznade@gmail.com",password="amirali1384")
        self.user.is_active = True  
        self.user.save()
        self.profile= Profile.objects.create(
            user=self.user,
            first_name="ali",
            last_name="arzande",
            desciption="jnlsndl",
        )
        self.post = Post.objects.create(
            author=self.profile,
            status=True,
            category=None,
            content="dsbkjs",
            published_at = datetime.now(),
            title="ksdksdnk",
        )

    def test_view_returns_correct_response_and_template(self):
        url = reverse("blog:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,template_name="blog/post_list.html")
        self.assertTrue(str(response.content).find("Articles"))

    def test_post_detail_view(self):
        self.client.force_login(self.user)
        url = reverse("blog:post_detail",kwargs={"pk":self.post.id})
        response = self.client.get(url)
        if response.status_code == 302:
            print(f"Redirected to: {response.url}")
        self.assertEqual(response.status_code, 200)
