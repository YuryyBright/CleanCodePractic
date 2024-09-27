from datetime import datetime


class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self) -> dict:
        return {
            "username": self.event.username,
            "password": "**redacted**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d% H: %M"),
        }


class LoginEvent:
    """
    While this works and might look like a good option to start with, as time passes and we
    want to extend our system, we will find some issues:
    Too many classes: As the number of events grows, the number of serialization
    classes will grow in the same order of magnitude, because they are mapped one
    to one.
    The solution is not flexible enough: If we need to reuse parts of the components
    (for example, we need to hide the password in another type of event that also
    has it), we will have to extract this into a function, but also call it repeatedly from
    multiple classes, meaning that we are not reusing that much code after all.
    Boilerplate: The serialize() method will have to be present in all event
    classes, calling the same code. Although we can extract this into another class
    (creating a mixin), it does not seem like a good use of inheritance
    """
    SERIALIZER = LoginEventSerializer

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self):
        return self.SERIALIZER(self).serialize()


def hide_field(field) -> str:
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_original(event_field):
    return event_field


class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in
            self.serialization_fields.items()
        }


class Serialization:
    def __init__(self, **transformations):
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=show_original,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
class LoginEvent:
    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp
