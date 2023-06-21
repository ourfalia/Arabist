from django.test.client import RequestFactory
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from profiles.views import profile_view


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

    def test_profile_view_unauthenticated(self):
        client = self.client
        response = client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_profile_view_authenticated(self):
        client = self.client
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_view_requires_login(self):
        client = self.client
        response = client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_profile_view_with_anonymous_user(self):
        client = self.client
        request = self.factory.get(reverse('profile'))
        request.user = AnonymousUser()
        response = client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/profile/')
