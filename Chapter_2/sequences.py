class Items:
    def __init__(self, *values):
        """
        In the case that your class is a wrapper around a standard library object, you might as well
        delegate the behavior as much as possible to the underlying object. This means that if your
        class is actually a wrapper on the list, call all of the same methods on that list to make sure
        that it remains compatible. In the following listing, we can see an example of how an object
        wraps a list, and for the methods we are interested in, we just delegate to its corresponding
        version on the list object:
        Parameters
        ----------
        values :
        """
        self._values = values

    def __len__(self):
        raise len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)

    def __repr__(self):
        return {self._values}


my_items = Items(1, 3, 4, 5, 6, 7, 8, 9)


