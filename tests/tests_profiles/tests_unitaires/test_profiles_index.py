import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles-index')
    response = client.get(url)
    html = response.content.decode()
    assert "<title>Profiles</title>" in html
    assert response.status_code == 200
