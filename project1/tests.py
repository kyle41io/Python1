from django.http import response
from django.test import TestCase,  SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_project1_page_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)