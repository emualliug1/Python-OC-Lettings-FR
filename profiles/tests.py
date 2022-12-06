import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles-index')
    response = client.get(url)
    html = response.content.decode()
    expected_content = "<title>Profiles</title>"
    assert expected_content in html
    assert response.status_code == 200


class TestProfiles:
    @pytest.mark.django_db
    def setup_method(self):
        self.user = User.objects.create_user(
            first_name='Test',
            last_name='User',
            username='TestUser',
            password='test12345',
            email='testuser@test.com',
            )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris')

    @pytest.mark.django_db
    def test_profiles_detail(self, client):
        url = reverse('profiles-detail', kwargs={'username': 'TestUser'})
        response = client.get(url)
        html = response.content.decode()
        expected_content = "title"
        assert response.status_code == 200
        assert expected_content in html

