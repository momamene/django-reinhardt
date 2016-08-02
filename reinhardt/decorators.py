def object_permission(codename=None):
    """
    Decorate method in the Django model to mark that
    this method is for checking object-level permission
    """
    def decorator(func):
        func._codename = codename
        return func
    return decorator
