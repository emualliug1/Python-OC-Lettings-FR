import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('lettings-index')
    response = client.get(url)
    html = response.content.decode()
    expected_content = "<title>Lettings</title>"
    assert expected_content in html
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail(client):
    url = reverse('lettings-detail', kwargs={'letting_id': 2})
    response = client.get(url[1:])
    html = response.content.decode()
    expected_content = "title"
    assert expected_content in html




