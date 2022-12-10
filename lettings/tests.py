import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_lettings_index(client):
    url = reverse('lettings:index')
    response = client.get(url)
    html = response.content.decode()
    expected_content = "<title>Lettings</title>"
    assert response.status_code == 200
    assert expected_content in html


@pytest.mark.django_db
def test_letting_detail(client):
    url = reverse('lettings:letting', args=[1])
    response = client.get(url)
    html = response.content.decode()
    expected_content = "<h1>Test Letting</h1>"
    assert response.status_code == 200
    assert expected_content in html
