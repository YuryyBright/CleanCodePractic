# Consider the following erroneous function definition
from tomlkit import value


# wrong
def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
    print(user_metadata)
    # pop we use for delete from dict
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"


# best
def user_display(user_metadata: dict = None):
    user_metadata = user_metadata or {"name": "John", "age": 30}
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"



# BAD WAY
class BadList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"

bl = BadList((0, 1, 2, 3, 4, 5))
print(bl[1])
print(bl[2])
# print("".join(bl))
# >>> "".join(bl)
# Traceback (most recent call last):
# ...
# TypeError: sequence item 0: expected str instance, int found




# BEST WAY
from collections import UserList

class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"


bl = GoodList((0, 1, 2, 3, 4, 5))
print(bl[1])
print(bl[2])
print("".join(bl))
