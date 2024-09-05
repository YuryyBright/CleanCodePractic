import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_valid_email(potentially_valid_email: str):
    """
    #to protect certain information about the user from being incorrect, such as their email, as shown in the following code:
    Parameters
    ----------
    potentially_valid_email :

    Returns
    -------

    """
    return re.match(EMAIL_FORMAT, potentially_valid_email)


class User:
    def __init__(self, user_name: str):
        self.username = user_name
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"Can't set {new_email} as it's not a valid email")
        self._email = new_email


#  EXAMPLE
# user = User('Jon')
#
# user.email = '134@ukr.net'


######################### ITERATOR #########################

# Iteration works in Python by its own protocol (namely the iteration protocol). When you try
# to iterate an object in the form for e in myobject:..., what Python checks at a very
# high level are the following two things, in order:
# If the object contains one of the iterator methods—__next__ or __iter__
# If the object is a sequence and has __len__ and __getitem_

from datetime import timedelta, date


class DateRangeIterable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, date):
            raise ValueError('Var must be data')
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.getter
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, date):
            raise ValueError('Var must be data')
        self._end_date = end_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today

    def __repr__(self):

        return f"Class DateRangeGenerable start: {self._start_date} - end: {self._end_date}, present_day: {self._present_day}"


# for day in DateRangeIterable(date(2018, 1, 1), date(2018, 1, 4)):
#     print(day)

my_calendar = DateRangeIterable(date(2018, 1, 1), date(2018, 1, 4))

for day in my_calendar:
    # print(day)
    break


# We can iterable only one case
# for day in my_calendar:
#     print(day)


class DateRangeGenerable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    @property
    def start_date(self):
        return self._start_date

    @start_date.getter
    def end_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, date):
            raise ValueError('Var must be data')
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.getter
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, date):
            raise ValueError('Var must be data')
        self._end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

    def __repr__(self):
        return f"Class DateRangeGenerable start: {self._start_date} - end {self._end_date}"


my_calendar = DateRangeGenerable(date(2018, 1, 1), date(2018, 1, 4))

for day in my_calendar:
    # print(day)
    break

# print('step two')
for day in my_calendar:
    # print(day)
    break

# Обидва класи реалізують ітерацію по діапазону дат, але роблять це різними способами. Давайте розглянемо відмінності між ними.
# #
# # 1. DateRangeIterable
# # Опис:
# #
# # Цей клас реалізує ітератор, який зберігає стан (поточну дату) в атрибуті _present_day.
# # Метод __next__() відповідає за повернення наступної дати в діапазоні.
# # Ключові моменти:
# #
# # Стан: Клас зберігає стан у _present_day, що означає, що після завершення ітерації ви не зможете повторно ітерувати по тому ж об'єкту без його повторної ініціалізації.
# # Методи: Реалізує методи __iter__() і __next__(), що робить його ітератором.
# # Використання: Після завершення ітерації, якщо ви спробуєте знову ітерувати по тому ж об'єкту, ви не отримаєте жодних значень, оскільки _present_day вже досягне end_date.
# # 2. DateRangeGenerable
# # Опис:
# #
# # Цей клас реалізує генератор, який використовує yield для повернення значень.
# # Метод __iter__() є генератором, який генерує дати по мірі їх запиту.
# # Ключові моменти:
# #
# # Стан: Клас не зберігає стан у класі. Замість цього, при кожному виклику __iter__(), він починає нову ітерацію з start_date.
# # Методи: Реалізує лише метод __iter__(), який є генератором. Метод __next__() не реалізується, оскільки генератори автоматично обробляють це.
# # Використання: Ви можете ітерувати по об'єкту кілька разів, і кожен раз ітерація почнеться з start_date.



# The implementation with an iterable will use less memory, but it takes up to O(n) to get an
# element, whereas implementing a sequence will use more memory (because we have to
# hold everything at once), but supports indexing in constant time, O(1).
# This is what the new implementation might look like:


class CustomDataDescriptor:

    @classmethod
    def verify_val(cls, val):
        if not isinstance(val, date):
            raise ValueError('Var must be data')

    def __set_name__(self, owner, name):
        self.name = '_'+name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, val):
        self.verify_val(val)
        setattr(instance,self.name, val)

class DateRangeSequence:
    start_date = CustomDataDescriptor()
    end_date = CustomDataDescriptor()

    def __init__(self, start_date, end_day):
        self.start_date = start_date
        self.end_day = end_day
        self._range = self._create_range()

    def _create_range(self):
        days = []

        current_day = self.start_date

        while current_day< self.end_day:
            days.append(current_day)
            current_day+=timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)



my_sequence_day = DateRangeSequence(date(2018, 1, 1), date(2018, 1, 5))


for day in my_sequence_day:
    print(day)

print(my_sequence_day[-1])