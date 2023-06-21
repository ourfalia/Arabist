from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import UserProfile, create_or_update_user_profile


class UserProfileTestCase(TestCase):
    def test_create_or_update_user_profile(self):
        # Disconnect the signal handler temporarily
        post_save.disconnect(create_or_update_user_profile, sender=User)

        # Create a user without triggering the signal handler
        user = User.objects.create(username='testuser')
        UserProfile.objects.create(user=user)

        # Reconnect the signal handler
        post_save.connect(create_or_update_user_profile, sender=User)

        # Trigger the signal manually
        post_save.send(sender=User, instance=user, created=True)

        # Retrieve the UserProfile object
        user_profile = UserProfile.objects.get(user=user)

        # Assert that the UserProfile was created
        self.assertEqual(user_profile.user, user)

        # Modify and save the user
        user.username = 'modifieduser'
        user.save()

        # Retrieve the UserProfile again
        updated_user_profile = UserProfile.objects.get(user=user)

        # Assert that the UserProfile was updated
        self.assertEqual(updated_user_profile.user, user)
