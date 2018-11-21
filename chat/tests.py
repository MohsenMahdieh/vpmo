from django.test import TestCase, Client
from django.shortcuts import reverse
from django.conf import settings

from vpmoauth.models import MyUser
from vpmotree.models import Project

from create_base_permissions import create_base_permissions


# Create your tests here.
class ChannelsTestCase(TestCase):
    client = Client()

    def setUp(self):
        create_base_permissions()

        user_creds = {
            "username": "TestUser2",
            "email": "TestUser@vpmotest.com",
            "fullname": "Test User"
        }
        self.user = MyUser.objects.create(**user_creds)
        self.client.force_login(self.user)

        self.project = Project(name="Test Proj", project_owner=self.user)
        self.project.save()
        self.project.create_channel()

        # This adds the user to the project
        self.user.assign_role("project_admin", self.project)

        print(dir(self.project.get_users_in_channel()[0]))

    def tearDown(self):
        self.project.delete_channel()

    def test_token_generation(self):
        url = reverse("chat:twilio-token")

        r = self.client.get(url)

        self.assertEqual(r.status_code, 200)

    def test_channel_list(self):
        url = reverse("chat:user-channels")

        r = self.client.get(url)

        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
