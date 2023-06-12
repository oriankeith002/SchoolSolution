from django.test import TestCase,Client
from django.urls import reverse
from factories import UserFactory
# Create your tests here.

class TestApp(TestCase):

    def test_ok(self):
        """The Application returns 200 OK """
        client = Client() 
        user = UserFactory() # create user object
        client.force_login(user)
        response = client.get(reverse('app'))
        self.assertEqual(response.status_code,200)

  
    def test_unathenticated_access(self):
        """Unauthenticated Users are redirected to the login page"""
        client = Client()
        response = client.get(reverse('app'))
        self.assertEqual(response.status_code,302)
        self.assertIn(reverse("account_login"), response.get("Location"))