# Dependency inversion\


# BAD WAY

# Bad practice: direct dependency on low-level module

# High-level modules directly depend on low-level modules.
# High-level module
class NotificationService:
    """

    # Usage
    >>> notification_service = NotificationService()
    >>> notification_service.notify("Hello via Email!")
    """

    def __init__(self):
        self.email_notifier = EmailNotifier()  # Direct dependency on a low-level module

    def notify(self, message: str):
        self.email_notifier.send(message)


# Low-level module
class EmailNotifier:
    def send(self, message: str):
        print(f"Sending email: {message}")


# Comments:
#
# In this example, NotificationService directly depends on the EmailNotifier class (a low-level module).
# If we want to add another notification method (like SMS), we would have to modify the NotificationService class, which violates the Dependency Inversion Principle.
# This tight coupling makes the code less flexible and harder to maintain.


# GOOD WAY

# Abstraction
class Notifier:
    def send(self, message: str):
        pass


# High-level module
class NotificationService1:

    """
    # Usage
    >>>    email_notifier = EmailNotifier()
    >>>    notification_service = NotificationService(email_notifier)
    >>>    notification_service.notify("Hello via Email!")

    >>>    sms_notifier = SMSNotifier()
    >>>    notification_service = NotificationService(sms_notifier)
    >>>    notification_service.notify("Hello via SMS!")
    """
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)


# Low-level module
class EmailNotifier1(Notifier):
    def send(self, message: str):
        print(f"Sending email: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending SMS: {message}")
