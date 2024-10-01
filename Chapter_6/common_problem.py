# The issue of global shared state
# As we have already mentioned, descriptors need to be set as class attributes to work. This
# should not be a problem most of the time, but it does come with some warnings that need
# to be taken into consideration.
# The problem with class attributes is that they are shared across all instances of that class.
# Descriptors are not an exception here, so if we try to keep data in a descriptor object,
# keep in mind that all of them will have access to the same value.
# Let's see what happens when we incorrectly define a descriptor that keeps the data itself,
# instead of storing it in each object:

class SharedDataDescriptor:
    def __init__(self, initial_value):
        self.value = initial_value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        self.value = value


class ClientClass:
    """
    >>> client1 = ClientClass()
    >>> client1.descriptor
    'first value'
    >>> client2 = ClientClass()
    >>> client2.descriptor
    'first value'
    >>> client2.descriptor = "value for client 2"
    >>> client2.descriptor
    'value for client 2'
    >>> client1.descriptor
    'value for client 2'
    """
    descriptor = SharedDataDescriptor("first value")


from weakref import WeakKeyDictionary


class DescriptorClass:
    def __init__(self, initial_value):
        self.value = initial_value
        self.mapping = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.mapping.get(instance, self.value)

    def __set__(self, instance, value):
        self.mapping[instance] = value
