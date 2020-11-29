# TDD -> i make first the test and then the model

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # Test creating a user with an email is successful
        email = 'none@gmail.com'
        password = 'Testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # i run here some assertions to test that the email is the above field
        self.assertEqual(user.email, email)
        # it returns true if the pass is true
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        # test the email for a new user is normalized
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        #test creating user with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_superuser(self):
        # test creating a new superuser
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        # the superuser is included in the PermissionsMixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
