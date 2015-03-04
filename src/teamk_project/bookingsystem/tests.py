"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from bookingsystem.models import Client
from django.contrib.auth.models import User, Group, UserManager
import datetime


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TestMemberStatusChange(TestCase):
    def setUp(self):

        parentsGroup = Group.objects.create(name="Parent")

        parent = User.objects.create_user(username="Parent1", email="parent@parents.com", password="There is no pass")
        parent.first_name = "John"
        parent.last_name = "Hyfig"
        g = Group.objects.get(name='Parent')
        g.user_set.add(parent)
        parent.save()

        Client.objects.create(uid=1, firstname="Atanas", lastname = "Pamukchiev", email="atanas.pam@gmail.com", telephone="021312213", dateofbirth=datetime.date(1993, 10, 9), ismember=False, managedby=0, belongsto=parent, genderid=1, experiencelevel=8)
        Client.objects.create(uid=2, firstname="Mahsa", lastname = "Johnson", email="mahsa.johnson@gmail.com", telephone="034672213", dateofbirth=datetime.date(1998, 8, 15), ismember=False, managedby=0, belongsto=parent, genderid=0, experiencelevel=2)

    def test_status_of_member_change(self):
        """Clients can be assigned as members pf the club"""
        client = Client.objects.filter(uid=1)
        client.ismember=True
        self.assertEqual(client.ismember, True)
