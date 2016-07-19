from __future__ import unicode_literals


class PermissionBackend(object):

    PREFIX = 'can'

    def authenticate(self, username, password):
        return None

    def has_perm(self, user_obj, perm, obj=None):
        if obj is None:
            return False
        if '.' in perm:
            app_label, perm = perm.split('.')
            if app_label != obj._meta.app_label:
                raise Exception(
                    "App label of given obj '%s' doesn't "
                    "match with app label of perm '%s'" % (
                        obj._meta.app_label, app_label)
                )

        perm_func = getattr(obj, "%s_%s" % (self.PREFIX, perm))

        if perm_func is None:
            return False

        return perm_func(user_obj)
