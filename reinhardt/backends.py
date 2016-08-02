from __future__ import unicode_literals
from inspect import getmembers, isfunction


class PermissionBackend(object):

    _model_perm_cache = {}

    def authenticate(self, username, password):
        return None

    def get_model_permissions(self, obj):
        """
        Returns a dict that maps ``codename`` to ``function name``,
        which is defined in the model of obj
        """
        key = "%(app_label)s.%(model_name)s" % {
            'app_label': obj._meta.app_label,
            'model_name': obj._meta.model_name
        }
        if key in self._model_perm_cache:
            return self._model_perm_cache[key]

        self._model_perm_cache[key] = {
            func._codename: func_name
            for func_name, func
            in getmembers(obj._meta.model, isfunction)
            if hasattr(func, '_codename')
        }
        return self._model_perm_cache[key]

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

        model_perms = self.get_model_permissions(obj)
        if perm not in model_perms:
            return False
        perm_func_name = model_perms[perm]
        perm_func = getattr(obj, perm_func_name)

        return perm_func(user_obj)
