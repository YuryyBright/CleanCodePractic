# __get__(self, instance, owner)
# The first parameter, instance, refers to the object from which the descriptor is being
# called. In our first example, this would mean the client object


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return f"{self.__class__.__name__}.{owner.__name__}"
        return f"value for {instance}"


class ClientClass:
    descriptor = DescriptorClass()


cls = ClientClass()
print(cls.descriptor)


