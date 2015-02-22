"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from bookingsystem.models import Client


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TestMemberStatusChange(TestCase):
    def setUp(self):
        Client.objects.create(uid=1, firstname="Atanas", lastname = "Pamukchiev", email="atanas.pam@gmail.com", telephone="021312213", age=21, ismember=False, managedby=NULL, belongsto=1, genderid=1, experiencelevel=8)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        client = Client.objects.filter(uid=1)
        client.ismember=True
        self.assertEqual(client.ismember, True)
