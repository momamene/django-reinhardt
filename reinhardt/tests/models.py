from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from reinhardt.decorators import object_permission


class Inquiry(models.Model):

    writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    @object_permission(codename='add_inquiry')
    def is_addable_by(self, user):
        return self.writer == user

    @object_permission(codename='change_inquiry')
    def is_changeable_by(self, user):
        return self.writer == user

    @object_permission(codename='delete_inquiry')
    def is_deletable_by(self, user):
        return self.writer == user

    @object_permission(codename='view_inquiry')
    def is_viewable_by(self, user):
        return self.writer == user
