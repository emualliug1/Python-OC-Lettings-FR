from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="TestUser",
            password="TestPassword",
            email="test_user@test.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Nantes")

    def test_profiles_index(self):
        url = reverse('profiles:index')
        response = self.client.get(url)
        html = response.content.decode()
        expected_content = "<title>Profiles</title>"
        assert response.status_code == 200
        assert expected_content in html

    def test_profile_detail(self):
        url = reverse('profiles:profile', args=['TestUser'])
        response = self.client.get(url)
        html = response.content.decode()
        expected_content = "<title>TestUser</title>"
        assert response.status_code == 200
        assert expected_content in html
