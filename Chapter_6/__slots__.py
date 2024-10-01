class Coordinate2D:
    """
    >>>cord = Coordinate2D(1, 2)
    >>>cord.some_attr = 'vaal'
    Traceback (most recent call last):
    ^^^^^^^
    AttributeError: 'Coordinate2D' object has no attribute some_attr
    """
    __slots__ = ("lat", "long")

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lat}, {self.long})"

