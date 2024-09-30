# __set_name__(self, owner, name)
# When we create the descriptor object in the class that is going to use it, we generally
# need the descriptor to know the name of the attribute it is going to be handling.
# This attribute name is the one we use to read from and write to __dict__ in the __get__
# and __set__ methods, respectively.


class DescriptorWithName:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, value):
        if instance is None:
            return self
        print("getting %r attribute from %r", self.name, instance)
        return instance.__dict__[self.name]

    # def __set_name__(self, owner, name):
    #     self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ClientClass:
    """
    Before __set_name__
    >>> client = ClientClass()
    >>> client.descriptor = "value"
    >>> client.descriptor
    INFO:getting 'descriptor' attribute from <ClientClass object at 0x...>
    'value'
    After __set_name__
    """
    descriptor = DescriptorWithName("descriptor")


