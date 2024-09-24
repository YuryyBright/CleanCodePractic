# The open/closed principle

# The open/closed principle (OCP) states that a module should be both open and closed (but
# with respect to different aspects).

# open to extension but closed for modification.


# Example of maintainability perils for not following the open/closed principle

# SOME BAD WAY
class Event:

    def __init__(self, raw_data):
        self.raw_data = raw_data


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data."""


class LoginEvent(Event):
    """A event representing a user that has just entered the system."""


class LogoutEvent(Event):
    """An event representing a user that has just left the system."""


class SystemMonitor:
    """
    >>> l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    >>> l1.identify_event().__class__.__name__
    'LoginEvent'
    >>> l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    >>> l2.identify_event().__class__.__name__
    'LogoutEvent'
    >>> l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    >>> l3.identify_event().__class__.__name__
    'UnknownEvent'

    """

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if (
                self.event_data["before"]["session"] == 0
                and self.event_data["after"]["session"] == 1
        ):
            return LoginEvent(self.event_data)
        elif (
                self.event_data["before"]["session"] == 1
                and self.event_data["after"]["session"] == 0
        ):
            return LogoutEvent(self.event_data)
        return UnknownEvent(self.event_data)


# SOME BETTER WAY

class Event1:

    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict):
        return False


class UnknownEvent1(Event):
    """A type of event that cannot be identified from its data"""


class LoginEvent1(Event1):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
                event_data["before"]["session"] == 0
                and event_data["after"]["session"] == 1
        )


class LogoutEvent1(Event1):
    """An event representing a user that has just left the system."""

    @staticmethod
    def meets_condition(event_data: dict):
        return (
                event_data["before"]["session"] == 1
                and event_data["after"]["session"] == 0
        )


#### IF we want to create new clas just do >
class TransactionEvent(Event):
    """Represents a transaction that has just occurred on the system."""

    @staticmethod
    def meets_condition(event_data: dict):
        return event_data["after"].get("transaction") is not None


class SystemMonitor1:
    """
    >>> event_data_login = {
        "before": {"session": 0},
        "after": {"session": 1}
    }

    >>> event_data_logout = {
        "before": {"session": 1},
        "after": {"session": 0}
    }

    >>> event_data_unknown = {
        "before": {"session": 1},
        "after": {"session": 2}  # Невідома подія, оскільки сесія не може бути 2
    }

    # Створюємо екземпляри SystemMonitor1 для кожного набору даних
    >>> monitor_login = SystemMonitor1(event_data_login)
    >>> monitor_logout = SystemMonitor1(event_data_logout)
    >>> monitor_unknown = SystemMonitor1(event_data_unknown)

    # Ідентифікуємо події
    >>> event_login = monitor_login.identify_event()
    >>> event_logout = monitor_logout.identify_event()
    >>>event_unknown = monitor_unknown.identify_event()
    # Виводимо результати
    >>> print(type(event_login))  # <class '__main__.LoginEvent1'>
    >>> print(type(event_logout))  # <class '__main__.LogoutEvent1'>
    >>> print(type(event_unknown))  # <class '__main__.UnknownEvent1'>


    FOR NEW CLASS JUST NEED


    >>> l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    >>> l1.identify_event().__class__.__name__
    'LoginEvent'
    >>> l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    >>> l2.identify_event().__class__.__name__
    'LogoutEvent'
    >>> l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    >>> l3.identify_event().__class__.__name__
    'UnknownEvent'
    >>> l4.identify_event().__class__.__name__
    'TransactionEvent'
    """

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event1.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)

