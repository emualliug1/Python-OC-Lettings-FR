from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Profile


class ProfilesTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Test",
            last_name="User",
            username="TestUser",
            password="test123456",
            email="testUser@testing.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_setup(self):
        test_user = User.objects.get(username='TestUser')

        assert test_user in User.objects.all()

    def test_profiles_index(self):
        url = reverse('profiles:index')
        response = self.client.get(url)
        html = response.content.decode()
        expected_content = "<title>Profiles</title>"
        assert response.status_code == 200
        assert expected_content in html

    def test_profile_detail(self):
        url = reverse('profiles:profile', args=["TestUser"])
        url2 = '/profiles/TestUser/'
        response = self.client.get(url2)
        html = response.content.decode()
        expected_content = "<title>TestUser</title>"
        assert response.status_code == 200
        assert expected_content in html
