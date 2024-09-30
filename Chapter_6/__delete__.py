# __delete__(self, instance)

# This method is called upon with the following statement, in which self would be the
# descriptor attribute, and instance would be the client object in this example:
# >>> del client.descriptor


class ProtectedAttribute:
    def __init__(self, requires_role=None) -> None:
        self.permission_required = requires_role
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, user, value):
        if value is None:
            raise ValueError(f"{self._name} can't be set to None")
        user.__dict__[self._name] = value

    def __delete__(self, user):
        if self.permission_required in user.permissions:
            user.__dict__[self._name] = None
        else:
            raise ValueError(
                f"User {user!s} doesn't have {self.permission_required} "
                "permission"
            )


class User:
    """Only users with "admin" privileges can remove their email
   address.
   >>> admin = User("root", "root@d.com", ["admin"])
    >>> user = User("user", "user1@d.com", ["email", "helpdesk"])
    >>> admin.email
    'root@d.com'
    >>> del admin.email
    >>> admin.email is None
    True
    >>> user.email
    'user1@d.com'
    >>> user.email = None
    ...
    ValueError: email can't be set to None
    >>> del user.email
    ...
    ValueError: User user doesn't have admin permission
   """
    email = ProtectedAttribute(requires_role="admin")

    def __init__(self, username: str, email: str, permission_list: list =
    None) -> None:

        self.username = username
        self.email = email
        self.permissions = permission_list or []

    def __str__(self):
        return self.username
