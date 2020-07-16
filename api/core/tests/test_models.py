from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = "me@ngelrojasp.com"
        password = "me123456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = 'test@MYEMAIL.COM'
        user = get_user_model().objects.create_user(email, 'me12345')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'me123456')

    def test_create_new_superuser(self):
        """create a new superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@ngelrojasp.com',
            'admin2020'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
