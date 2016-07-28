from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Inquiry(models.Model):

    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def can_change_inquiry(self, user):
        return self.writer == user

    def can_view_inquiry(self, user):
        return self.writer == user or user.is_staff
