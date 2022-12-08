from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingsTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=77,
            street="test",
            city="test",
            state="test",
            zip_code=44000,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        html = response.content.decode()
        expected_content = "<title>Lettings</title>"
        assert response.status_code == 200
        assert expected_content in html

    def test_letting_detail(self):
        url = reverse('lettings:letting', args=[1])
        response = self.client.get(url)
        html = response.content.decode()
        expected_content = "<h1>Test Letting</h1>"
        assert response.status_code == 200
        assert expected_content in html
