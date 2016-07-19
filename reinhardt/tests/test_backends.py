from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth import get_user_model
from reinhardt.tests.models import Inquiry


class PermissionBackendTestCase(TestCase):

    def setUp(self):
        self.user1 = get_user_model().objects.create(
            username='nanase'
        )
        self.user2 = get_user_model().objects.create(
            username='maiyan'
        )
        self.inquiry = Inquiry.objects.create(
            writer=self.user1,
            text='How can I delete my account?'
        )

    def test_has_perm(self):
        self.assertTrue(
            self.user1.has_perm('tests.add_inquiry', obj=self.inquiry)
        )
        self.assertFalse(
            self.user2.has_perm('tests.add_inquiry', obj=self.inquiry)
        )
