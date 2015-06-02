"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from bookingsystem.models import Client, Block, Session, Payment
from django.contrib.auth.models import User, Group, UserManager
from django.utils import timezone
import datetime


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class InitialSetup(TestCase):
    def setUp(self):
        parent = User.objects.create_user(username="Parent1", email="parent@parents.com", password="There is no pass", first_name = "John", last_name = "Hyfig")

        Client.objects.create(firstname="Atanas", lastname = "Pamukchiev", email="atanas.pam@gmail.com", telephone="021312213", dateofbirth=datetime.date(1993, 10, 9), ismember=False, managedby=0, belongsto=parent, genderid=1, experiencelevel=8)

    def test_empty_child_exists(self):
        self.assertTrue(Client.objects.get(uid=1) is not None)
    def test_empty_block_exists(self):
        block = Block.objects.create(begindate=datetime.date(1993, 10, 9), enddate=datetime.date(1993, 10, 9), label='Some Day Morning', type='Morning')
        self.assertEquals(Block.objects.get(blockid=1).label, 'Some Day Morning')
    def test_empty_session_exists(self):
        block = Block.objects.create(begindate=datetime.date(1993, 10, 9), enddate=datetime.date(1993, 10, 9), label='Some Day Morning', type='Morning')
        session = Session.objects.create(duration=1, begintime=timezone.now(), endtime=timezone.now() + datetime.timedelta(hours=1), block_blockid=block, capacity=1, agegroup="random", skillgroup='RANDOM', isfull=0)
        self.assertEquals(Session.objects.get(sessionid=1).capacity, 1)
    def test_empty_payment_exists(self):
        payment = Payment.objects.create(usertopay=Client.objects.get(uid=1), amount=100, label=1, haspayed=0, duedate=datetime.date.today(), paymenttype=1)
        self.assertTrue(True)

class TestMemberStatusChange(TestCase):
    def setUp(self):

        parentsGroup = Group.objects.create(name="Parent")

        parent = User.objects.create_user(username="Parent1", email="parent@parents.com", password="There is no pass", first_name = "John", last_name = "Hyfig")
        #parent.first_name = "John"
        #parent.last_name = "Hyfig"
        g = Group.objects.get(name='Parent')
        g.user_set.add(parent)
        parent.save()

        Client.objects.create(uid=1, firstname="Atanas", lastname = "Pamukchiev", email="atanas.pam@gmail.com", telephone="021312213", dateofbirth=datetime.date(1993, 10, 9), ismember=False, managedby=0, belongsto=parent, genderid=1, experiencelevel=8)
        Client.objects.create(uid=2, firstname="Mahsa", lastname = "Johnson", email="mahsa.johnson@gmail.com", telephone="034672213", dateofbirth=datetime.date(1998, 8, 15), ismember=False, managedby=0, belongsto=parent, genderid=0, experiencelevel=2)

    def test_child_does_exist(self):
        client = Client.objects.get(uid=1)
        self.assertTrue(client.firstname == "Atanas")

    def test_status_of_member_change(self):
        """Clients can be assigned as members pf the club"""
        client = Client.objects.filter(uid=1)
        client.ismember=True
        self.assertEqual(client.ismember, True)