===============================
django-reinhardt
===============================


.. image:: https://img.shields.io/pypi/v/django-reinhardt.svg
        :target: https://pypi.python.org/pypi/django-reinhardt

.. image:: https://img.shields.io/travis/momamene/django-reinhardt.svg
        :target: https://travis-ci.org/momamene/django-reinhardt

.. image:: https://readthedocs.org/projects/django-reinhardt/badge/?version=latest
        :target: https://django-reinhardt.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/momamene/django-reinhardt/shield.svg
        :target: https://pyup.io/repos/github/momamene/django-reinhardt/
        :alt: Updates


There are many object permission backends like `django-guardian <https://github.com/django-guardian/django-guardian>`_ or `django-permission <https://github.com/lambdalisue/django-permission>`_.

But some time, it is needed to define permissions as not just object-user relationship.

`django-reinhardt <https://github.com/momamene/django-reinhardt>`_ make you handle object permissions by defining methods in your django model

* Free software: MIT license
* Documentation: https://django-reinhardt.readthedocs.io.


Installation
------------
Use pip_ like::

    $ pip install django-reinhardt

.. _pip:  https://pypi.python.org/pypi/pip

Usage
-----
Add extra authorization backends in your settings.py::

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend', # default
        'reinhardt.backends.PermissionBackend',
    )

It's done. you don't need to add any app or migrate anything.

Assume that ``Inquiry`` model needs to have two permission: ``change_inqury``, ``view_inquiry``  ::

    class Inquiry(models.Model):

        writer = models.ForeignKey(settings.AUTH_USER_MODEL)
        text = models.TextField()
        pub_date = models.DateTimeField(auto_now_add=True)

        @object_permission(codename='change_inquiry')
        def is_changeable_by(self, user):
            return self.writer == user or user.is_staff

        @object_permission(codename='view_inquiry')
        def is_viewable_by(self, user):
            return self.writer == user

Then you can just define methods having ``user`` parameter, decorated by ``object_permission``.

Now the following codes will work as expected: ::

    user1 = get_user_model().objects.create(
        username='nanase'
    )
    user2 = get_user_model().objects.create(
        username='maiyan'
    )
    user3 = get_user_model().objects.create(
        username='ikuta'
    )
    inquiry = Inquiry.objects.create(
        writer=self.user1,
        text='How can I delete my account?'
    )

    assert user1.has_perm('yourapp.change_inquiry', obj=inquiry) == True
    assert user2.has_perm('yourapp.view_inquiry', obj=inquiry) == False
    assert user3.has_perm('yourapp.change_inquiry', obj=inquiry) == False
    assert user3.has_perm('yourapp.view_inquiry', obj=inquiry) == True


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
