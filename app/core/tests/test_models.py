from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'azri.mohamad56@gmail.com'
        password = 'Azri3000'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        email = 'azri.mohamad56@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Azri3000')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Azri3000')

    def test_new_user_is_superuser(self):
        '''Test created user is superuser and staff'''
        user = get_user_model().objects.create_superuser(
            email='azri.mohamad56@gmail.com',
            password='Azri3000'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
