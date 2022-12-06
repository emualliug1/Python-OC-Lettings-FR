import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles-index')
    response = client.get(url)
    html = response.content.decode()
    expected_content = "<title>Profiles</title>"
    assert expected_content in html
    assert response.status_code == 200


@pytest.mark.django_db
def test_profiles_detail(client):
    url = reverse('profiles-detail', kwargs={'username': '4meRomance'})
    response = client.get(url[1:])
    html = response.content.decode()
    expected_content = "title"
    assert expected_content in html
