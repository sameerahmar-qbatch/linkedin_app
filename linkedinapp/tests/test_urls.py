from django.test import SimpleTestCase
from django.urls import reverse, resolve
from linkedinapp.views import home, register, login


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
