import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles:index')
    response = client.get(url)
    html = response.content.decode()
    expected_content = "<title>Profiles</title>"
    assert response.status_code == 200
    assert expected_content in html


@pytest.mark.django_db
def test_profile_detail(client):
    url = reverse('profiles:profile', kwargs={'username': '4meRomance'})
    response = client.get(url)
    html = response.content.decode()
    expected_content = "<title>HeadlinesGazer</title>"
    assert response.status_code == 200
    assert expected_content in html
